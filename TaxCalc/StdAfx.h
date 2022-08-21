// stdafx.h : include file for standard system include files,
// or project specific include files that are used frequently,
// but are changed infrequently

// standard include file for calculations
#if defined(CALCDLL) /*|| defined(STATECALCDLL)*/
#include "CalcPortableTypes.h"
#else
#define NOMINMAX
#include <Windows.h>
#include <intsafe.h>
#endif

#include <stdio.h>
#include <math.h>
#include "CALCDEFS.H"

// common standard headers
#include <string>
#include <vector>
#include <set>
#include <map>
#include <memory>
#include <sstream>
#include <functional>

// common third-party library headers
#include <rapidjson/rapidjson.h>
#include <rapidjson/document.h>
#include <rapidjson/writer.h>

#include <tinyxml2.h>

// global project headers
#include "CALCINFO.H"
#include "prntdefs.h"
#include "icalcmgr.h"
#include "ICALCFRM.H"
#include "ICALCFLD.H"

#if defined(CALCDLL) || defined(STATECALCDLL)
#include "CALCMGR.H"
#include "CALCFORM.H"
#include "CALCFLD.H"
#include "CALCFUNC.H"
#include "CUSTFUNC.H"
#endif

#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wunused-parameter"
#pragma GCC diagnostic ignored "-Wparentheses"
#pragma GCC diagnostic ignored "-Wconversion"
#else
#pragma warning(disable: 4100) //disable "unreferenced paramater" warning
#pragma warning(disable: 4706) //disable "assignment within condition" warning
#pragma warning(disable: 4800) //disable "forcing value to bool" warning
#endif
