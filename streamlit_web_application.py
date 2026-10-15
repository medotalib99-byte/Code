            
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
