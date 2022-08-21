"""
This is a "clean" implementation of basic conversion and analyses pulling functionality from other modules together
"""
import subprocess
from forms.math_processor import replace_pairs, replace_return_value, replace_form_references, replace_tool_func_calls
from forms.parser import parse_mmfs
from forms.math_extractor import Extractor as MathExtractor
import os
from utf8cleaner import cleaner
from datetime import datetime
import logging
logging.basicConfig(level=logging.INFO)

# Setup base and target directories for processing
base_dir = "./fed-individual-source"
target_dir = "./fed-individual-py"
target_dir_final = "./fed-individual-py-final"
subs_extracted = './fed-individual-sub1'
subs_stage1_processed = "./fed-individual-sub2"
subs_stage2_processed = "./fed-individual-sub3"
current_dir = os.path.dirname(os.path.abspath(__file__))
PROCESS_DIRS = [base_dir, target_dir, target_dir_final, subs_extracted, subs_stage1_processed, subs_stage2_processed]


def create_all_folders():
    # Creates all folders required for processing
    for fld in PROCESS_DIRS:
        if not os.path.exists(fld):
            os.mkdir(fld)


def list_source_mmf():
    # list of tuples (path_to_file, filename) of mmf files with their relative path
    return [(os.path.join(base_dir, name), name) for name in os.listdir(base_dir) if name.endswith(".mmf")]


def convert_mmf_forms_to_py():
    # check if `.cleaner` file in base_dir (meaning that the utf8cleaner has been already used on files)
    cleaner_flag = os.path.join(base_dir, ".cleaner")
    cleaning_done = os.path.exists(cleaner_flag)

    # remove __init__.py from the target dir
    if os.path.exists(f"{target_dir}/__init__.py"):
        os.remove(f"{target_dir}/__init__.py")

    # let's convert forms to python classes
    for file in [x for x in os.listdir(base_dir) if x.endswith(".mmf")]:
        file_with_path = os.path.join(base_dir, file)

        # clean non-utf charts from files if the cleaning hasn't been done yet
        if not cleaning_done:
            cleaner.clean(file_with_path)
            os.rename(f"{file_with_path}.clean", file_with_path)

        # build python files and save in target dir
        parse_mmfs(file_with_path, target_dir)

        # export math
        extractor = MathExtractor(file_with_path)

    if not cleaning_done:
        open(cleaner_flag, 'w').write("")


def list_all_functions():
    data = MathExtractor.get_all_mmf_functions(base_dir)
    logging.info(f"There are {len(data)} functions in {base_dir} mmf files")


def subs_stage_complete(source_stage_len, subs_stage):
    return source_stage_len == len(os.listdir(os.path.join(current_dir, subs_stage)))


def process_subs_stage1():
    """
    Takes forms files, extracts subs from them into individual files and runs vb2py over them
    """
    subprocess.run(["pwd", ])
    for f, n in list_source_mmf():
        file_to_process = os.path.join(current_dir, subs_extracted, f"{n[:-4]}.bas")
        logging.info(f"Processing {file_to_process}")
        MathExtractor.funcs_to_file(f, os.path.join(subs_extracted, f"{n[:-4]}.bas"))
        subprocess.run(["../forms/convert.sh", os.path.join(current_dir, subs_extracted, f"{n[:-4]}.bas"),
                        os.path.join(current_dir, subs_stage1_processed)])
        os.rename(os.path.join(subs_stage1_processed, "None.py"), os.path.join(subs_stage1_processed, f"{n[:-4]}.py"))


def process_subs_stage2():
    """
    does additional processing on top of subs processed by vb2py
    """
    for f in os.listdir(subs_stage1_processed):
        func = open(os.path.join(subs_stage1_processed, f), 'r').read()
        func = replace_tool_func_calls(func)
        func = replace_form_references(func)
        func = replace_return_value(func)
        with open(os.path.join(subs_stage2_processed, f), "w") as target:
            target.write(func)


def embed_subs():
    for f in os.listdir(target_dir):
        if f in ("__init__.py", ".cleaner", "__pycache__"):
            continue
        form_lines = open(os.path.join(target_dir, f), "r").readlines()
        try:
            sub_lines = open(os.path.join(subs_stage2_processed, f), "r").readlines()
            for line in sub_lines[4:]:
                form_lines.append(f"    {line}")
        finally:
            # Some files have 0 subs, this handles that "gracefully"
            continue
        with open(os.path.join(target_dir_final, f), "w") as target:
            target.writelines(form_lines)


if __name__ == "__main__":
    logging.info(f"{base_dir} contains {len(os.listdir(base_dir))} files")
    start = datetime.now()
    create_all_folders()
    # # assert all folders are created and empty
    convert_mmf_forms_to_py()
    # assert py module length is length of mmf_forms
    list_all_functions()
    fn_len = len(list(filter(
        lambda name: name.endswith(".mmf"),
        os.listdir(os.path.join(base_dir))
    )))
    if not subs_stage_complete(fn_len, subs_stage1_processed):
        # can this be parallelized?
        process_subs_stage1()
    if not subs_stage_complete(fn_len, subs_stage2_processed):
        process_subs_stage2()

    embed_subs()
    time_spent = datetime.now() - start
    logging.info(f"Done in {time_spent.total_seconds()} seconds")
