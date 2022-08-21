#ifndef CALCSTATICDATA_H
#define CALCSTATICDATA_H

#include "CalcStaticDataTypes.h"

extern CalcStaticData g_calcStaticData;

WORD GetCachedFormID(const char *formName);
WORD GetCachedFieldID(WORD formID, const char *fieldName, WORD index);
extern "C" CALC_EXPORT bool InitStaticData(const char *filename);

std::string GetFormFieldMapJson();
std::string GetCustomFieldMapJson();

#endif
