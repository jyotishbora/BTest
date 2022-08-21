#ifndef AUTOATTACHMENTS_H
#define AUTOATTACHMENTS_H

#include "CommonConst.h"
#include "iprntmgr.h"
#include "xstring.h"

#include <map>
#include <vector>

#include "rapidjson/document.h"
#include "rapidjson/writer.h"

struct AutoAttachmentDesc
{
    Tax::xstring name;
    Tax::xstring type;
    Tax::xstring module;

    std::map<Tax::xstring, Tax::xstring> params;

    bool writeJson(rapidjson::Writer<rapidjson::StringBuffer>& out) const;
};

std::vector<AutoAttachmentDesc> ParseAutoAttachments(ITaxFormManager *formMgr, EfReturnType type);

#endif
