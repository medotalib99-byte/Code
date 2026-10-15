import base64
import os
import textwrap
import datetime
import numpy as np
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

# ==============================================================================
# 1. STREAMLIT PAGE CONFIGURATION
# ==============================================================================
st.set_page_config(
    page_title="Mohamed Talib, MSc | Public Health Informatics Consultant",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ==============================================================================
# 2. HELPER FUNCTIONS & SAFE HTML RENDERING
# ==============================================================================
def render_html(html_str):
    """
    Renders HTML safely without Python-Markdown interpreting leading indentation
    or empty lines as raw code blocks. Strips common leading whitespace.
    """
    st.markdown(textwrap.dedent(html_str).strip(), unsafe_allow_html=True)


# ==============================================================================
# 3. CIVICA-INSPIRED & CORPORATE CSS STYLING
# ==============================================================================
CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    color: #1F2937;
}

/* Subtle background tone */
.stApp {
    background-color: #FAFCFB;
}

/* Brand Header Bar */
.brand-header {
    background: #ffffff;
    padding: 16px 26px;
    border-bottom: 2px solid #E5E7EB;
    border-left: 6px solid #004D34;
    margin-bottom: 24px;
    border-radius: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 4px 14px rgba(0, 77, 52, 0.04);
}

.brand-logo {
    background: linear-gradient(135deg, #004D34 0%, #002B1D 100%);
    color: #ffffff !important;
    padding: 9px 20px;
    font-weight: 800;
    font-size: 1.35rem;
    letter-spacing: 1.5px;
    border-radius: 6px;
    display: inline-block;
}

.brand-tagline {
    color: #004D34;
    font-weight: 600;
    font-size: 0.98rem;
    display: flex;
    align-items: center;
    gap: 10px;
}

.status-badge {
    background-color: #E8F8F0;
    color: #007A53;
    font-size: 0.78rem;
    font-weight: 700;
    padding: 4px 12px;
    border-radius: 20px;
    border: 1px solid #70E000;
    display: inline-block;
}

/* Hero Banner Overlay Card */
.hero-card {
    background: linear-gradient(135deg, #004D34 0%, #002B1D 100%);
    color: #ffffff;
    padding: 38px 40px;
    border-radius: 14px;
    box-shadow: 0 16px 32px rgba(0, 77, 52, 0.16);
    margin-bottom: 25px;
    border-right: 6px solid #70E000;
}

.hero-pill {
    background: rgba(112, 224, 0, 0.2);
    border: 1px solid #70E000;
    color: #70E000;
    padding: 5px 14px;
    border-radius: 30px;
    font-size: 0.82rem;
    font-weight: 700;
    letter-spacing: 0.5px;
    display: inline-block;
    margin-bottom: 14px;
    text-transform: uppercase;
}

.hero-title {
    font-size: 2.35rem;
    font-weight: 800;
    color: #ffffff;
    line-height: 1.22;
    margin-bottom: 14px;
}

.hero-subtitle {
    font-size: 1.1rem;
    color: #D1FAE5;
    line-height: 1.6;
    margin-bottom: 22px;
    font-weight: 400;
}

.accent-btn {
    background-color: #70E000;
    color: #004D34 !important;
    padding: 11px 24px;
    font-weight: 700;
    font-size: 0.95rem;
    border-radius: 6px;
    display: inline-block;
    text-decoration: none;
    box-shadow: 0 4px 12px rgba(112, 224, 0, 0.35);
    transition: all 0.2s ease-in-out;
}

.accent-btn:hover {
    background-color: #5ec400;
    transform: translateY(-1px);
}

/* Feature & Service Cards */
.civica-card {
    background-color: #ffffff;
    border-top: 5px solid #004D34;
    padding: 24px 22px;
    border-radius: 10px;
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.04);
    border-left: 1px solid #E5E7EB;
    border-right: 1px solid #E5E7EB;
    border-bottom: 1px solid #E5E7EB;
    margin-bottom: 20px;
    height: calc(100% - 20px);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.civica-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 24px rgba(0, 77, 52, 0.08);
}

.civica-card h4 {
    color: #004D34;
    font-weight: 700;
    font-size: 1.18rem;
    margin-bottom: 12px;
}

.civica-card ul {
    padding-left: 20px;
    margin-bottom: 0;
}

.civica-card li {
    margin-bottom: 8px;
    color: #374151;
    font-size: 0.95rem;
    line-height: 1.5;
}

/* Stat Metric Counter Card */
.stat-card {
    background: #ffffff;
    border: 1px solid #E5E7EB;
    border-bottom: 4px solid #70E000;
    border-radius: 10px;
    padding: 18px 20px;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.03);
    margin-bottom: 16px;
}

.stat-number {
    font-size: 2rem;
    font-weight: 800;
    color: #004D34;
    margin-bottom: 4px;
}

.stat-label {
    font-size: 0.85rem;
    color: #4B5563;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

/* Testimonial Banner */
.testimonial-box {
    background-color: #F4F6F5;
    border-left: 5px solid #70E000;
    padding: 22px 24px;
    border-radius: 8px;
    margin-bottom: 18px;
    box-shadow: 0 3px 10px rgba(0, 0, 0, 0.02);
}

.testimonial-rating {
    color: #F59E0B;
    font-size: 1.05rem
