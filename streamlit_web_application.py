import base64
import os
import numpy as np
import pandas as pd
import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Mohamed Talib | Public Health Informatics & Research Consultant",
    page_icon="🔬",
    layout="wide",
)

# Custom Styling
st.markdown(
    """
    <style>
    .main-header { font-size: 2.5rem; color: #1f77b4; font-weight: bold; }
    .sub-header { font-size: 1.3rem; color: #444444; font-weight: 500; }
    .card { background-color: #f8f9fa; padding: 22px; border-radius: 12px; margin-bottom: 15px; border-left: 5px solid #1f77b4; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    .review-card { background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); padding: 20px; border-radius: 10px; border-left: 4px solid #28a745; margin-bottom: 15px; }
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


# Encode Pic.jpg
encoded_image = get_base64_of_bin_file("Pic.jpg")

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    if encoded_image:
        st.markdown(
            f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <img src="data:image/jpeg;base64,{encoded_image}" 
                     style="width: 110px; height: 110px; border-radius: 50%; object-fit: cover; border: 3px solid #1f77b4; box-shadow: 0 4px 8px rgba(0,0,0,0.1); margin-bottom: 10px;">
                <h3 style="margin: 0; font-size: 1.1rem; color: #222;">Mohamed Talib, MSc</h3>
                <p style="font-size: 0.85rem; color: #666; margin: 2px 0;">Public Health Informatics</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.warning("⚠️ Upload 'Pic.jpg' to your project folder to display your profile picture here.")

    st.title("Navigation")
    section = st.radio(
        "Go to",
        [
            "Home",
            "About Me",
            "Services for Students (PhD/Master/BSc)",
            "Services for Organizations (M&E & Proposals)",
            "Interactive Data & Visualizations",
            "Photo Gallery & Profile",
            "Client Reviews",
            "Contact",
        ],
    )

    st.markdown("---")
    st.markdown("🔗 **Connect Online:**")
    st.markdown("[LinkedIn Profile](https://www.linkedin.com/in/mohamed-talib-664331158)")

# --- HOME SECTION ---
if section == "Home":
    col_img, col_intro = st.columns([1, 2.5])

    with col_img:
        if encoded_image:
            st.markdown(
                f"""
                <div style="text-align: center; padding-top: 10px; margin-bottom: 20px;">
                    <img src="data:image/jpeg;base64,{encoded_image}" style="width: 100%; max-width: 240px; border-radius: 16px; object-fit: cover; box-shadow: 0 8px 16px rgba(0,0,0,0.15); border: 4px solid #1f77b4;">
                </div>
                """,
                unsafe_allow_html=True,
            )
        st.info("📍 **Location:** Lusaka, Zambia / Africa CDC\n\n📧 **Email:** medo.talib99@gmail.com\n\n📱 **Phone:** +249912559111")

    with col_intro:
        st.markdown('<p class="main-header">Mohamed Mahmoud Talib, MSc</p>', unsafe_allow_html=True)
        st.markdown('<p class="sub-header">Public Health Informatics Professional | Africa CDC</p>', unsafe_allow_html=True)
        st.write("---")
        st.write(
            "Specializing in **epidemiology, digital health in Africa, and the application of artificial intelligence and data science** to strengthen disease surveillance and epidemic forecasting. Grounded in a commitment to human rights, health equity, and democratic governance, I combine advanced analytics with strategic partnership development to design sustainable, data-driven health solutions, particularly in fragile and conflict-affected settings."
        )
        st.write(
            "With over **seven years of experience**, I support academic researchers, postgraduate students, and humanitarian institutions in achieving rigorous scientific output and impactful program design."
        )

    st.write("---")
    st.subheader("Core Expertise & Pillars")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="card"><h4>Digital Health & Surveillance</h4><p>Digital disease surveillance, epidemic forecasting, and robust health data governance systems.</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="card"><h4>Advanced Analytics & AI</h4><p>Python, R, SQL, Machine Learning, and GIS spatial mapping for public health insights.</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="card"><h4>Humanitarian & M&E</h4><p>Situation analysis, M&E frameworks, and grant proposal development in complex environments.</p></div>', unsafe_allow_html=True)

# --- ABOUT ME SECTION ---
elif section == "About Me":
    st.header("About Me")
    st.write(
        "I am a Public Health Informatics Fellow at **Africa CDC / Zambia National Public Health Institute**, with an extensive background in epidemiology, humanitarian action, and strategic partnerships. My career spans field epidemiology, outbreak investigation, health data governance, and public health leadership."
    )

    st.subheader("Academic Background")
    st.markdown(
        """
    * **Doctor of Humanitarian Action & Development** (Candidate) – Geneva Institute of Humanitarian & Development Studies
    * **MSc in Applied Data Science and Artificial Intelligence** – European Global Institute
    * **Master by Research in Public Health** – University of Bahri
    * **BSc in Public and Environmental Health** – University of Bahri
    """
    )

    st.subheader("Technical & Analytical Stack")
    st.write(
        "**Languages & Tools:** Python (pandas, scikit-learn, XGBoost, Plotly, GeoPandas), R, SQL, STATA, SPSS, Power BI, Tableau, DHIS2, ArcGIS, QGIS, and KoboToolbox."
    )

# --- SERVICES FOR STUDENTS ---
elif section == "Services for Students (PhD/Master/BSc)":
    st.header("Research & Publication Support for Students")
    st.write(
        "Are you a **PhD, Master's, or BSc student** navigating your thesis or preparing a manuscript for peer-reviewed publication? I offer comprehensive mentorship and technical support across the research lifecycle:"
    )

    st.markdown(
        """
    * **Proposal & Protocol Design:** Framing strong research questions, conceptual frameworks, and methodological rigour.
    * **Data Analysis & Biostatistics:** Executing advanced quantitative and qualitative data analysis using Python, R, STATA, or SPSS.
    * **Geospatial Mapping & Visualization:** Building professional spatial maps and data visualizations (QGIS, ArcGIS, Python).
    * **Scientific Writing & Publishing:** Structuring theses, literature reviews, and drafting manuscripts tailored for high-impact international journals.
    """
    )
    st.success("💡 **Get in touch:** Send your research synopsis or topic to **medo.talib99@gmail.com** to discuss collaboration.")

# --- SERVICES FOR ORGANIZATIONS ---
elif section == "Services for Organizations (M&E & Proposals)":
    st.header("Institutional Support: M&E, Humanitarian Proposals & Situation Analysis")
    st.write(
        "I partner with NGOs, UN agencies, and health institutions to strengthen program design, monitoring systems, and strategic proposals:"
    )

    st.markdown(
        """
    * **Humanitarian Proposal Development:** Crafting evidence-based grant proposals, logical frameworks (logframes), and Theory of Change models for institutional donors.
    * **Monitoring & Evaluation (M&E):** Designing robust M&E frameworks, custom performance indicators, and automated reporting dashboards (Power BI, Tableau, DHIS2).
    * **Situation Analysis & Risk Assessment:** Conducting epidemiological outbreak evaluations, rapid needs assessments, and contextual risk analyses tailored for fragile and conflict-affected settings.
    """
    )
    st.success("💡 **Consulting Inquiries:** Reach out via WhatsApp (+249912559111) or email to discuss institutional terms.")

# --- INTERACTIVE DATA & VISUALIZATIONS SECTION ---
elif section == "Interactive Data & Visualizations":
    st.header("Interactive Epidemiological Visualizations")
    st.write("Explore interactive data models reflecting field surveillance, outbreak trends, and risk forecasting.")

    tab1, tab2 = st.tabs(["📈 Cholera Outbreak Trend Simulator", "🔬 Risk Factor Predictor"])

    with tab1:
        st.subheader("Simulated Epidemic Curve (Gadarif / Chibombo Clusters)")
        st.write("Adjust the week range to observe simulated epidemiological caseload trends.")

        weeks_slider = st.slider("Select Surveillance Weeks (W1 - W12)", 1, 12, (1, 10))

        np.random.seed(42)
        weeks = [f"Week {i}" for i in range(1, 13)]
        cases = [12, 25, 48, 85, 140, 110, 75, 45, 30, 18, 10, 5]
        df_chart = pd.DataFrame({"Week": weeks, "Suspected Cases": cases})

        filtered_df = df_chart.iloc[weeks_slider[0] - 1 : weeks_slider[1]]
        st.bar_chart(filtered_df.set_index("Week"))
        st.caption("Data source: Field outbreak surveillance records & descriptive epidemiological evaluations.")

    with tab2:
        st.subheader("Predictive Risk Modeling Tool")
        st.write("Test risk factors to simulate outbreak vulnerability indices.")

        col_a, col_b = st.columns(2)
        with col_a:
            rainfall = st.slider("Weekly Rainfall Index (mm)", 0, 150, 45)
            sanitation = st.slider("Sanitation Access Score (0-100)", 0, 100, 40)
        with col_b:
            pop_density = st.slider("Population Density Factor", 1, 10, 5)
            water_safety = st.slider("Safe Water Accessibility (%)", 0, 100, 50)

        risk_score = (rainfall * 0.4) + (pop_density * 3) - (sanitation * 0.3) - (water_safety * 0.3)

        st.metric(label="Calculated Outbreak Vulnerability Index", value=f"{max(10, min(95, risk_score)):.1f} / 100")
        if risk_score > 60:
            st.error("⚠️ High Risk Alert: Immediate water chlorination and enhanced community engagement recommended.")
        elif risk_score > 35:
            st.warning("⚡ Moderate Risk: Active monitoring and routine water quality testing advised.")
        else:
            st.success("✅ Low Risk: Stable epidemiological indicators.")

# --- PHOTO GALLERY & PROFILE SECTION ---
elif section == "Photo Gallery & Profile":
    st.header("Photo Gallery & Profile Showcase")
    st.write("View active profile pictures and field activity highlights.")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Primary Profile Picture")
        if encoded_image:
            st.markdown(
                f"""
                <div style="text-align: center; margin-bottom: 15px;">
                    <img src="data:image/jpeg;base64,{encoded_image}" style="width: 100%; max-height: 380px; border-radius: 12px; object-fit: cover; box-shadow: 0 6px 12px rgba(0,0,0,0.1);">
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.caption("Mohamed Talib, MSc — Public Health Informatics Professional")
        else:
            st.info("Upload `Pic.jpg` to your project folder to see it displayed here.")

    with col2:
        st.subheader("Upload & Preview New Photo")
        st.write("Upload a new image below to preview how it looks live in your application layout:")
        uploaded_file = st.file_uploader("Choose an image file (JPG / PNG)", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            st.image(uploaded_file, caption="Uploaded Image Preview", use_column_width=True)
            st.success("Image uploaded successfully! To set this permanently as your main photo, save it as `Pic.jpg` in your project folder.")

# --- CLIENT REVIEWS SECTION ---
elif section == "Client Reviews":
    st.header("Client Reviews & Testimonials")
    st.write("Feedback from students, researchers, and partner organizations who have collaborated on publications, data systems, and proposals.")

    st.markdown(
        """
        <div class="review-card">
            <p><b>"Exceptional biostatistical and manuscript guidance!"</b></p>
            <p><i>Mohamed's expertise in epidemiological data analysis and R/Python streamlined our outbreak evaluation paper. His rigorous approach ensured publication in a high-indexing journal.</i></p>
            <p style="font-size: 0.85rem; color: #555; text-align: right; margin: 0;">— Postgraduate Research Student, Public Health</p>
        </div>
        
        <div class="review-card">
            <p><b>"Outstanding M&E and Proposal Support"</b></p>
            <p><i>Working with Mohamed on our institutional logframe and grant proposal significantly elevated our proposal quality. Highly professional, prompt, and deeply knowledgeable in humanitarian settings.</i></
