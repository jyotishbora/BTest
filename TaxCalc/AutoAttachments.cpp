#include "stdafx.h"
#include "AutoAttachments.h"

#include <map>
#include <string>

#include "icalcmgr.h"
#include "ICALCFLD.H"

bool AutoAttachmentDesc::writeJson(rapidjson::Writer<rapidjson::StringBuffer>& out) const
{
    out.StartObject();

    out.Key("Name");
    out.String(name);

    out.Key("Type");
    out.String(type);

    out.Key("Module");
    out.String(module);

    out.Key("Params");

    out.StartObject();

    for (const auto& param : params)
    {
        out.Key(param.first);
        out.String(param.second);
    }

    out.EndObject();

    out.EndObject();

    return true;
}

bool isExtension(EfReturnType returnType)
{
    return ((returnType == efExtension) ||
        (returnType == efSpecialExtension) ||
        (returnType == efSpecialTaxpayerExt) ||
        (returnType == efSpecialSpouseExt) ||
        (returnType == efExtension2));
}

bool isAmended(EfReturnType returnType)
{
    return ((returnType == efAmendedReturn) ||
        (returnType == efAmendedReturn2) || 
        (returnType == efSpecialAmended) ||
        (returnType == efSpecialAmended2) ||
        (returnType == efSpecialAmended3) ||
        (returnType == efSpecialAmended4));
}

bool isSpecial(EfReturnType returnType)
{
    return ((returnType == efSpecialReturn) ||
        (returnType == efSpecialReturn2) ||
        (returnType == efSpecialReturn3) ||
        (returnType == efSpecialExtension) ||
        (returnType == efSpecialAmended) ||
        (returnType == efSpecialEstimatedTax1) ||
        (returnType == efSpecialEstimatedTax2) ||
        (returnType == efSpecialEstimatedTax3) ||
        (returnType == efSpecialEstimatedTax4) ||
        (returnType == efSpecialTaxpayer) ||
        (returnType == efSpecialSpouse) ||
        (returnType == efFilingFee) ||
        (returnType == efSpecialTaxpayerExt) ||
        (returnType == efSpecialSpouseExt) ||
        (returnType == efSpecialReturn4) ||
        (returnType == efSpecialAmended2) ||
        (returnType == efSpecialAmended3) ||
        (returnType == efSpecialAmended4));
}

Tax::xstring FixModuleName(const Tax::xstring& module)
{
    Tax::xstring result = module;
    result.MakeUpper();

    if (result == "FED")
    {
        result = "FEDERAL";
    }

    return result;
}

bool GetPdfAutoAttachments(ITaxFormManager* formMgr, Tax::xstring& csAttachments, EfReturnType type)
{
    csAttachments.clear();

    if (formMgr)
    {
        if (!isExtension(type))
        {
            std::string key = "PDFAutoAttachments";

            if (isSpecial(type))
            {
                key += std::to_string(type);
            }

            auto pField = formMgr->GetCustomField(key.c_str());

            if (pField)
            {
                std::vector<char> buf;
                buf.resize(pField->GetStringLength() + 1);
                pField->GetString(buf.data(), buf.size());

                csAttachments = buf.data();
            }
            else
            {
                csAttachments.clear();
            }
        }
    }
    else
    {
        return false;
    }

    return true;
}

std::vector<AutoAttachmentDesc> ParseAutoAttachments(ITaxFormManager *formMgr, EfReturnType type)
{
    std::vector<AutoAttachmentDesc> result;

    char moduleName[64] = {};
    formMgr->GetModuleName(moduleName);

    Tax::xstring csAttachments;
    if (GetPdfAutoAttachments(formMgr, csAttachments, type))
    {
        if (!csAttachments.IsEmpty())
        {
            int nIndex = 1;

            while (true)
            {
                Tax::xstring csAttachmentInfo = csAttachments.GetParam(nIndex, '|');

                if (csAttachmentInfo.IsEmpty())
                {
                    break;
                }

                nIndex++;

                Tax::xstring csAttachmentName = csAttachmentInfo.GetParam(1, '(');
                Tax::xstring csTemp = csAttachmentInfo.GetParam(2, '(');

                Tax::xstring csFormInfo = csTemp.GetParam(1, ',');
                Tax::xstring csForm = csFormInfo.GetParam(1, '.');
                Tax::xstring csField = csFormInfo.GetParam(2, '.');

                Tax::xstring csCopyID = csTemp.GetParam(2, ',');
                csCopyID.Replace(")", "");

                AutoAttachmentDesc toAdd;
                toAdd.name = csAttachmentName;

                if (csForm.CompareNoCase("PrintReturn") == 0)
                {
                    toAdd.type = "Return";
                    toAdd.module = FixModuleName(csCopyID);
                }
                else if (csForm.CompareNoCase("PrintCustom") == 0)
                {
                    toAdd.type = "Custom";
                    toAdd.module = FixModuleName(moduleName);

                    toAdd.params["custom"] = csCopyID;
                }
                else
                {
                    if (csField.empty())
                    {
                        toAdd.type = "Form";
                    }
                    else
                    {
                        toAdd.type = "Details";
                    }

                    Tax::xstring formPrefix = csForm.Left(2);
                    if (formPrefix.CompareNoCase("US") == 0)
                    {
                        toAdd.module = FixModuleName("FED");
                    }
                    else
                    {
                        toAdd.module = FixModuleName(formPrefix);
                    }

                    toAdd.params["form"] = csForm;
                    toAdd.params["field"] = csField;
                    toAdd.params["copyid"] = csCopyID;
                }

                result.push_back(toAdd);
            }
        }
    }

    return result;
}
