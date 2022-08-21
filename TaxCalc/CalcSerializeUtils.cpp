#include "StdAfx.h"
#include "CalcSerializeUtils.h"

JsonFormKey::JsonFormKey(const std::string& str)
{
    auto findComma = str.find(',');
    if (findComma != std::string::npos)
    {
        m_name = str.substr(0, findComma);
        m_copyId = static_cast<WORD>(std::strtoul(str.c_str() + findComma + 1, nullptr, 10));
    }
    else
    {
        m_name = str;
        m_copyId = 1;
    }
}

JsonFormKey::JsonFormKey(const std::string& formName, WORD copyId)
    : m_name(formName),
    m_copyId(copyId)
{
}

std::string JsonFormKey::formName() const
{
    return m_name;
}

WORD JsonFormKey::copyId() const
{
    return m_copyId;
}

std::string JsonFormKey::str() const
{
    return m_name + "," + std::to_string(m_copyId);
}

bool JsonFormKey::operator<(const JsonFormKey& other) const
{
    if (m_name != other.m_name)
    {
        return m_name < other.m_name;
    }

    return m_copyId < other.m_copyId;
}

bool JsonFormKey::operator==(const JsonFormKey& other) const
{
    return (m_name == other.m_name) && (m_copyId == other.m_copyId);
}

JsonFieldKey::JsonFieldKey(const std::string& str)
{
    auto findComma = str.find(',');
    if (findComma != std::string::npos)
    {
        m_name = str.substr(0, findComma);
        m_index = std::strtol(str.c_str() + findComma + 1, nullptr, 10);
    }
    else
    {
        m_name = str;
        m_index = 0;
    }
}

JsonFieldKey::JsonFieldKey(const std::string& fieldName, int index)
    : m_name(fieldName),
    m_index(index)
{
}

std::string JsonFieldKey::fieldName() const
{
    return m_name;
}

int JsonFieldKey::index() const
{
    return m_index;
}

std::string JsonFieldKey::str() const
{
    return m_name + "," + std::to_string(m_index);
}

bool JsonFieldKey::operator<(const JsonFieldKey& other) const
{
    if (m_name != other.m_name)
    {
        return m_name < other.m_name;
    }

    return m_index < other.m_index;
}

bool JsonFieldKey::operator==(const JsonFieldKey& other) const
{
    return (m_name == other.m_name) && (m_index == other.m_index);
}
