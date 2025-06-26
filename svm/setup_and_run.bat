@echo off
REM This script sets up a global virtual environment and runs the Streamlit app for SVM
set VENV_DIR=..\tutor_venv
if not exist %VENV_DIR% (
    python -m venv %VENV_DIR%
)
call %VENV_DIR%\Scripts\activate.bat
pip install -r requirements.txt
streamlit run app.py
