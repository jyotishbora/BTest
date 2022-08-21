#include "StdAfx.h"
#include "CalcVariant.h"

CalcVariant::CalcVariant()
    : m_type(Type::None)
{
}

CalcVariant::CalcVariant(LONG value)
    : m_type(Type::Long),
    m_long(value)
{
}

CalcVariant::CalcVariant(TAXCURRENCY value)
    : m_type(Type::Currency),
    m_currency(value)
{
}

CalcVariant::CalcVariant(DOUBLE value)
    : m_type(Type::Double),
    m_double(value)
{
}

CalcVariant::CalcVariant(CTaxString value)
    : m_type(Type::String),
    m_string(value)
{
}

CalcVariant::CalcVariant(CTaxDate value)
    : m_type(Type::Date),
    m_date(value)
{
}

#ifndef CALCDLL
CalcVariant::CalcVariant(BOOL value)
    : m_type(Type::Bool),
    m_bool(value)
{
}
#endif

CalcVariant::operator LONG() const
{
    return castValue<LONG>();
}

CalcVariant::operator TAXCURRENCY() const
{
    return castValue<TAXCURRENCY>();
}

CalcVariant::operator DOUBLE() const
{
    return castValue<DOUBLE>();
}

CalcVariant::operator CTaxString() const
{
    return castValue<CTaxString>();
}

CalcVariant::operator CTaxDate() const
{
    return castValue<CTaxDate>();
}

#ifndef CALCDLL
CalcVariant::operator BOOL() const
{
    return castValue<BOOL>();
}
#endif

CalcVariant::Type CalcVariant::type() const
{
    return m_type;
}

void CalcVariant::CheckParameters(int numActual, CalcVariant *params, int numExpected)
{
    if (numActual != numExpected)
    {
        throw std::invalid_argument("Incorrect number of parameters");
    }
}
