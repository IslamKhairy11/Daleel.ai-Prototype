# Home.py (Simplified)
import streamlit as st
from utils.data_manager import setup_database, get_user_credentials
from utils.ui_utils import display_logo

# Ensures the DB and table exist on first run
setup_database()

st.set_page_config(page_title="Daleel.ai", layout="centered")

# --- If not logged in, display login/signup tabs ---
st.title("Welcome to Daleel.ai")
display_logo()
st.header("Beyond Resumes, Into the Future.")
