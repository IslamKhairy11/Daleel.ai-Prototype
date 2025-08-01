# utils/ui_utils.py (Final, Robust Version)
import streamlit as st

def display_logo():
    """Displays the Daleel.ai logo using reliable online URLs, switching for themes."""
    
    # --- IMPORTANT: Replace these with YOUR actual raw GitHub URLs ---
    LOGO_BLACK_URL = "https://github.com/IslamKhairy11/Daleel.ai-Prototype/blob/main/assets/daleel-logo-black.png?raw=true"
    LOGO_WHITE_URL = "https://github.com/IslamKhairy11/Daleel.ai-Prototype/blob/main/assets/daleel-logo-white.png?raw=true"

    # CSS to hide/show the correct logo based on the theme
    logo_html = f"""
        <style>
            /* Hide the dark-theme logo by default */
            .logo-dark {{ display: none; }}
            .logo-light {{ display: block; }}

            /* Show the dark-theme logo and hide the light one when dark theme is active */
            [data-theme="dark"] .logo-dark {{ display: block; }}
            [data-theme="dark"] .logo-light {{ display: none; }}
        </style>

        <div style="display: flex; justify-content: center;">
            <a href="/" target="_self">
                <img src="{LOGO_WHITE_URL}" class="logo-dark" style="width: 200px;">
                <img src="{LOGO_BLACK_URL}" class="logo-light" style="width: 200px;">
            </a>
        </div>
    """
    st.markdown(logo_html, unsafe_allow_html=True)