# utils/auth_utils.py (Corrected and Final)
import streamlit_authenticator as stauth
import re
from passlib.context import CryptContext
from .data_manager import add_user, get_user_credentials

# --- Password Hashing Context (Defined once) ---
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    """Verifies a plain password against a hashed one."""
    return pwd_context.verify(plain_password, hashed_password)

def hash_password(password):
    """Hashes a password."""
    return pwd_context.hash(password)

def init_authenticator():
    """
    Initializes the authenticator object from the database.
    This should only be called ONCE per session.
    """
    credentials = get_user_credentials()
    return stauth.Authenticate(
        credentials,
        "daleel_cookie",
        "some_random_key_that_should_be_secret",
        30
    )

def login_user(username, password):
    """
    Handles the user login process.
    Fetches user data and verifies the password.
    Returns (status, name, username) tuple.
    """
    if not username or not password:
        return False, None, None # Incomplete form

    credentials = get_user_credentials()['usernames']
    
    if username.lower() in credentials:
        user_data = credentials[username.lower()]
        if verify_password(password, user_data['password']):
            # Success! Return the data needed to set the session state.
            return True, user_data['name'], username.lower()
    
    # If username not found or password incorrect
    return False, None, None

def register_user(email, username, name, password, confirm_password, user_type):
    """Handles new user registration, validation, and saving to the database."""
    # --- Validation Logic ---
    if password != confirm_password:
        return "Passwords do not match."
    if not all([email, username, name, password]):
        return "Please fill all fields."
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return "Invalid email address."
    if "Employer" in user_type and email.split('@')[1] in ['gmail.com', 'outlook.com', 'yahoo.com', 'icloud.com', 'hotmail.com']:
        return "Employer registration requires a corporate email address."

    # --- Hash password and add user to DB ---
    hashed_pass = hash_password(password)
    if add_user(username.lower(), name, email, hashed_pass):
        return "Registration successful! You can now log in."
    else:
        return "Username already exists. Please choose another."