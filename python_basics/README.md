## Virtual Environment
This project uses a global virtual environment (`tutor_venv`) shared by all topics.

- The automation scripts (`setup_and_run.bat` and `setup_and_run.sh`) will:
  - Check if `tutor_venv` exists at the root of the repository.
  - If not, create it and activate it.
  - Install dependencies from `requirements.txt`.
  - Launch the Streamlit app.

You do not need to manually create or activate the virtual environment—just run the setup script for your OS!

---

# Python Basics: Streamlit Tutorial

This folder contains a beginner-friendly tutorial and an interactive Streamlit app covering:
- Variables and Data Types
- Input and Output
- Control Flow
- Loops
- Functions
- Lists and Basic Operations

## Getting Started Locally

1. **Open a terminal in this folder (`python_basics/streamlit_app`).**
2. **Run the automation script:**
   - On Windows: Double-click `setup_and_run.bat` or run it in the terminal.
   - On Mac/Linux: Run `bash setup_and_run.sh` in the terminal.

These scripts will set up the global virtual environment, install dependencies, and launch the Streamlit app automatically.

## Manual Setup (Alternative)
1. Create and activate the virtual environment manually (optional, since scripts do this):
   ```
   python -m venv ../../tutor_venv
   # On Windows:
   ..\..\tutor_venv\Scripts\activate.bat
   # On Mac/Linux:
   source ../../tutor_venv/bin/activate
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the app:
   ```
   streamlit run app.py
   ```

## Deploying on Streamlit Community Cloud
1. Push your repo to GitHub.
2. Go to [Streamlit Community Cloud](https://streamlit.io/cloud).
3. Click "New app", connect your GitHub repo, and select the branch and `python_basics/streamlit_app/app.py` as the main file.
4. Click "Deploy". Streamlit Cloud will install dependencies from `requirements.txt` and launch your app.

---

Enjoy learning Python basics interactively!
