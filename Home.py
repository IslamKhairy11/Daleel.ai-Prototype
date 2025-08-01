# Home.py (Simplified)
import streamlit as st
from utils.auth_utils import init_authenticator, register_user, login_user
from utils.data_manager import setup_database, get_user_credentials

# Ensures the DB and table exist on first run
setup_database()

st.set_page_config(page_title="Daleel.ai", layout="centered")

# Initialize authenticator for session/cookie management
if "authenticator" not in st.session_state:
    st.session_state.authenticator = init_authenticator()

authenticator = st.session_state.authenticator

# --- Check for existing login session ---
if st.session_state.get("authentication_status"):
    # Redirect logic
    config = get_user_credentials()
    user_email = config['usernames'][st.session_state['username']]['email']
    domain = user_email.split('@')[1]
    banned_domains = ['gmail.com', 'outlook.com', 'yahoo.com', 'icloud.com', 'hotmail.com']
    
    if domain not in banned_domains:
        st.session_state['user_type'] = 'employer'
        st.switch_page("pages/3_Employer_Dashboard.py")
    else:
        st.session_state['user_type'] = 'talent'
        st.switch_page("pages/2_Talent_Dashboard.py")
    st.stop()

# --- If not logged in, display login/signup tabs ---
st.title("Welcome to Daleel.ai")
try:
    st.image("daleel-logo-black.png", width=200)
except Exception:
    st.image("https://i.imgur.com/gL12iV4.png", width=200) # Fallback logo
st.header("Beyond Resumes, Into the Future.")

tab1, tab2 = st.tabs(["Login", "Sign Up"])

with tab1:
    # ... (rest of the login code is exactly the same)
    st.subheader("Login to Your Account")
    login_username = st.text_input("Username", key="login_username")
    login_password = st.text_input("Password", type="password", key="login_password")

    if st.button("Login", type="primary", use_container_width=True):
        auth_status, user_name, username = login_user(login_username, login_password)
        
        if auth_status:
            st.session_state["authentication_status"] = True
            st.session_state["name"] = user_name
            st.session_state["username"] = username
            st.rerun()
        else:
            st.error('Username/password is incorrect or fields are empty.')

with tab2:
    # ... (rest of the registration code is exactly the same)
    st.subheader("Create New Account")
    with st.form("registration_form", clear_on_submit=False):
        reg_email = st.text_input("Email")
        reg_username = st.text_input("Username")
        reg_name = st.text_input("Full Name")
        reg_password = st.text_input("Password", type="password")
        reg_confirm_password = st.text_input("Confirm Password", type="password")
        reg_user_type = st.radio("I am a:", ("Talent (Job Seeker)", "Employer"))

        submitted = st.form_submit_button("Register")
        if submitted:
            message = register_user(
                reg_email, reg_username, reg_name, 
                reg_password, reg_confirm_password, reg_user_type
            )
            if "successful" in message:
                st.success(message)
            else:
                st.error(message)