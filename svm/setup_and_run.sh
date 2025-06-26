#!/bin/bash
# This script sets up a global virtual environment and runs the Streamlit app for SVM
VENV_DIR="../tutor_venv"
if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv "$VENV_DIR"
fi
source "$VENV_DIR/bin/activate"
pip install -r requirements.txt
streamlit run app.py
