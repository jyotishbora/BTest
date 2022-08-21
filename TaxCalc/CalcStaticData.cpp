#include "StdAfx.h"
#include "CalcStaticData.h"
#include "CALCINFO.H"
#include "xstring.h"

#include <fstream>
#include <unordered_map>
#include <string>
#include <map>
#include <mutex>

#include <rapidjson/rapidjson.h>
#include <rapidjson/writer.h>

std::mutex g_mutexInitStaticData;
bool g_didInitCalcStaticData = false;
CalcStaticData g_calcStaticData;

std::unordered_map<std::string, WORD> g_cachedFormIDs;

void InitCachedFormIDs()
{
    WORD nForms = static_cast<WORD>(g_calcStaticData.forms.size());
    g_cachedFormIDs.reserve(nForms);

    for (WORD formID = 1; formID <= nForms; formID++)
    {
        Tax::xstring upperName = g_calcStaticData.forms[formID - 1].name;
        upperName.MakeUpper();

        g_cachedFormIDs.insert(std::make_pair(upperName, formID));
    }
}

WORD GetCachedFormID(const char *formName)
{
    Tax::xstring upperName = formName;
    upperName.MakeUpper();

    auto find = g_cachedFormIDs.find(upperName);
    if (find != g_cachedFormIDs.end())
    {
        return find->second;
    }

    return 0;
}

struct CachedFieldIDInfo
{
    WORD beginID;
    WORD endID;
};

std::vector<std::unordered_map<std::string, CachedFieldIDInfo>> g_cachedFieldIDs;

void InitCachedFieldIDs()
{
    WORD nForms = static_cast<WORD>(g_calcStaticData.forms.size());
    g_cachedFieldIDs.resize(nForms);

    for (WORD formID = 1; formID <= nForms; formID++)
    {
        auto& formData = g_calcStaticData.forms[formID - 1];
        auto& formCachedFieldIDs = g_cachedFieldIDs[formID - 1];

        WORD nFields = static_cast<WORD>(formData.fields.size());
        formCachedFieldIDs.reserve(nFields);

        for (WORD fieldID = 1; fieldID <= nFields; fieldID++)
        {
            Tax::xstring upperName = formData.fields[fieldID - 1].name;
            upperName.MakeUpper();

            auto findField = formCachedFieldIDs.find(upperName);
            if (findField == formCachedFieldIDs.end())
            {
                CachedFieldIDInfo toAdd;
                toAdd.beginID = fieldID;
                toAdd.endID = fieldID + 1;

                formCachedFieldIDs.insert(std::make_pair(upperName, toAdd));
            }
            else
            {
                if (findField->second.endID <= fieldID)
                {
                    findField->second.endID = fieldID + 1;
                }
            }
        }
    }
}

WORD GetCachedFieldID(WORD formID, const char *fieldName, WORD index)
{
    if (formID > 0 && formID <= g_cachedFieldIDs.size())
    {
        Tax::xstring upperName = fieldName;
        upperName.MakeUpper();

        auto find = g_cachedFieldIDs[formID - 1].find(upperName);
        if (find != g_cachedFieldIDs[formID - 1].end())
        {
            WORD result = find->second.beginID + index;

            if (result < find->second.endID)
            {
                return result;
            }
        }
    }

    return 0;
}

extern "C" CALC_EXPORT bool InitStaticData(const char *filename)
{
    std::lock_guard<std::mutex> lock(g_mutexInitStaticData);

    if (!g_didInitCalcStaticData)
    {
        std::ifstream in(filename, std::ios_base::in | std::ios_base::binary);
        if (in.is_open())
        {
            in.seekg(0, std::ios_base::end);
            auto fileSize = in.tellg();
            in.seekg(0, std::ios_base::beg);

            XStream::xstream xs(static_cast<unsigned int>(fileSize));
            in.read(xs.data(), xs.size());

            xs >> g_calcStaticData;

            if (g_calcStaticData.forms.size() != FORM_TOTALFORMS)
            {
                g_calcStaticData = CalcStaticData();
                return false;
            }
        }
        else
        {
            return false;
        }

        InitCachedFormIDs();
        InitCachedFieldIDs();
    }

    g_didInitCalcStaticData = true;
    return true;
}

std::string GetFormFieldMapJson()
{
    rapidjson::StringBuffer buffer;
    buffer.Clear();
    rapidjson::Writer<rapidjson::StringBuffer> writer(buffer);

    writer.StartObject();

    for (const auto& form : g_calcStaticData.forms)
    {
        writer.Key(form.name.c_str(), static_cast<rapidjson::SizeType>(form.name.length()), true);

        writer.StartObject();

        writer.Key("MaxCopies");
        writer.Uint(form.maxCopies);

        writer.Key("TotalFields");
        writer.Uint(form.totalFields);

        writer.Key("Flags");
        writer.Uint(form.flags);

        writer.Key("Fields");
        writer.StartObject();

        struct JsonFieldData
        {
            WORD type;
            int arraySize;
        };

        std::map<std::string, JsonFieldData> jsonFieldData;

        for (const auto& field : form.fields)
        {
            auto findField = jsonFieldData.find(field.name);
            if (findField == jsonFieldData.end())
            {
                JsonFieldData toInsert;
                toInsert.type = field.type;
                toInsert.arraySize = 1;

                jsonFieldData.insert(std::make_pair(field.name, toInsert));
            }
            else
            {
                findField->second.arraySize++;
            }
        }

        for (const auto& data : jsonFieldData)
        {
            writer.Key(data.first.c_str(), static_cast<rapidjson::SizeType>(data.first.length()), true);

            writer.StartObject();

            writer.Key("Type");
            writer.Int(data.second.type);

            if (data.second.arraySize != 1)
            {
                writer.Key("ArraySize");
                writer.Int(data.second.arraySize);
            }

            writer.EndObject();
        }

        writer.EndObject();

        writer.EndObject();
    }

    writer.EndObject();

    return buffer.GetString();
}

std::string GetCustomFieldMapJson()
{
    rapidjson::StringBuffer buffer;
    buffer.Clear();
    rapidjson::Writer<rapidjson::StringBuffer> writer(buffer);

    writer.StartObject();

    for (const auto& custom : g_calcStaticData.customFields)
    {
        writer.Key(custom.name.c_str());

        writer.StartObject();

        writer.Key("Form");
        writer.String(g_calcStaticData.forms[custom.formID - 1].name.c_str());

        writer.Key("Field");
        writer.String(g_calcStaticData.forms[custom.formID - 1].fields[custom.fieldID - 1].name.c_str());

        writer.EndObject();
    }

    writer.EndObject();

    return buffer.GetString();
}
