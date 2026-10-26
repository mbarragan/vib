@echo off
setlocal

set "ROOT_DIR=%~dp0"
set "PYTHON_EXE=%ROOT_DIR%.venv\Scripts\python.exe"

if not exist "%PYTHON_EXE%" (
    set "PYTHON_EXE=python"
)

if "%~1"=="" (
    "%PYTHON_EXE%" -m mouse_jiggler.main --config "%ROOT_DIR%config.toml"
) else (
    "%PYTHON_EXE%" -m mouse_jiggler.main %*
)

