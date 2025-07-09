@REM @echo off
setlocal enabledelayedexpansion

@REM Set the path where mise will be installed
if defined MISE_INSTALL_PATH (
    set "MISE_PATH=%MISE_INSTALL_PATH%"
) else (
    set "MISE_PATH=%USERPROFILE%\.local\bin\mise.exe"
)

@REM Install mise if not already available
if not exist "%MISE_PATH%" call :try_install_with_winget
if not exist "%MISE_PATH%" call :try_install_with_chocolatey
if not exist "%MISE_PATH%" call :try_install_with_scoop
if not exist "%MISE_PATH%" (
    echo "Failed to install Mise" >&2
    exit /b 1
)


@REM Get the tool name (script name without extension)
set "TOOL_NAME=%~n0"

@REM Either run mise or the specified tool
if "%TOOL_NAME%"=="mise" (
    "%MISE_PATH%" %*
) else (
    "%MISE_PATH%" exec -- "%TOOL_NAME%" %*
)

exit /b %ERRORLEVEL%




    :try_install_with_winget
where winget >nul 2>&1 && winget install --silent --force jdxdev.mise
goto :EOF

    :try_install_with_chocolatey
where choco >nul 2>&1 && choco install --yes mise
goto :EOF

    :try_install_with_scoop
where scoop >nul 2>&1 && scoop install mise
goto :EOF
