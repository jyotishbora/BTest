#ifndef CALCSERIALIZEUTILS_H
#define CALCSERIALIZEUTILS_H

#include "rapidjson/document.h"
#include "rapidjson/writer.h"

#include <type_traits>

struct JsonFormKey
{
    JsonFormKey(const std::string& str);
    JsonFormKey(const std::string& formName, WORD copyId);

    std::string formName() const;
    WORD copyId() const;
    std::string str() const;

    bool operator<(const JsonFormKey& other) const;
    bool operator==(const JsonFormKey& other) const;

private:
    std::string m_name;
    WORD m_copyId = 0;
};

struct JsonFieldKey
{
    JsonFieldKey(const std::string& str);
    JsonFieldKey(const std::string& fieldName, int index);

    std::string fieldName() const;
    int index() const;
    std::string str() const;

    bool operator<(const JsonFieldKey& other) const;
    bool operator==(const JsonFieldKey& other) const;

private:
    std::string m_name;
    int m_index = 0;
};

#endif
