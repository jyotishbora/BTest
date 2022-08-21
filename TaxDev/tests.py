import re
from unittest.mock import patch
import unittest
import inspect
from types import ModuleType
import os
from TaxDev.convert import convert_mmf_forms_to_py, process_subs_stage1, process_subs_stage2, embed_subs


class ConverterTests(unittest.TestCase):

    def setUp(self):
        # configure mocks for each stage
        pass

    @patch('TaxDev.convert.parse_mmfs')
    @patch('TaxDev.convert.os.listdir', lambda x: [])
    @patch('TaxDev.convert.os.path.exists', lambda x: True)
    @patch('TaxDev.convert.os.remove', lambda x: None)
    def test_parse_mmfs_empty_source(self, parse_mmfs_mock):
        convert_mmf_forms_to_py()
        parse_mmfs_mock.assert_not_called()

    @patch('TaxDev.convert.list_source_mmf', lambda: [])
    @patch('TaxDev.convert.subprocess.run')
    @patch('TaxDev.convert.MathExtractor.funcs_to_file')
    def test_empty_sub_1(self, mock_funcs_to_file, mock_subproc):
        process_subs_stage1()
        mock_funcs_to_file.assert_not_called()
        mock_subproc.assert_called_once()

    @patch('TaxDev.convert.os.listdir', lambda x: [])
    @patch('TaxDev.convert.replace_tool_func_calls')
    @patch('TaxDev.convert.replace_form_references')
    @patch('TaxDev.convert.replace_return_value')
    def test_empty_sub_2(self, mock_replace_tool_func, mock_form_ref, mock_replace_return):
        process_subs_stage2()
        mock_replace_tool_func.assert_not_called()
        mock_form_ref.assert_not_called()
        mock_replace_return.assert_not_called()

    @patch('TaxDev.convert.os.listdir', lambda x: [])
    @patch('TaxDev.convert.open')
    def test_embed_subs(self, mock_open):
        embed_subs()
        mock_open.assert_not_called()
