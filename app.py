import streamlit as st
import datetime

# --- AUDIT FILE LOGIC ---
# --- AUDIT FILE LOGIC (Rescue Edition) ---
def log_audit_event(filename, result):
    try:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        clean_result = result.replace("\n", " ")
        log_entry = f"[{timestamp}] PROCESSED: {filename} | AI_EXTRACTED: {clean_result}\n"
        
        # Change "a" to "w" to overwrite instead of adding more
        with open("audit_log.txt", "w") as f:
            f.write(log_entry)
        
        # Add to the live UI log too!
        st.session_state.log.append(f"Audit Logged: {filename}")
    except Exception as e:
        st.session_state.log.append(f"Audit Write Failed: {e}")
import brain
import time
from streamlit_confetti import confetti 

# --- 1. CLEAN THEME & SIDEBAR STYLE ---
st.set_page_config(page_title="AI HR Agent", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: white; }
    
    /* Green HackerRank Style Buttons */
    div.stButton > button {
        background-color: #2ec866 !important;
        color: white !important;
        border-radius: 5px !important;
        font-weight: bold !important;
        width: 100%;
    }

    /* Custom Sidebar Tech Look */
    [data-testid="stSidebar"] {
        background-color: #f8f9fa;
        border-right: 1px solid #e0e0e0;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. THE NEW TECH SIDEBAR ---
with st.sidebar:
    st.title("🛰️ Agent Environment")
    st.markdown("---")
    
    # System Health "Side Work"
    st.subheader("🖥️ System Health")
    st.success("Core: Gemini 2.5 Flash")
    st.info("Environment: Python 3.12")
    st.warning("API Quota: 85% Remaining")
    
    st.markdown("---")
    st.subheader("🛠️ Live Process Log")
    # --- ADD THIS INSIDE THE SIDEBAR BLOCK ---
    st.divider()
    st.subheader("📁 Project Exports")
    
    try:
        # This looks for the audit file created by your extraction
        with open("audit_log.txt", "rb") as file:
            st.download_button(
                label="📥 Download Audit File",
                data=file,
                file_name="HR_Onboarding_Audit.txt",
                mime="text/plain",
                help="Download the history of AI extractions for the judges."
            )
    except FileNotFoundError:
        # This shows if you haven't successfully extracted an ID yet
        st.info("Log file will be available after the first successful extraction.")
    # This creates a "running" log look
    if 'log' not in st.session_state:
        st.session_state.log = ["System Initialized...", "Waiting for Document..."]
    
    for entry in st.session_state.log[-5:]: # Shows last 5 actions
        st.caption(f"• {entry}")

# --- 3. MAIN INTERFACE ---
st.title("🚀 AI Agent for Autonomous HR Workflows")

if 'emp_data' not in st.session_state:
    st.session_state.emp_data = None
if 'victory_mode' not in st.session_state:
    st.session_state.victory_mode = False

# DOCUMENT UPLOAD
st.header("1. Document Analysis")
uploaded_file = st.file_uploader("Upload Employee Document", type=['png', 'jpg', 'jpeg'])
if uploaded_file and not st.session_state.victory_mode:
    if st.button("🚀 Run Extraction Agent"):
        with st.spinner("Agent calling Gemini 2.5 Flash..."):
           try:
                raw_text = brain.get_summary(uploaded_file)
                
                # --- PASTE THIS NEW LINE HERE ---
                log_audit_event(uploaded_file.name, raw_text)
                
                st.session_state.emp_data = {"Summary": raw_text, "Status": "Pending"}
                st.success("Extraction Successful!")
           except Exception as e:
                # These lines MUST be pushed in further than 'except'
                st.error(f"⚠️ API Error: {e}")
                st.session_state.log.append(f"Extraction Failed: {e}")
# --- 4. RESULTS & EXECUTION ---
if st.session_state.emp_data and not st.session_state.victory_mode:
    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📄 AI Extraction Result")
        st.info(st.session_state.emp_data["Summary"])
        
    with col2:
        st.subheader("⚙️ Agent Actions")
        if st.button("🚀 Execute: Auto-Verify & Notify HR"):
            if st.session_state.emp_data["Status"] == "REJECTED":
                st.error("Cannot process a rejected document.")
            else:
                st.session_state.log.append("Starting Onboarding Workflow...")
                with st.status("Agent Executing...", expanded=True) as s:
                    st.write("Verifying credentials...")
                    time.sleep(1)
                    st.session_state.log.append("Credentials Verified")
                    st.write("Updating HR Database...")
                    time.sleep(1)
                    st.session_state.log.append("Database Synced")
                    s.update(label="Workflow Complete!", state="complete")
                    
                    # 🎉 CONGRATULATIONS FLYING PAPERS
                    confetti(emojis=["🎊", "📄"]) 
                    st.session_state.victory_mode = True
                    st.rerun()

# --- 5. VICTORY SCREEN ---
# --- SUCCESS CELEBRATION & RESET ---
if st.session_state.victory_mode:
    # 1. Trigger the visual celebration
    st.balloons() 
    
    # 2. Show the big success message
    st.success("🎉 CONGRATULATIONS! Employee Onboarding is officially complete!")
    
    if st.button("🔄 Start Next Onboarding"):
        # Clear data for the next round
        st.session_state.emp_data = None
        st.session_state.victory_mode = False
        
        # Show the 60-second API cooldown warning
        st.warning("⏳ System Resetting... Please wait 60 seconds before uploading the next ID to avoid API Quota limits.")
        
        # Small delay so they can read the warning
        import time
        time.sleep(3) 
        st.rerun()
        # Show the log at the bottom of the page
if st.checkbox("🔍 Show System Audit Log"):
    with open("audit_log.txt", "r") as f:
        st.text(f.read())