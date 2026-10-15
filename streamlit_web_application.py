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
    
    /* Hero Banner Overlay Card */
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
        margin: 10px 0px;
    }
    
    .hero-title {
        font-size: 2.1rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 12px;
        line-height: 1.25;
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
        padding: 10px 20px;
        font-weight: 700;
        border-radius: 6px;
        display: inline-block;
    }
    
    /* Feature & Service Cards */
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
        sidebar_img_html = (
            '<div style="text-align: center; margin-bottom: 20px;">'
            f'<img src="data:image/jpeg;base64,{encoded_image}" '
            'style="width: 120px; height: 120px; border-radius: 50%; object-fit: cover; border: 3px solid #004D34; box-shadow: 0 4px 10px rgba(0,0,0,0.15);">'
            '<h3 style="margin: 10px 0 2px 0; font-size: 1.15rem; color: #004D34;">Mohamed Talib, MSc</h3>'
            '<p style="font-size: 0.85rem; color: #4B5563; margin: 0;">Public Health Informatics Fellow</p>'
            '<p style="font-size: 0.80rem; color: #6B7280; margin: 0;">Africa CDC / ZNPHI</p>'
            '</div>'
        )
        st.markdown(sidebar_img_html, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Upload 'Pic.jpg' to your project directory to display your profile picture here.")

    st.markdown("### Menu Navigation")
    section = st.radio(
        "Go to page:",
        [
            "Home & Showcase",
            "About Profile",
            "Services for Students (PhD/MSc)",
            "Services for Organizations (M&E)",
            "Interactive Data & Analytics",
            "Photo Profile & Media",
            "Client Reviews",
            "Contact & Consultations",
        ],
    )

    st.markdown("---")
    st.markdown("🔗 **Connect Directly:**")
    st.markdown("[LinkedIn Profile](https://www.linkedin.com/in/mohamed-talib-664331158)")
    st.markdown("📧 **Email:** medo.talib99@gmail.com")
    st.markdown("📱 **WhatsApp:** +249912559111")

# --- 1. HOME & SHOWCASE SECTION ---
if section == "Home & Showcase":
    col_hero_text, col_hero_img = st.columns([1.8, 1])

    with col_hero_text:
        hero_card_html = (
            '<div class="hero-overlay-card">'
            '<div class="hero-title">Empowering public health through digital data science.</div>'
            '<div class="hero-subtitle">'
            'Delivering advanced biostatistical modeling, digital disease surveillance, and strategic M&E frameworks across Africa CDC & ZNPHI deployments.'
            '</div>'
            '<div class="accent-btn">Public Health Informatics & AI</div>'
            '</div>'
        )
        st.markdown(hero_card_html, unsafe_allow_html=True)

    with col_hero_img:
        if encoded_image:
            hero_img_html = (
                '<div style="padding: 10px; text-align: center;">'
                f'<img src="data:image/jpeg;base64,{encoded_image}" '
                'style="width: 100%; max-width: 270px; border-radius: 12px; object-fit: cover; box-shadow: 0 10px 20px rgba(0,0,0,0.15); border: 4px solid #004D34;">'
                '</div>'
            )
            st.markdown(hero_img_html, unsafe_allow_html=True)
        st.info("📍 **Base:** Lusaka, Zambia / Africa CDC\n\n📧 **Direct Email:** medo.talib99@gmail.com\n\n📱 **Phone:** +249912559111")

    st.markdown("---")
    st.subheader("Core Capabilities & Solutions")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            """
            <div class="civica-card">
                <h4>Digital Health & Surveillance</h4>
                <p>Architecting digital disease surveillance workflows, DHIS2 implementations, epidemic response pipelines, and health data governance.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class="civica-card">
                <h4>Advanced Analytics & AI</h4>
                <p>Applying Python, R, XGBoost, and GIS spatial mapping to model epidemic risks, forecast outbreaks, and conduct biostatistical research.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            """
            <div class="civica-card">
                <h4>Humanitarian M&E & Grants</h4>
                <p>Designing donor-grade grant proposals, Theory of Change models, baseline evaluations, and interactive Power BI dashboards.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# --- 2. ABOUT PROFILE SECTION ---
elif section == "About Profile":
    st.header("Professional Profile & Background")
    st.write(
        "I serve as a **Public Health Informatics Fellow** with Africa CDC stationed at the **Zambia National Public Health Institute (ZNPHI)**. "
        "With over seven years of field epidemiology, research leadership, and data analytics experience, I bridge technical
