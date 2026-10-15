import base64
import os

# --- PAGE INITIALIZATION & STYLING ---
st.set_page_config(
    page_title="Mohamed Talib | Public Health Informatics & Research Consultant",
    page_icon="🔬",
    layout="wide",
)

# ... (rest of your custom style definitions here)

# Function to safely encode your local image for HTML display
def get_base64_of_bin_file(bin_file):
    if os.path.isfile(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None

# Sidebar Navigation & *UPDATED* Profile Branding
with st.sidebar:
    # 1. ADD: Encode and Display your Local Profile Photo
    encoded_image = get_base64_of_bin_file('profile.jpg')
    
    if encoded_image:
        st.markdown(
            f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <img src="data:image/jpeg;base64,{encoded_image}" 
                     style="width: 110px; height: 110px; border-radius: 50%; object-fit: cover; border: 3px solid #1f77b4; box-shadow: 0 4px 8px rgba(0,0,0,0.1); margin-bottom: 10px;">
                <h3 style="margin: 0; font-size: 1.1rem; color: #222;">Mohamed Talib, MSc</h3>
                <p style="font-size: 0.85rem; color: #666; margin: 2px
