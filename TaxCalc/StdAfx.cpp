// stdafx.cpp : source file that includes just the standard includes
//  Tax.pch will be the pre-compiled header
//  stdafx.obj will contain the pre-compiled type information

#include "StdAfx.h"

#include "CommonConst.h"

// [ROLLOVER]
#pragma warning(push)
#pragma warning(disable:4130)
// since both strings here are string literals, assume that MSVC is optimizing and using the same pointer for both
static_assert(kAPP_YEAR == "2021", "kAPP_YEAR mismatch. Please ensure you are on the correct branch of TaxCodeShared.");
#pragma warning(pop)

// use this one if the above assert fails in a future version of MSVC
// constexpr char_traits is supported in VS2017 and newer only
// static_assert(std::char_traits<char>::compare(kAPP_YEAR, "2021") == 0, "kAPP_YEAR mismatch. Please ensure you are on the correct branch of TaxCodeShared.");
