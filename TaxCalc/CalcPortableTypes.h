#ifndef CALCPORTABLETYPES_H
#define CALCPORTABLETYPES_H

// compatibility shims for Linux builds of the calcdll

#include <cstdint>
#include <cstdarg>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cctype>

// Windows types
using BOOL = int;
using UCHAR = unsigned char;
using BYTE = uint8_t;
using WORD = uint16_t;
using DWORD = uint32_t;
using LONG = int; // this is "long" in the windows headers but it's supposed to be the same size on 32 and 64 bit builds
using DOUBLE = double;

using INT_PTR = intptr_t;

using HINSTANCE = void *;
using HWND = void *;

using LPSTR = char *;
using LPCSTR = const char *;
using LPWORD = WORD *;

constexpr BOOL FALSE = 0;
constexpr BOOL TRUE = 1;

// stdlib functions
#ifdef __GNUC__
inline int _stricmp(const char *a, const char *b)
{
    return strcasecmp(a, b);
}

inline int _strnicmp(const char *a, const char *b, size_t n)
{
    return strncasecmp(a, b, n);
}

inline int sprintf_s(char *s, const char *format, ...)
{
    va_list args;
    va_start(args, format);
    int result = vsprintf(s, format, args);
    va_end(args);
    return result;
}

inline int sprintf_s(char *s, size_t bytes, const char *format, ...)
{
    va_list args;
    va_start(args, format);
    int result = vsprintf(s, format, args);
    va_end(args);
    return result;
}

inline char *strcpy_s(char *dest, size_t bytes, const char *source)
{
    return strcpy(dest, source);
}

inline char *strcpy_s(char *dest, const char *source)
{
    return strcpy(dest, source);
}

inline char *strncpy_s(char *dest, size_t bytes, const char *source, size_t n)
{
    return strncpy(dest, source, n);
}

inline char *strncpy_s(char *dest, const char *source, size_t n)
{
    return strncpy(dest, source, n);
}

inline char *strcat_s(char *dest, size_t bytes, const char *source)
{
    return strcat(dest, source);
}

inline char *_strdup(const char *source)
{
    if (source)
    {
        return strdup(source);
    }
    else
    {
        return nullptr;
    }
}

inline char* _strlwr_s(char* s)
{
    for (char* tmp = s; *tmp; ++tmp)
    {
        *tmp = (char)tolower(*tmp);
    }

    return s;
}

inline char* _strupr_s(char* s)
{
    for (char* tmp = s; *tmp; ++tmp)
    {
        *tmp = (char)toupper(*tmp);
    }

    return s;
}

inline char* _strlwr_s(char* s, size_t n)
{
    return _strlwr_s(s);
}

inline char* _strupr_s(char* s, size_t n)
{
    return _strupr_s(s);
}
#endif

#endif
