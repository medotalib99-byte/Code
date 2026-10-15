import base64
import os
import numpy as np
import pandas as pd
import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Mohamed Talib, MSc | Public Health Informatics Consultant",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- CIVICA-INSPIRED CUSTOM CSS STYLING ---
st.markdown(
    """
    <style>
    /* Main Theme Palette */
    :root {
        --civica-dark-green: #004D34;
        --civica-bright-green: #70E000;
        --civica-light-bg: #F4F6F5;
        --civica-text-dark: #1F2937;
    }
    
    /* Top Header Bar Styling */
    .brand-header {
        background-color: #ffffff;
        padding: 15px 25px;
        border-bottom: 2px solid #E5E7EB;
        margin-bottom: 25px;
        border-radius: 8px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .brand-logo {
        background-color: #004D34;
        color: #ffffff;
        padding: 8px 18px;
        font-weight: 900;
        font-size: 1.6rem;
        letter-spacing: 2px;
        border-radius: 4px;
        display: inline-block;
    }
    
    /* Hero Banner Overlay Card (Civica Style) */
    .hero-container {
        background-color: #ffffff;
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid #E5E7EB;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        margin-bottom: 30px;
    }
    
    .hero-overlay-card {
        background-color: #004D34;
        color: #ffffff;
        padding: 35px;
        border-radius: 8px;
        margin: 20px;
    }
    
    .hero-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 12px;
        line-height: 1.2;
    }
    
    .hero-subtitle {
        font-size: 1.05rem;
        color: #D1FAE5;
        margin-bottom: 20px;
        line-height: 1.5;
    }
    
    .accent-btn {
        background-color: #70E000;
        color: #004D34;
        padding: 10px 24px;
        font-weight: 700;
        border-radius: 6px;
        text-decoration: none;
        display: inline-block;
    }
    
    /* Service Cards */
    .civica-card {
        background-color: #ffffff;
        border-top: 5px solid #004D34;
        padding: 24px;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.04);
        border-left: 1px solid #E5E7EB;
        border-right: 1px solid #E5E7EB;
        border-bottom: 1px solid #E5E7EB;
        margin-bottom: 20px;
        height: 100%;
    }
    
    .civica-card h4 {
        color: #004D34;
        font-weight: 700;
        margin-bottom: 10px;
    }

    /* Testimonial Banner */
    .testimonial-box {
        background-color: #F4F6F5;
        border-left: 5px solid #70E000;
        padding: 20px;
        border-radius: 6px;
        margin-bottom: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Helper function to encode local image safely
def get_base64_of_bin_file(bin_file):
    if os.path.isfile(bin_file):
        with open(bin_file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None


# Load local profile photo Pic.jpg
encoded_image = get_base64_of_bin_file("Pic.jpg")

# --- TOP BRAND HEADER BAR ---
st.markdown(
    """
    <div class="brand-header">
        <div class="brand-logo">MOHAMED TALIB</div>
        <div style="color: #004D34; font-weight: 600; font-size: 1.05rem;">
            Public Health Informatics & Research Consultancy
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    if encoded_image:
        st.markdown(
            f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <img src="data:image/jpeg;base64,{encoded_image}" 
                     style="width: 120px; height: 120px; border-radius: 50%; object-fit: cover; border: 3px solid #004D34; box-shadow: 0 4px 10px rgba(0,0,0,0.15);">
                <h3 style="margin: 10px 0 2px 0; font-size: 1.15rem; color: #004D34;">Mohamed Talib, MSc</h3>
                <p style="font-size: 0.85rem; color: #4B5563; margin: 0;">Public Health Informatics Fellow</p>
                <p style="font-size: 0.80rem; color: #6B7
