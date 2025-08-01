# utils/ui_utils.py
import streamlit as st
import base64

@st.cache_data
def get_img_as_base64(file):
    """Reads an image file and returns its base64 representation."""
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def display_logo():
    """Displays the Daleel.ai logo, dynamically switching between light and dark themes."""
    try:
        img_black = get_img_as_base64("daleel-logo-black.png")
        img_white = get_img_as_base64("daleel-logo-white.png")

        logo_html = f"""
            <style>
                /* Hide the dark logo by default (for light theme) */
                .logo-dark {{ display: none; }}
                .logo-light {{ display: block; }}

                /* Show the dark logo and hide the light one when dark theme is active */
                [data-theme="dark"] .logo-dark {{ display: block; }}
                [data-theme="dark"] .logo-light {{ display: none; }}
            </style>
            <picture>
                <source srcset="data:image/png;base64,{img_white}" media="(prefers-color-scheme: dark)" class="logo-dark">
                <img src="data:image/png;base64,{img_black}" class="logo-light" style="width: 200px; margin: 0 auto;">
            </picture>
        """
        st.markdown(logo_html, unsafe_allow_html=True)
    except FileNotFoundError:
        st.image("https://i.imgur.com/gL12iV4.png", width=200) # Fallback if local files are not found