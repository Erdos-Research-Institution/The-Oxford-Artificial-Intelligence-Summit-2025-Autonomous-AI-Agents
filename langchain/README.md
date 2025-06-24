## Virtual Environment
This project uses a global virtual environment (`tutor_venv`) shared by all topics.

- The automation scripts (`setup_and_run.bat` and `setup_and_run.sh`) will:
  - Check if `tutor_venv` exists at the root of the repository.
  - If not, create it and activate it.
  - Install dependencies from `requirements.txt`.
  - Launch the FastAPI backend and Streamlit app.

You do not need to manually create or activate the virtual environment—just run the setup script for your OS!

---

# Langchain AI Agent: Streamlit + FastAPI Tutorial

This folder contains a beginner-friendly tutorial and an interactive Streamlit app covering:
- Langchain basics
- Langchain Memory, Tool usage
- RAG (Retrieval Augmented Generation)
- FastAPI backend (connect with Streamlit frontend)

## Getting Started Locally

1. **Open a terminal in this folder (`langchain/streamlit_app`).**
2. **Run the automation script:**
   - On Windows: Double-click `setup_and_run.bat` or run it in the terminal.
   - On Mac/Linux: Run `bash setup_and_run.sh` in the terminal.

These scripts will set up the global virtual environment, install dependencies, launch the FastAPI backend, and start the Streamlit app automatically.

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
3. Start the FastAPI backend:
   ```
   uvicorn api:app --reload
   ```
4. In a new terminal, run the Streamlit app:
   ```
   streamlit run app.py
   ```

## Deploying on Streamlit Community Cloud
- Note: Streamlit Community Cloud does not support running FastAPI and Streamlit together. For full-stack deployment, use a cloud provider like Azure, AWS, or Heroku.

---

Enjoy building AI agents with Langchain!
