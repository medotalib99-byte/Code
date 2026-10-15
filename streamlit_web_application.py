import base64
import os
import numpy as np
import pandas as pd
import streamlit as st

# --- PAGE CONFIGURATION & THEME ---
st.set_page_config(
    page_title="Mohamed Talib, MSc | Public Health Informatics & Research Consultant",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Professional CSS Styling
st.markdown(
    """
    <style>
    /* Primary Colors & Fonts */
    .main-title { font-size: 2.6rem; color: #0f4c81; font-weight: 800; margin-bottom: 0.2rem; }
    .sub-title { font-size: 1.25rem; color: #4a5568; font-weight: 600; margin-bottom: 1.5rem; }
    .badge { display: inline-block; background-color: #ebf8ff; color: #2b6cb0; padding: 4px 12px; border-radius: 20px; font-weight: 600; font-size: 0.85rem; margin-right: 8px; margin-bottom: 10px; border: 1px solid #bee3f8; }
    
    /* Executive Card Styling */
    .feature-card { background: #ffffff; padding: 24px; border-radius: 14px; border: 1px solid #e2e8f0; border-top: 4px solid #0f4c81; box-shadow: 0 4px 12px rgba(0,0,0,0.03); margin-bottom: 20px; }
    .stat-box { text-align: center; background: #f7fafc; padding: 16px; border-radius: 10px; border: 1px solid #edf2f7; }
    .stat-number { font-size: 1.8rem; font-weight: 700; color: #0f4c81; }
    .stat-label { font-size: 0.85rem; color: #718096; font-weight: 500; }
    
    /* Testimonial Box */
    .testimonial-card { background: #f8fafc; border-left: 4px solid #38a169; padding: 18px; border-radius: 8px; margin-bottom: 15px; }
    </style>
    """,
    unsafe_allow_html=True,
)


# Safe Image Encoding Helper
def get_base64_of_bin_file(bin_file):
    if os.path.isfile(bin_file):
        with open(bin_file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None


# Load Local Profile Image
encoded_image = get_base64_of_bin_file("Pic.jpg")

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    if encoded_image:
        st.markdown(
            f"""
            <div style="text-align: center; padding-top: 10px; margin-bottom: 15px;">
                <img src="data:image/jpeg;base64,{encoded_image}" 
                     style="width: 120px; height: 120px; border-radius: 50%; object-fit: cover; border: 3px solid #0f4c81; box-shadow: 0 4px 10px rgba(0,0,0,0.15);">
                <h3 style="margin: 10px 0 2px 0; font-size: 1.15rem; color: #1a202c;">Mohamed Talib, MSc</h3>
                <p style="font-size: 0.85rem; color: #4a5568; margin: 0;">Public Health Informatics Fellow</p>
                <p style="font-size: 0.80rem; color: #718096; margin: 0;">Africa CDC / ZNPHI</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.warning("⚠️ Upload 'Pic.jpg' to display your profile picture.")

    st.markdown("### Navigation")
    section = st.radio(
        "Select Page:",
        [
            "Home & Overview",
            "About & Leadership",
            "Research Services (Students)",
            "Institutional M&E & Proposals",
            "Interactive Analytics Lab",
            "Media & Photo Profile",
            "Client Testimonials",
            "Contact & Consultations",
        ],
    )

    st.markdown("---")
    st.markdown("🌐 **Professional Networks**")
    st.markdown("[🔗 LinkedIn Profile](https://www.linkedin.com/in/mohamed-talib-664331158)")
    st.markdown("📧 **Email:** medo.talib99@gmail.com")
    st.markdown("📱 **WhatsApp:** +249912559111")

# --- 1. HOME & OVERVIEW SECTION ---
if section == "Home & Overview":
    col_img, col_hero = st.columns([1, 2.5])

    with col_img:
        if encoded_image:
            st.markdown(
                f"""
                <div style="text-align: center; margin-bottom: 15px;">
                    <img src="data:image/jpeg;base64,{encoded_image}" 
                         style="width: 100%; max-width: 260px; border-radius: 16px; object-fit: cover; box-shadow: 0 10px 20px rgba(0,0,0,0.12); border: 4px solid #0f4c81;">
                </div>
                """,
                unsafe_allow_html=True,
            )
        st.info(
            "📍 **Current Base:** Lusaka, Zambia\n\n"
            "🏛️ **Affiliation:** Africa CDC / ZNPHI\n\n"
            "🎓 **Candidate:** Doctorate in Humanitarian Action"
        )

    with col_hero:
        st.markdown('<div class="main-title">Mohamed Mahmoud Talib, MSc</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-title">Public Health Informatics Professional | Data Scientist | Field Epidemiologist</div>', unsafe_allow_html=True)
        
        st.markdown(
            '<span class="badge">Epidemic Surveillance</span>'
            '<span class="badge">Artificial Intelligence</span>'
            '<span class="badge">Biostatistics</span>'
            '<span class="badge">GIS Spatial Mapping</span>'
            '<span class="badge">Humanitarian M&E</span>',
            unsafe_allow_html=True,
        )
        
        st.write(
            "Specializing at the intersection of **field epidemiology, digital health systems, and artificial intelligence** to strengthen outbreak surveillance and data-driven disease response across Africa. "
            "Combining advanced biostatistical modeling with strategic project management to guide researchers, academic scholars, and international humanitarian organizations."
        )
        
        st.write(
            "With over **seven years of experience**, I deliver high-impact quantitative insights, peer-reviewed manuscript development, and institutional M&E frameworks in fragile and conflict-affected settings."
        )

    st.markdown("---")
    
    # Impact Metrics
    st.subheader("Key Impact Pillars")
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown('<div class="stat-box"><div class="stat-number">7+ Years</div><div class="stat-label">Public Health & M&E</div></div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="stat-box"><div class="stat-number">Africa CDC</div><div class="stat-label">Informatics Fellow</div></div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="stat-box"><div class="stat-number">AI & ML</div><div class="stat-label">Outbreak Modeling</div></div>', unsafe_allow_html=True)
    with m4:
        st.markdown('<div class="stat-box"><div class="stat-number">100%</div><div class="stat-label">Data Confidentiality</div></div>', unsafe_allow_html=True)
