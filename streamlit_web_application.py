import base64
import os
import numpy as np
import pandas as pd
import streamlit as st

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
# 2. CIVICA-INSPIRED CUSTOM CSS STYLING
# ==============================================================================
CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

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
    font-size: 1.05rem;
    margin-bottom: 8px;
}

.testimonial-quote {
    font-size: 0.97rem;
    color: #374151;
    font-style: italic;
    line-height: 1.6;
    margin-bottom: 10px;
}

.testimonial-author {
    font-size: 0.88rem;
    color: #004D34;
    font-weight: 700;
    text-align: right;
    margin: 0;
}

.testimonial-role {
    font-size: 0.8rem;
    color: #6B7280;
    text-align: right;
    margin: 0;
}

/* Direct Form Styling */
.form-input-label {
    font-weight: 600;
    font-size: 0.9rem;
    color: #1F2937;
    margin-bottom: 6px;
    display: block;
}

.form-input-field {
    width: 100%;
    padding: 10px 12px;
    border-radius: 6px;
    border: 1px solid #D1D5DB;
    font-size: 0.95rem;
    color: #1F2937;
    background-color: #ffffff;
    box-sizing: border-box;
}

.form-input-field:focus {
    outline: none;
    border-color: #004D34;
    box-shadow: 0 0 0 3px rgba(0, 77, 52, 0.15);
}

