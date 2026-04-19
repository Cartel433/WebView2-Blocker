@echo off
title Pascal Tweaks — WebView2 Hard Blocker
color 0A
mode con: cols=60 lines=35

net session >nul 2>&1
if %errorLevel% neq 0 (
    powershell start-process "%~f0" -verb runas
    exit /b
)

:MENU
cls
color 0A
echo.
echo.
echo          ╔══════════════════════════════════════╗
echo          ║                                      ║
echo          ║      PASCAL TWEAKS PRESENTS          ║
echo          ║                                      ║
echo          ║     WebView2  HARD  BLOCKER          ║
echo          ║                                      ║
echo          ╚══════════════════════════════════════╝
echo.
echo          ┌──────────────────────────────────────┐
echo          │                                      │
echo          │   [1]  HARD DISABLE  (Gaming Mode)   │
echo          │                                      │
echo          │   [2]  RE-ENABLE     (Normal Mode)   │
echo          │                                      │
echo          │   [3]  KILL Running Processes        │
echo          │                                      │
echo          │   [4]  EXIT                          │
echo          │                                      │
echo          └──────────────────────────────────────┘
echo.
set /p "choice=                    Select [1-4]: "

if "%choice%"=="1" goto HARD_DISABLE
if "%choice%"=="2" goto ENABLE
if "%choice%"=="3" goto KILL
if "%choice%"=="4" exit
goto MENU

:HARD_DISABLE
cls
color 0C
echo.
echo.
echo          ╔══════════════════════════════════════╗
echo          ║                                      ║
echo          ║        APPLYING  HARD  BLOCK         ║
echo          ║                                      ║
echo          ╚══════════════════════════════════════╝
echo.

taskkill /f /im "msedgewebview2.exe" >nul 2>&1
echo             [+] Killed WebView2 processes

sc stop "MicrosoftEdgeElevationService" >nul 2>&1
sc config "MicrosoftEdgeElevationService" start= disabled >nul 2>&1
echo             [+] Service disabled

takeown /f "C:\Program Files (x86)\Microsoft\EdgeWebView\Application\*.*" /a >nul 2>&1
icacls "C:\Program Files (x86)\Microsoft\EdgeWebView\Application\*.*" /grant administrators:F >nul 2>&1

if exist "C:\Program Files (x86)\Microsoft\EdgeWebView\Application\msedgewebview2.exe" (
    ren "C:\Program Files (x86)\Microsoft\EdgeWebView\Application\msedgewebview2.exe" "msedgewebview2.exe.disabled" >nul 2>&1
    echo             [+] Executable renamed
)

copy nul "C:\Program Files (x86)\Microsoft\EdgeWebView\Application\msedgewebview2.exe" >nul 2>&1
attrib +r "C:\Program Files (x86)\Microsoft\EdgeWebView\Application\msedgewebview2.exe" >nul 2>&1
echo             [+] Block file created

reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\Appx" /v "AllowAllTrustedApps" /t REG_DWORD /d 0 /f >nul 2>&1
echo             [+] App restrictions applied

reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\msedgewebview2.exe" /v "Debugger" /t REG_SZ /d "cmd.exe" /f >nul 2>&1
echo             [+] IFEO block applied

echo.
echo          ┌──────────────────────────────────────┐
echo          │                                      │
echo          │      HARD BLOCK IS NOW ACTIVE        │
echo          │       WebView2 cannot run            │
echo          │                                      │
echo          │   Re-enable when done gaming!        │
echo          │                                      │
echo          └──────────────────────────────────────┘
echo.
pause
goto MENU

:ENABLE
cls
color 0B
echo.
echo.
echo          ╔══════════════════════════════════════╗
echo          ║                                      ║
echo          ║         RE-ENABLING WebView2         ║
echo          ║                                      ║
echo          ╚══════════════════════════════════════╝
echo.

reg delete "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\msedgewebview2.exe" /f >nul 2>&1
echo             [+] IFEO block removed

if exist "C:\Program Files (x86)\Microsoft\EdgeWebView\Application\msedgewebview2.exe.disabled" (
    attrib -r "C:\Program Files (x86)\Microsoft\EdgeWebView\Application\msedgewebview2.exe" >nul 2>&1
    del "C:\Program Files (x86)\Microsoft\EdgeWebView\Application\msedgewebview2.exe" >nul 2>&1
    ren "C:\Program Files (x86)\Microsoft\EdgeWebView\Application\msedgewebview2.exe.disabled" "msedgewebview2.exe" >nul 2>&1
    echo             [+] Executable restored
)

sc config "MicrosoftEdgeElevationService" start= manual >nul 2>&1
sc start "MicrosoftEdgeElevationService" >nul 2>&1
echo             [+] Service re-enabled

reg delete "HKLM\SOFTWARE\Policies\Microsoft\Windows\Appx" /v "AllowAllTrustedApps" /f >nul 2>&1
echo             [+] App restrictions removed

echo.
echo          ┌──────────────────────────────────────┐
echo          │                                      │
echo          │       WebView2 FULLY ENABLED         │
echo          │      Normal operation restored       │
echo          │                                      │
echo          └──────────────────────────────────────┘
echo.
pause
goto MENU

:KILL
cls
color 0E
echo.
echo.
echo          ╔══════════════════════════════════════╗
echo          ║                                      ║
echo          ║      KILLING WebView2 PROCESSES      ║
echo          ║                                      ║
echo          ╚══════════════════════════════════════╝
echo.

taskkill /f /im "msedgewebview2.exe" >nul 2>&1
echo             [+] msedgewebview2.exe terminated

taskkill /f /im "MicrosoftEdgeUpdate.exe" >nul 2>&1
echo             [+] MicrosoftEdgeUpdate.exe terminated

echo.
echo          ┌──────────────────────────────────────┐
echo          │                                      │
echo          │      All processes terminated        │
echo          │                                      │
echo          └──────────────────────────────────────┘
echo.
pause
goto MENU
