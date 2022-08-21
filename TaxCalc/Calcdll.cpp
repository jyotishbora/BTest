// calculation DLL implementation

#include "StdAfx.h"
#include "Calcmgr.h"

#if defined(STATECALCDLL) || defined(PRINTDLL)
extern HINSTANCE m_hinst;

extern "C"
BOOL WINAPI DllMain(HINSTANCE hinstDLL, DWORD dwReason, LPVOID lpReserved)
{
    switch (dwReason)
    {
        case DLL_PROCESS_ATTACH:
            // Initialize once for each new process.
            // Return FALSE to fail DLL load.
            m_hinst = hinstDLL;
            break;

        case DLL_THREAD_ATTACH:
            // Do thread-specific initialization.
            break;

        case DLL_THREAD_DETACH:
            // Do thread-specific cleanup.
            break;

        case DLL_PROCESS_DETACH:
            // Perform any necessary cleanup.
            break;
    }

    return TRUE;
}
#endif