.form-submit-btn {
    background: linear-gradient(135deg, #004D34 0%, #003625 100%);
    color: #ffffff !important;
    padding: 12px 26px;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-weight: 700;
    font-size: 1rem;
    letter-spacing: 0.5px;
    box-shadow: 0 4px 14px rgba(0, 77, 52, 0.25);
    transition: all 0.2s ease;
}

.form-submit-btn:hover {
    background: #003625;
    transform: translateY(-1px);
}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


# ==============================================================================
# 3. HELPER FUNCTIONS & IMAGE HANDLING
# ==============================================================================
def find_and_encode_image():
    """
    Safely finds profile photo files ('Pic.jpg', 'pic.jpg', 'Pic.png', etc.)
    and returns base64 encoded string and format, or None.
    """
    candidate_filenames = [
        "Pic.jpg",
        "pic.jpg",
        "Pic.png",
        "pic.png",
        "Pic.jpeg",
        "pic.jpeg",
        "profile.jpg",
        "profile.png",
    ]
    for filename in candidate_filenames:
        if os.path.isfile(filename):
            try:
                with open(filename, "rb") as f:
                    data = f.read()
                mime = "png" if filename.lower().endswith(".png") else "jpeg"
                return base64.b64encode(data).decode(), mime
            except Exception:
                continue
    return None, None


encoded_image, img_mime = find_and_encode_image()


def render_avatar(size=120, border_color="#004D34", extra_style=""):
    """
    Renders the profile image if present, or an SVG graphic fallback avatar
    matching the CIVICA color palette.
    """
    if encoded_image:
        return (
            f'<img src="data:image/{img_mime};base64,{encoded_image}" '
            f'style="width: {size}px; height: {size}px; border-radius: 50%; '
            f'object-fit: cover; border: 3px solid {border_color}; '
            f'box-shadow: 0 6px 14px rgba(0,0,0,0.15); {extra_style}">'
        )
    # Modern SVG Fallback Icon with Initial "MT"
    svg_fallback = (
        f'<div style="width: {size}px; height: {size}px; border-radius: 50%; '
        f'background: linear-gradient(135deg, #004D34 0%, #002B1D 100%); '
        f'display: flex; align-items: center; justify-content: center; '
        f'border: 3px solid {border_color}; margin: 0 auto; box-shadow: 0 6px 14px rgba(0,0,0,0.15); {extra_style}">'
        f'<span style="color: #70E000; font-size: {int(size * 0.38)}px; font-weight: 800; font-family: sans-serif;">MT</span>'
        f'</div>'
    )
    return svg_fallback


# ==============================================================================
# 4. TOP BRAND HEADER BAR
# ==============================================================================
brand_header_html = """
<div class="brand-header">
    <div class="brand-logo">MOHAMED TALIB</div>
    <div class="brand-tagline">
        <span>Public Health Informatics & Research Consultancy</span>
        <span class="status-badge">● Available for Consultations</span>
    </div>
</div>
"""
st.markdown(brand_header_html, unsafe_allow_html=True)


# ==============================================================================
# 5. SIDEBAR NAVIGATION & PROFILE SUMMARY
# ==============================================================================
with st.sidebar:
    avatar_html = render_avatar(size=115, border_color="#70E000")
    sidebar_profile = f"""
    <div style="text-align: center; padding-bottom: 12px; margin-bottom: 14px; border-bottom: 1px solid #E5E7EB;">
        {avatar_html}
        <h3 style="margin: 10px 0 2px 0; font-size: 1.15rem; color: #004D34; font-weight: 800;">Mohamed Talib, MSc</h3>
        <p style="font-size: 0.85rem; color: #1F2937; font-weight: 600; margin: 0 0 2px 0;">Public Health Informatics Fellow</p>
        <p style="font-size: 0.80rem; color: #4B5563; margin: 0;">Africa CDC / ZNPHI</p>
    </div>
    """
    st.markdown(sidebar_profile, unsafe_allow_html=True)

    if not encoded_image:
        st.info("💡 Place `Pic.jpg` in your project folder to display your custom profile photo here.")

    st.markdown("### Navigation")
    section = st.radio(
        label="Select Section:",
        options=[
            "Home & Showcase",
            "About Profile",
            "Services for Students (PhD/MSc)",
            "Services for Organizations (M&E)",
            "Interactive Data & Analytics",
            "Photo Profile & Media",
            "Client Reviews",
            "Contact & Consultations",
        ],
        index=0,
        label_visibility="collapsed",
    )

    st.markdown("---")
    st.markdown("#### 🔗 Direct Channels")
    st.markdown(
        """
        - 🌐 [LinkedIn Profile](https://www.linkedin.com/in/mohamed-talib-664331158)
        - 📧 [medo.talib99@gmail.com](mailto:medo.talib99@gmail.com)
        - 📱 [WhatsApp (+249912559111)](https://wa.me/249912559111)
        - 📍 *Base: Lusaka, Zambia*
        """
    )
    st.caption("© 2026 Mohamed Talib. All rights reserved.")


# ==============================================================================
# 6. MULTI-PAGE SECTIONS
# ==============================================================================

# ------------------------------------------------------------------------------
# 6.1 HOME & SHOWCASE
# ------------------------------------------------------------------------------
if section == "Home & Showcase":
    col_hero_text, col_hero_img = st.columns([1.75, 1], gap="medium")

    with col_hero_text:
        hero_card_html = """
        <div class="hero-card">
            <div class="hero-pill">Public Health Informatics & AI Systems</div>
            <div class="hero-title">Empowering public health through digital data science.</div>
            <div class="hero-subtitle">
                Architecting digital disease surveillance pipelines, advanced biostatistical modeling, 
                and donor-grade M&E architectures across Africa CDC & ZNPHI deployments.
            </div>
            <div>
                <a href="#services" class="accent-btn">Explore Consultancy Services →</a>
            </div>
        </div>
        """
        st.markdown(hero_card_html, unsafe_allow_html=True)

    with col_hero_img:
        if encoded_image:
            hero_img_html = f"""
            <div style="background: #ffffff; padding: 12px; border-radius: 14px; text-align: center; 
                        box-shadow: 0 10px 25px rgba(0,0,0,0.06); border: 1px solid #E5E7EB;">
                <img src="data:image/{img_mime};base64,{encoded_image}" 
                     style="width: 100%; max-height: 275px; border-radius: 10px; object-fit: cover; 
                            border: 3px solid #004D34;">
                <div style="margin-top: 10px; font-weight: 700; color: #004D34;">Mohamed Talib, MSc</div>
                <div style="font-size: 0.82rem; color: #6B7280;">Health Informatics Fellow & Data Scientist</div>
            </div>
            """
            st.markdown(hero_img_html, unsafe_allow_html=True)
        else:
            hero_img_fallback = f"""
            <div style="background: #ffffff; padding: 24px 16px; border-radius: 14px; text-align: center; 
                        box-shadow: 0 10px 25px rgba(0,0,0,0.06); border: 1px solid #E5E7EB;">
                {render_avatar(size=140, border_color="#70E000")}
                <div style="margin-top: 14px; font-weight: 800; font-size: 1.1rem; color: #004D34;">Mohamed Talib, MSc</div>
                <div style="font-size: 0.84rem; color: #6B7280; margin-top: 2px;">Public Health Informatics Specialist</div>
                <div style="font-size: 0.78rem; color: #004D34; background: #E8F8F0; padding: 4px 10px; border-radius: 12px; margin-top: 10px; display: inline-block;">
                    📍 Lusaka, Zambia / Africa CDC
                </div>
            </div>
            """
            st.markdown(hero_img_fallback, unsafe_allow_html=True)

    # Key Impact Metrics
    st.markdown("### Professional Milestones & Impact")
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown(
            """
            <div class="stat-card">
                <div class="stat-number">7+</div>
                <div class="stat-label">Years Field & Research Experience</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with m2:
        st.markdown(
            """
            <div class="stat-card">
                <div class="stat-number">20+</div>
                <div class="stat-label">Surveillance & Outbreak Missions</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with m3:
        st.markdown(
            """
            <div class="stat-card">
                <div class="stat-number">30+</div>
                <div class="stat-label">MSc & PhD Theses Mentored</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with m4:
        st.markdown(
            """
            <div class="stat-card">
                <div class="stat-number">$15M+</div>
                <div class="stat-label">Donor Grants & Logframes Supported</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.markdown('<div id="services"></div>', unsafe_allow_html=True)
    st.subheader("Core Capabilities & Consultancy Verticals")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            """
            <div class="civica-card">
                <h4>Digital Health & Surveillance</h4>
                <p>Architecting electronic disease surveillance systems, DHIS2 implementations, epidemic alert pipelines, and interoperable health data governance across national institutes.</p>
                <ul>
                    <li>Integrated Disease Surveillance & Response (IDSR)</li>
                    <li>Automated outbreak early warning alerts</li>
                    <li>KoboToolbox, REDCap, and ODK deployment</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class="civica-card">
                <h4>Advanced Analytics & AI</h4>
                <p>Applying state-of-the-art predictive modeling, machine learning, spatial GIS mapping, and biostatistical pipelines to forecast outbreaks and inform rapid emergency response.</p>
                <ul>
                    <li>XGBoost & Random Forest risk modeling</li>
                    <li>QGIS / GeoPandas spatial clustering</li>
                    <li>R & Python epidemiological forecasting</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            """
            <div class="civica-card">
                <h4>Humanitarian M&E & Grants</h4>
                <p>Formulating rigorous donor-grade grant proposals, Theory of Change models, baseline evaluations, and executive Power BI dashboards for international agencies and NGOs.</p>
                <ul>
                    <li>USAID, Global Fund, and ECHO alignments</li>
                    <li>Logical Frameworks (Logframes) & KPI systems</li>
                    <li>Baseline, Midline, and Endline evaluations</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ------------------------------------------------------------------------------
# 6.2 ABOUT PROFILE
# ------------------------------------------------------------------------------
elif section == "About Profile":
    st.header("Professional Profile & Background")
    st.markdown(
        """
        I serve as a **Public Health Informatics Fellow** with **Africa CDC**, stationed at the 
        **Zambia National Public Health Institute (ZNPHI)** in Lusaka. With more than seven years of 
        field epidemiology, academic mentorship, and digital health leadership, I specialize in 
        translating complex clinical and humanitarian data into actionable intelligence for policy makers, 
        academics, and humanitarian organizations.
        """
    )

    st.markdown("---")
    col_edu, col_fellowships = st.columns(2, gap="medium")

    with col_edu:
        st.subheader("🎓 Academic Credentials")
        st.markdown(
            """
            <div class="civica-card">
                <h4>Doctor of Humanitarian Action & Development (Candidate)</h4>
                <p><em>Geneva Institute of Humanitarian & Development Studies</em></p>
                <p>Focus: Humanitarian health governance, conflict epidemiology, and emergency data architectures.</p>
            </div>
            <div class="civica-card">
                <h4>MSc in Applied Data Science & Artificial Intelligence</h4>
                <p><em>European Global Institute</em></p>
                <p>Specialization: Machine learning applications in communicable disease forecasting and health analytics.</p>
            </div>
            <div class="civica-card">
                <h4>Master by Research in Public Health</h4>
                <p><em>University of Bahri</em></p>
                <p>Thesis: Epidemiological investigation and environmental determinants of community outbreaks.</p>
            </div>
            <div class="civica-card">
                <h4>BSc in Public and Environmental Health</h4>
                <p><em>University of Bahri</em></p>
                <p>Graduated with distinction; foundational coursework in biostatistics, vector control, and sanitation.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_fellowships:
        st.subheader("🏛️ Institutional Fellowships & Roles")
        st.markdown(
            """
            <div class="civica-card">
                <h4>Public Health Informatics Fellow</h4>
                <p><strong>Africa CDC & ZNPHI (Lusaka, Zambia)</strong></p>
                <p>Leading digital health surveillance modernization, multi-source data integration, and technical capacity building for national rapid response teams.</p>
            </div>
            <div class="civica-card">
                <h4>Independent M&E & Biostatistics Consultant</h4>
                <p><strong>Regional Humanitarian & Academic Advisory</strong></p>
                <p>Advised 30+ postgraduate theses, designed institutional grant proposals, and developed automated surveillance dashboards for international NGOs.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.subheader("🛠️ Technical Proficiency & Toolkit")

    t1, t2, t3, t4 = st.columns(4)
    with t1:
        st.markdown(
            """
            <div class="civica-card">
                <h4>Data Science & ML</h4>
                <ul>
                    <li>Python (pandas, NumPy)</li>
                    <li>scikit-learn & XGBoost</li>
                    <li>R & tidyverse</li>
                    <li>SQL & Data Pipelines</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with t2:
        st.markdown(
            """
            <div class="civica-card">
                <h4>Biostatistics</h4>
                <ul>
                    <li>SPSS Statistics</li>
                    <li>STATA 17/18</li>
                    <li>Epi Info & CDC Tools</li>
                    <li>Survival Analysis & GLMs</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with t3:
        st.markdown(
            """
            <div class="civica-card">
                <h4>Spatial & GIS</h4>
                <ul>
                    <li>QGIS Desktop & Cloud</li>
                    <li>ArcGIS Pro</li>
                    <li>GeoPandas & Folium</li>
                    <li>Spatial Cluster Analysis</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with t4:
        st.markdown(
            """
            <div class="civica-card">
                <h4>Health Systems & BI</h4>
                <ul>
                    <li>DHIS2 Tracker & Capture</li>
                    <li>KoboToolbox & ODK</li>
                    <li>REDCap Administration</li>
                    <li>Power BI & Tableau</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ------------------------------------------------------------------------------
# 6.3 SERVICES FOR STUDENTS
# ------------------------------------------------------------------------------
elif section == "Services for Students (PhD/MSc)":
    st.header("Research & Thesis Mentorship for Postgraduate Scholars")
    st.markdown(
        """
        Providing high-caliber technical guidance for **PhD candidates, Master's scholars, and academic fellows** 
        in Public Health, Epidemiology, Global Health, and Data Science. From initial protocol formulation to 
        peer-reviewed manuscript acceptance in indexed journals (PubMed/Scopus).
        """
    )

    s1, s2 = st.columns(2, gap="medium")
    with s1:
        st.markdown(
            """
            <div class="civica-card">
                <h4>1. Proposal & Protocol Conception</h4>
                <ul>
                    <li><strong>Research Hypotheses & Conceptual Frameworks:</strong> Formulate rigorous, defensible primary and secondary research questions.</li>
                    <li><strong>Sample Size & Statistical Power:</strong> Calculate exact sample requirements for cross-sectional, cohort, case-control, and intervention studies.</li>
                    <li><strong>Institutional Review Board (IRB) Protocols:</strong> Structure complete ethics submissions adhering to international Declaration of Helsinki standards.</li>
                    <li><strong>Questionnaire & Tool Design:</strong> Build validated survey instruments in KoboToolbox, ODK, and REDCap.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with s2:
        st.markdown(
            """
            <div class="civica-card">
                <h4>2. Biostatistical Execution & Modeling</h4>
                <ul>
                    <li><strong>Data Cleansing & Imputation:</strong> Handle missing data, outliers, and normalization in Python, R, SPSS, or STATA.</li>
                    <li><strong>Inferential Statistics:</strong> Multivariable logistic regression, Poisson regression, Cox proportional hazards, and ANOVA models.</li>
                    <li><strong>Spatial Mapping & Epicurves:</strong> Produce publication-grade GIS thematic maps and epidemic curves.</li>
                    <li><strong>Code & Output Documentation:</strong> Receive annotated reproducible scripts and cleanly formatted statistical tables.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    s3, s4 = st.columns(2, gap="medium")
    with s3:
        st.markdown(
            """
            <div class="civica-card">
                <h4>3. Scientific Manuscript Writing</h4>
                <ul>
                    <li><strong>STROBE / PRISMA Compliance:</strong> Draft Results and Discussion sections matching strict journal reporting guidelines.</li>
                    <li><strong>High-Impact Visualizations:</strong> Generate vector charts, forest plots, and survival curves in 300+ DPI.</li>
                    <li><strong>Reviewer Response Strategy:</strong> Formulate point-by-point statistical rebuttals during journal peer review rounds.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with s4:
        st.markdown(
            """
            <div class="civica-card">
                <h4>4. Thesis Defense Coaching</h4>
                <ul>
                    <li><strong>Slide Deck Architecture:</strong> Distill 100+ thesis pages into a compelling 20-slide executive presentation.</li>
                    <li><strong>Defense Simulations:</strong> Mock defense interrogations focusing on methodology defense and limitations.</li>
                    <li><strong>Statistical Defense:</strong> Coaching on how to confidently defend statistical choices before external examiners.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.subheader("Mentorship Engagement Roadmap")
    r1, r2, r3, r4 = st.columns(4)
    r1.info("💬 **Step 1: Consultation**\n\nReview thesis guidelines, timeline, and current progress.")
    r2.info("📊 **Step 2: Analysis Plan**\n\nEstablish statistical analysis plan (SAP) and clean data.")
    r3.info("🔬 **Step 3: Modeling & Viz**\n\nExecute calculations, generate models, tables, and charts.")
    r4.success("🎓 **Step 4: Defense & Submission**\n\nFinal review, journal formatting, and defense rehearsal.")

# ------------------------------------------------------------------------------
# 6.4 SERVICES FOR ORGANIZATIONS
# ------------------------------------------------------------------------------
elif section == "Services for Organizations (M&E)":
    st.header("Institutional Solutions: Proposals, M&E Architectures & Analytics")
    st.markdown(
        """
        Partnering with **UN Agencies, International NGOs, Ministries of Health, and Research Consortia** 
        to engineer data systems, draft winning multimillion-dollar grant applications, and deliver 
        comprehensive field evaluations in complex settings.
        """
    )

    o1, o2 = st.columns(2, gap="medium")
    with o1:
        st.markdown(
            """
            <div class="civica-card">
                <h4>Grant Proposals & Strategic Frameworks</h4>
                <ul>
                    <li><strong>Donor Alignment:</strong> Tailor technical proposals for USAID, Global Fund, ECHO, FCDO, and Gavi funding mechanisms.</li>
                    <li><strong>Theory of Change (ToC):</strong> Design causal impact pathways, intermediate outcome indicators, and assumption matrices.</li>
                    <li><strong>Logical Frameworks (Logframes):</strong> Define SMART indicators, source verifications, and milestone tracking schedules.</li>
                    <li><strong>Needs Assessment:</strong> Rapid epidemiological situation analyses and baseline risk profiling in humanitarian crises.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with o2:
        st.markdown(
            """
            <div class="civica-card">
                <h4>Monitoring & Evaluation (M&E) Architectures</h4>
                <ul>
                    <li><strong>PMP & MEL Plan Design:</strong> Create end-to-end Performance Monitoring Plans with detailed Indicator Reference Sheets (PIRS).</li>
                    <li><strong>Real-time Surveillance Dashboards:</strong> Automated Power BI and Tableau dashboards connected directly to field databases.</li>
                    <li><strong>Field Evaluation Missions:</strong> Rigorous baseline, midline, and endline mixed-methods evaluations.</li>
                    <li><strong>Data Quality Audits (DQA):</strong> Verify completeness, reliability, and validity of field reports.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.subheader("Select Institutional Deliverables Portfolio")

    deliv_df = pd.DataFrame(
        [
            {
                "Sector": "Epidemic Surveillance",
                "Client / Domain": "National Public Health Agency",
                "Core Deliverable": "Integrated Disease Surveillance & Response (IDSR) automated alert pipeline",
                "Tools Applied": "DHIS2, Python, PostgreSQL",
            },
            {
                "Sector": "Humanitarian Health",
                "Client / Domain": "International NGO (WASH/Health)",
                "Core Deliverable": "Multimillion-dollar Global Fund grant proposal, Theory of Change & Logframe",
                "Tools Applied": "Logframe matrix, R, Power BI",
            },
            {
                "Sector": "Cross-Border Health",
                "Client / Domain": "Regional Health Body",
                "Core Deliverable": "GIS spatial mapping of cross-border transmission corridors and sentinel sites",
                "Tools Applied": "QGIS, GeoPandas, ArcGIS",
            },
            {
                "Sector": "Program Evaluation",
                "Client / Domain": "Community Health Consortium",
                "Core Deliverable": "Mixed-methods Endline Program Evaluation and Data Quality Assessment (DQA)",
                "Tools Applied": "KoboToolbox, STATA, Tableau",
            },
        ]
    )
    st.dataframe(deliv_df, use_container_width=True, hide_index=True)

# ------------------------------------------------------------------------------
# 6.5 INTERACTIVE DATA & ANALYTICS
# ------------------------------------------------------------------------------
elif section == "Interactive Data & Analytics":
    st.header("Interactive Outbreak Analytics Lab")
    st.markdown(
        """
        Explore live interactive epidemiological tools illustrating real-world surveillance modeling, 
        epidemic curve simulators, and multi-factor vulnerability indices.
        """
    )

    tab1, tab2 = st.tabs(["📈 Epidemic Curve Simulator & Interventions", "🔬 Outbreak Vulnerability Risk Calculator"])

    with tab1:
        st.subheader("Simulated Epidemic Curve Model with Policy Interventions")
        st.write("Adjust surveillance weeks and intervention timing to simulate transmission deceleration.")

        ctrl_col1, ctrl_col2, ctrl_col3 = st.columns(3)
        with ctrl_col1:
            total_weeks = st.slider("Total Surveillance Window (Weeks):", 8, 20, 14)
        with ctrl_col2:
            peak_week = st.slider("Unmitigated Peak Week:", 4, 10, 6)
        with ctrl_col3:
            intervention_active = st.checkbox("Apply Rapid WASH & Vaccine Intervention", value=True)

        weeks_list = [f"W{i:02d}" for i in range(1, total_weeks + 1)]
        raw_cases = []
        for w in range(1, total_weeks + 1):
            val = int(220 * np.exp(-((w - peak_week) ** 2) / (2 * (2.2**2))))
            if intervention_active and w > peak_week:
                decay = 0.55 ** (w - peak_week)
                val = int(val * decay)
            val = max(4, val + np.random.randint(-3, 4))
            raw_cases.append(val)

        sim_df = pd.DataFrame({"Surveillance Week": weeks_list, "Suspected Cholera Cases": raw_cases})

        st.bar_chart(sim_df.set_index("Surveillance Week"), color="#004D34", use_container_width=True)

        m1, m2, m3 = st.columns(3)
        total_cases = sum(raw_cases)
        max_cases = max(raw_cases)
        peak_idx = raw_cases.index(max_cases) + 1
        m1.metric("Cumulative Cases Recorded", f"{total_cases:,}")
        m2.metric("Peak Weekly Case Load", f"{max_cases:,}")
        m3.metric("Peak Epidemic Week", f"Week {peak_idx:02d}")

        csv_data = sim_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Download Surveillance Dataset (CSV)",
            data=csv_data,
            file_name="simulated_epidemic_curve.csv",
            mime="text/csv",
        )

    with tab2:
        st.subheader("Multi-Factor Community Vulnerability Calculator")
        st.write("Calculate a normalized risk index (0–100) based on environmental, demographic, and WASH metrics.")

        col_a, col_b = st.columns(2, gap="large")
        with col_a:
            st.markdown("##### 🌧️ Environmental & Demographic Drivers")
            rainfall = st.slider("Weekly Cumulative Rainfall (mm)", 0, 200, 75, help="Heavy precipitation exacerbates runoff and contamination.")
            pop_density = st.slider("Settlement Density Score (1 = Rural, 10 = High Informal Density)", 1, 10, 7)
            drainage_score = st.slider("Inadequate Drainage Infrastructure (%)", 0, 100, 65)

        with col_b:
            st.markdown("##### 🛡️ Protective WASH & Health System Barriers")
            clean_water = st.slider("Access to Treated Municipal / Chlorinated Water (%)", 0, 100, 35)
            sanitation = st.slider("Households with Improved Latrines (%)", 0, 100, 40)
            vaccine_coverage = st.slider("Oral Cholera Vaccine (OCV) Coverage (%)", 0, 100, 20)

        hazard_score = (rainfall * 0.25) + (pop_density * 4.5) + (drainage_score * 0.30)
        protective_score = (clean_water * 0.35) + (sanitation * 0.35) + (vaccine_coverage * 0.30)

        raw_index = 25 + hazard_score - (protective_score * 0.6)
        vulnerability_index = float(np.clip(raw_index, 5.0, 99.0))

        st.markdown("---")
        res_col1, res_col2 = st.columns([1, 1.8], gap="medium")

        with res_col1:
            st.metric(
                label="Calculated Outbreak Vulnerability Index",
                value=f"{vulnerability_index:.1f} / 100",
                delta=f"{'+ Critical' if vulnerability_index >= 65 else ('Moderate' if vulnerability_index >= 40 else '- Low')}",
                delta_color="inverse",
            )

        with res_col2:
            if vulnerability_index >= 65:
                st.error(
                    """
                    **🚨 TIER 1: CRITICAL VULNERABILITY ALERT**  
                    *Recommendations:* Immediate pre-positioning of Cholera Treatment Kits (CTKs), active point-of-use water chlorination campaigns, and targeted OCV reactive vaccination drive.
                    """
                )
            elif vulnerability_index >= 40:
                st.warning(
                    """
                    **⚡ TIER 2: MODERATE VULNERABILITY LEVEL**  
                    *Recommendations:* Increase sentinel laboratory surveillance testing, inspect municipal water distribution networks, and reinforce community risk communication.
                    """
                )
            else:
                st.success(
                    """
                    **✅ TIER 3: STABLE EPIDEMIOLOGICAL INDICATORS**  
                    *Recommendations:* Maintain routine IDSR passive surveillance and ongoing water quality bacteriological monitoring.
                    """
                )

# ------------------------------------------------------------------------------
# 6.6 PHOTO PROFILE & MEDIA
# ------------------------------------------------------------------------------
elif section == "Photo Profile & Media":
    st.header("Photo Showcase & Media Profile")
    st.markdown("Professional photo assets, field mission previews, and dynamic profile image tester.")

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.subheader("Active Primary Profile Photo")
        if encoded_image:
            profile_img_html = f"""
            <div style="text-align: center; background: #ffffff; padding: 18px; border-radius: 12px; 
                        box-shadow: 0 6px 18px rgba(0,0,0,0.06); border: 1px solid #E5E7EB;">
                <img src="data:image/{img_mime};base64,{encoded_image}" 
                     style="width: 100%; max-height: 400px; border-radius: 10px; object-fit: cover; 
                            border: 3px solid #004D34;">
                <div style="margin-top: 14px; font-weight: 800; font-size: 1.15rem; color: #004D34;">Mohamed Talib, MSc</div>
                <div style="font-size: 0.88rem; color: #4B5563;">Public Health Informatics Specialist & Consultant</div>
                <div style="font-size: 0.80rem; color: #6B7280; margin-top: 4px;">Lusaka, Zambia • Africa CDC / ZNPHI</div>
            </div>
            """
            st.markdown(profile_img_html, unsafe_allow_html=True)
        else:
            st.info(
                "💡 **No local image detected yet.**\n\n"
                "To display your photo, save your headshot as **`Pic.jpg`** in the same directory as this script."
            )
            st.markdown(
                f"""
                <div style="text-align: center; padding: 30px; background: #ffffff; border-radius: 12px; border: 1px solid #E5E7EB;">
                    {render_avatar(size=160, border_color="#004D34")}
                    <p style="margin-top: 15px; font-weight: 700; color: #004D34;">Avatar Placeholder Active</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    with col2:
        st.subheader("Test New Headshot / Preview")
        st.write("Upload a candidate photo to preview how it integrates with the Civica layout before setting it live:")

        uploaded_file = st.file_uploader("Upload Image (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            st.image(uploaded_file, caption="Live Preview of Uploaded Photo", use_container_width=True)
            st.success("✅ Looks great! To make this permanent, save this file as `Pic.jpg` in your root folder and refresh.")
        else:
            st.caption("Upload any standard portrait image (recommended 800x800px or 3:4 aspect ratio).")

# ------------------------------------------------------------------------------
# 6.7 CLIENT REVIEWS
# ------------------------------------------------------------------------------
elif section == "Client Reviews":
    st.header("Client Endorsements & Peer Reviews")
    st.markdown(
        """
        Feedback from postgraduate researchers, university faculty, and NGO project directors 
        who have partnered on biostatistical analyses, journal publications, and M&E systems.
        """
    )

    t1, t2 = st.columns(2, gap="medium")

    with t1:
        st.markdown(
            """
            <div class="testimonial-box">
                <div class="testimonial-rating">★★★★★ (5.0 / 5.0)</div>
                <div class="testimonial-quote">
                    "Mohamed's statistical mentorship was pivotal for my PhD dissertation. He guided my 
                    multivariable regression and survival analysis with extreme clarity, helping turn complex 
                    epidemiological data into publishable manuscripts. Accepted into an Q1 journal with minor revisions!"
                </div>
                <div class="testimonial-author">Dr. A. Mwewa, PhD</div>
                <div class="testimonial-role">Postgraduate Research Fellow in Epidemiology</div>
            </div>
            
            <div class="testimonial-box">
                <div class="testimonial-rating">★★★★★ (5.0 / 5.0)</div>
                <div class="testimonial-quote">
                    "His command of DHIS2 and spatial analytics is exceptional. Mohamed delivered a 
                    complete outbreak surveillance dashboard ahead of schedule, enabling our field teams 
                    to track hot-spots in near real-time during emergency deployments."
                </div>
                <div class="testimonial-author">H. Al-Hassan, MSc</div>
                <div class="testimonial-role">Humanitarian Health Coordinator, Emergency Response</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with t2:
        st.markdown(
            """
            <div class="testimonial-box">
                <div class="testimonial-rating">★★★★★ (5.0 / 5.0)</div>
                <div class="testimonial-quote">
                    "We engaged Mohamed to formulate our Theory of Change and M&E Logical Framework for an 
                    institutional Global Fund grant submission. His thorough indicator design and analytical rigor 
                    directly contributed to our successful consortium award."
                </div>
                <div class="testimonial-author">S. Banda, MPH</div>
                <div class="testimonial-role">Senior Program Manager, Regional Health Consortium</div>
            </div>

            <div class="testimonial-box">
                <div class="testimonial-rating">★★★★★ (5.0 / 5.0)</div>
                <div class="testimonial-quote">
                    "Prompt, meticulous, and deeply committed to scientific rigor. His sample size calculations 
                    and survey methodology for our community health study sailed through the Institutional Review Board (IRB) effortlessly."
                </div>
                <div class="testimonial-author">M. Elnour, MD, MSc</div>
                <div class="testimonial-role">Clinical Epidemiologist & Principal Investigator</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ------------------------------------------------------------------------------
# 6.8 CONTACT & CONSULTATIONS
# ------------------------------------------------------------------------------
elif section == "Contact & Consultations":
    st.header("Direct Inquiries & Consultation Booking")
    st.markdown(
        """
        Have an upcoming research project, thesis analysis need, grant proposal, or M&E architecture 
        requirement? Reach out directly below or submit your inquiry for a prompt response within 24 hours.
        """
    )

    col_info, col_form = st.columns([1, 1.25], gap="large")

    with col_info:
        st.markdown(
            """
            <div class="civica-card">
                <h4>Direct Communications</h4>
                <p>Feel free to reach out via your preferred communication channel:</p>
                <p>📧 <strong>Email:</strong><br>
                <a href="mailto:medo.talib99@gmail.com" style="color: #004D34; font-weight: 600;">medo.talib99@gmail.com</a></p>
                
                <p>📱 <strong>WhatsApp & Direct Line:</strong><br>
                <a href="https://wa.me/249912559111" target="_blank" style="color: #004D34; font-weight: 600;">+249 91 255 9111</a></p>
                
                <p>🌐 <strong>LinkedIn Profile:</strong><br>
                <a href="https://www.linkedin.com/in/mohamed-talib-664331158" target="_blank" style="color: #004D34; font-weight: 600;">linkedin.com/in/mohamed-talib-664331158</a></p>
                
                <p>📍 <strong>Primary Locations:</strong><br>
                Lusaka, Zambia (Africa CDC / ZNPHI) • Khartoum, Sudan</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div style="background-color: #E8F8F0; border-left: 4px solid #70E000; padding: 14px; border-radius: 6px;">
                <p style="margin: 0; font-size: 0.88rem; color: #004D34;">
                    ⚡ <strong>Fast Track Support:</strong> For urgent thesis submission deadlines or emergency outbreak M&E frameworks, WhatsApp is monitored daily.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_form:
        st.markdown("### Send an Inquiry (FormSubmit Integration)")
        st.markdown("Inquiries submitted through this secure form are forwarded immediately to `medo.talib99@gmail.com`.")

        contact_form_html = """
        <form action="https://formsubmit.co/medo.talib99@gmail.com" method="POST" enctype="multipart/form-data" 
              style="background: #ffffff; padding: 24px; border-radius: 10px; border: 1px solid #E5E7EB; box-shadow: 0 4px 14px rgba(0,0,0,0.03);">
            <input type="hidden" name="_subject" value="New Inquiry from Mohamed Talib Portfolio!">
            <input type="hidden" name="_captcha" value="false">
            <input type="hidden" name="_template" value="table">
            
            <div style="margin-bottom: 14px;">
                <label class="form-input-label">Full Name *</label>
                <input type="text" name="name" required placeholder="e.g. Dr. Jane Doe" class="form-input-field">
            </div>
            
            <div style="margin-bottom: 14px;">
                <label class="form-input-label">Email Address *</label>
                <input type="email" name="email" required placeholder="e.g. j.doe@university.edu" class="form-input-field">
            </div>

            <div style="margin-bottom: 14px;">
                <label class="form-input-label">Affiliation / Organization</label>
                <input type="text" name="organization" placeholder="e.g. University / NGO / Health Ministry" class="form-input-field">
            </div>
            
            <div style="margin-bottom: 14px;">
                <label class="form-input-label">Inquiry Category *</label>
                <select name="inquiry_type" class="form-input-field" style="height: 42px;">
                    <option value="Student Research Support (PhD/MSc)">Postgraduate Research / Thesis Support (PhD/MSc)</option>
                    <option value="Organizational M&E & Grant Proposals">Institutional M&E Frameworks & Grant Proposals</option>
                    <option value="Biostatistical Analysis & ML Modeling">Biostatistical Modeling & Outbreak Analytics</option>
                    <option value="Institutional Fellowship / Speaking">Professional Fellowship / Speaking Engagement</option>
                    <option value="Other Consultation">Other Inquiries</option>
                </select>
            </div>
            
            <div style="margin-bottom: 14px;">
                <label class="form-input-label">Project Scope & Requirements *</label>
                <textarea name="message" rows="4" required placeholder="Briefly detail your study design, dataset status, timeline, or scope of work..." class="form-input-field"></textarea>
            </div>

            <div style="margin-bottom: 18px;">
                <label class="form-input-label">Attach File / Document / Protocol (Optional, PDF or Image)</label>
                <input type="file" name="attachment" accept=".pdf,.doc,.docx,.png,.jpg,.jpeg" style="width: 100%; font-size: 0.88rem; color: #4B5563;">
            </div>
            
            <button type="submit" class="form-submit-btn">
                Send Direct Inquiry →
            </button>
        </form>
        """
        st.markdown(contact_form_html, unsafe_allow_html=True)

# ==============================================================================
# 7. FOOTER
# ==============================================================================
st.markdown("---")
footer_html = """
<div style="text-align: center; color: #6B7280; font-size: 0.85rem; padding: 10px 0 20px 0;">
    <strong>Mohamed Talib, MSc</strong> • Public Health Informatics & Research Consultancy<br>
    Africa CDC / Zambia National Public Health Institute (ZNPHI) • Lusaka, Zambia<br>
    Powered by Streamlit & Python • FormSubmit Direct Email Gateway
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)
