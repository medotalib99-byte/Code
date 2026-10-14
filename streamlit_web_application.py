import streamlit as st

# Page Configuration
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
    .card { background-color: #f8f9fa; padding: 20px; border-radius: 10px; margin-bottom: 15px; border-left: 5px solid #1f77b4; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar Navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio(
    "Go to",
    [
        "Home",
        "About Me",
        "Services for Students (PhD/Master/BSc)",
        "Services for Organizations (M&E & Proposals)",
        "Contact",
    ],
)

# --- HOME SECTION ---
if section == "Home":
    st.markdown('<p class="main-header">Mohamed Mahmoud Talib, MSc</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Public Health Informatics Professional | Africa CDC</p>', unsafe_allow_html=True)
    st.write("---")

    col1, col2 = st.columns([2, 1])
    with col1:
        st.write(
            "Specializing in **epidemiology, digital health in Africa, and the application of artificial intelligence and data science** to strengthen disease surveillance and epidemic forecasting. Grounded in a commitment to human rights, health equity, and democratic governance, I combine advanced analytics with strategic partnership development to design sustainable, data-driven health solutions, particularly in fragile and conflict-affected settings."
        )
        st.write(
            "With over **seven years of experience**, I support academic researchers, postgraduate students, and humanitarian institutions in achieving rigorous scientific output and impactful program design."
        )

    with col2:
        st.info("📍 **Location:** Lusaka, Zambia / Africa CDC\n\n📧 **Email:** medo.talib99@gmail.com\n\n📱 **Phone:** +249912559111")

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

# --- CONTACT SECTION ---
elif section == "Contact":
    st.header("Get in Touch")
    st.write(
        "Whether you are a student looking for research guidance, an organization seeking M&E support, or interested in a professional collaboration, I'd love to hear from you."
    )

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
        ### Direct Contacts
        * **Email:** medo.talib99@gmail.com
        * **Phone / WhatsApp:** +249912559111
        * **Current Base:** Lusaka, Zambia
        """
        )
    with col2:
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email / Organization")
            service = st.selectbox(
                "Inquiry Type",
                [
                    "Student Research Support",
                    "Institutional M&E / Proposal Writing",
                    "General Collaboration",
                ],
            )
            message = st.text_area("Brief Message")
            submitted = st.form_submit_button("Submit Inquiry")

            if submitted:
                st.success(
                    f"Thank you, {name}! Your inquiry regarding {service} has been received. You can also email me directly at medo.talib99@gmail.com."
                )