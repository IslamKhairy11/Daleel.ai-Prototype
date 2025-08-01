# utils/data_manager.py
import sqlite3
import streamlit as st

DB_PATH = 'daleel_users.db'

def get_db_connection():
    """Establishes a connection to the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def setup_database():
    """Creates the users table if it doesn't exist."""
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_user(username, name, email, hashed_password):
    """Adds a new user to the database. Returns True on success, False on failure."""
    try:
        conn = get_db_connection()
        conn.execute(
            'INSERT INTO users (username, name, email, password) VALUES (?, ?, ?, ?)',
            (username, name, email, hashed_password)
        )
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError: # This handles the 'UNIQUE' constraint violation for username
        return False
    except Exception as e:
        st.error(f"Database error: {e}")
        return False

def get_user_credentials():
    """Fetches all user credentials and formats them for the authenticator."""
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    
    credentials = {"usernames": {}}
    for user in users:
        user_dict = dict(user)
        credentials["usernames"][user_dict["username"]] = {
            "email": user_dict["email"],
            "name": user_dict["name"],
            "password": user_dict["password"]
        }
    return credentials