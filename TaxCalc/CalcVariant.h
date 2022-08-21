#ifndef CALCVARIANT_H
#define CALCVARIANT_H

#include <string>
#include <stdexcept>
#include "CALCDEFS.H"
#include "Taxstr.h"
#include "TAXDATE.H"

// variant type that encapsulates all the possible parameter types for Custom functions in the math
class CalcVariant
{
public:
    CalcVariant();
    CalcVariant(LONG value);
    CalcVariant(TAXCURRENCY value);
    CalcVariant(DOUBLE value);
    CalcVariant(CTaxString value);
    CalcVariant(CTaxDate value);

#ifndef CALCDLL
    CalcVariant(BOOL value);
#endif

    operator LONG() const;
    operator TAXCURRENCY() const;
    operator DOUBLE() const;
    operator CTaxString() const;
    operator CTaxDate() const;

#ifndef CALCDLL
    operator BOOL() const;
#endif

    enum class Type
    {
        None,
        Long,
        Currency,
        Double,
        String,
        Date,
        Bool
    };

    Type type() const;

    static void CheckParameters(int numActual, CalcVariant *params, int numExpected);

private:
    template<typename T>
    T castValue() const
    {
        switch (m_type)
        {
        case Type::Long:
            return castValue<T>(m_long);
            break;
        case Type::Currency:
            return castValue<T>(m_currency);
            break;
        case Type::Double:
            return castValue<T>(m_double);
            break;
        case Type::String:
            return castValue<T>(m_string);
            break;
        case Type::Date:
            return castValue<T>(m_date);
            break;
        case Type::Bool:
            return castValue<T>(m_bool);
            break;
        default:
            throw std::runtime_error("Trying to cast value from an uninitialized CalcVariant");
        }
    }

    template<typename T, typename S>
    typename std::enable_if<std::is_convertible<S, T>::value, T>::type
        castValue(S value) const
    {
#ifdef __GNUC__
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
        return static_cast<T>(value);
#pragma GCC diagnostic pop
#else
#pragma warning(push)
#pragma warning(disable:4244)
        return static_cast<T>(value);
#pragma warning(pop)
#endif
    }

    template<typename T, typename S>
    typename std::enable_if<std::negation<std::is_convertible<S, T>>::value, T>::type
        castValue(S value) const
    {
        throw std::runtime_error("CalcVariant: Casting to the requested type is not supported");
    }

    Type m_type;

    LONG m_long = 0;
    TAXCURRENCY m_currency;
    DOUBLE m_double = 0;
    CTaxString m_string;
    CTaxDate m_date;
    BOOL m_bool = false;
};

#endif
