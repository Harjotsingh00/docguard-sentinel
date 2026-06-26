import streamlit as st
import requests
import json
import time
import streamlit_js_eval 

st.set_page_config(page_title="DocGuard Sentinel PRO | Forensic Ingestion Workspace", layout="wide", page_icon="⚡")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Main Session Architecture State Initializations
if "interaction_metrics" not in st.session_state:
    st.session_state.interaction_metrics = {
        "start_time": time.time(),
        "copy_paste_count": 0,
        "keystroke_delays": [],
        "hesitation_flags": 0
    }

st.sidebar.markdown("### **DocGuard Sentinel PRO**\n*Active Forensic Sandbox Module*")

st.title("⚡ Document Forensics & Agentic Audit Sandbox")
st.markdown("Deploy advanced structural computer vision checks and multi-modal integrity tracking simultaneously.")
st.markdown("---")

# --- ADVANCED FEATURE: JAVASCRIPT BEHAVIOR TELEMETRY LAYER ---
# Injecting a non-intrusive lightweight JS script to capture submission patterns
st.components.v1.html(
    """
    <script>
    const metrics = {
        copyPasteCount: 0,
        lastKeyTime: Date.now(),
        delays: []
    };
    
    // Capture Copy & Paste fraud pattern anomalies
    document.addEventListener('paste', (e) => {
        metrics.copyPasteCount++;
        window.parent.postMessage({type: 'TELEMETRY_PASTE', count: metrics.copyPasteCount}, '*');
    });
    
    // Track inter-keystroke input delays to catch bot-scripts/hesitation indicators
    document.addEventListener('keydown', (e) => {
        const now = Date.now();
        const delay = now - metrics.lastKeyTime;
        metrics.lastKeyTime = now;
        if(delay > 300) { // Delays above 300ms signal contextual manual assembly/hesitation
            window.parent.postMessage({type: 'TELEMETRY_DELAY', delay: delay}, '*');
        }
    });
    </script>
    """,
    height=0
)

w1, w2 = st.columns([1, 2])

with w1:
    st.markdown("#### 📥 Payload Configuration")
    app_id = st.text_input("Active Target Application Reference ID", "APP-2026-4412")
    
    st.info("💡 **Behavioral Tracking Layer Activated:** Interactions on this browser viewport (keystroke intervals, form copy-pastes) are being actively compiled into the operational risk analysis model.")
    
    # Text Inputs to let users naturally interact with the form to test JS tracking
    applicant_name = st.text_input("Applicant Full Name (Type to test telemetry)")
    declared_income = st.number_input("Declared Annual Gross Revenue ($)", min_value=0, value=50000)

    uploaded_files = st.file_uploader("Drop Forensic Evaluation Targets Here (JPEG only)", type=["jpg", "jpeg"], accept_multiple_files=True)
    
    if st.button("🚀 Execute Forensic Pipeline Evaluation", type="primary", use_container_width=True):
        if not uploaded_files:
            st.error("Submission blocked. Provide operational artifact items to verify.")
        else:
            # Complete calculating submission interaction profiles
            session_duration = round(time.time() - st.session_state.interaction_metrics["start_time"], 2)
            st.session_state.interaction_metrics["session_duration_sec"] = session_duration
            
            # Formulate payloads for FastAPI Engine processing
            files_payload = [("files", (f.name, f.getvalue(), f.type)) for f in uploaded_files]
            
            # Injecting structural payload tracking fields
            behavioral_payload = {
                "session_duration_sec": session_duration,
                "copy_paste_detected": st.session_state.interaction_metrics["copy_paste_count"],
                "hesitation_events": st.session_state.interaction_metrics["hesitation_flags"],
                "form_declared_income": declared_income,
                "applicant_name_field": applicant_name
            }
            
            data_payload = {"behavior": json.dumps(behavioral_payload)}
            
            with st.spinner("Analyzing artifacts across multi-modal & behavioral vectors..."):
                try:
                    BACKEND_URL = st.sidebar.text_input("Backend Engine URL", "https://docguard-backend.onrender.com")
                    res = requests.post(f"{BACKEND_URL}/api/v1/analyze", files=files_payload, data=data_payload)
                    if res.status_code == 200:
                        st.session_state.pro_api_response = res.json()
                        st.success("Verification Completed Successfully.")
                    else:
                        st.error(f"Processing Error: {res.text}")
                except Exception as e:
                    st.error(f"Backend Node Unreachable: {str(e)}")

with w2:
    st.markdown("#### 🛡️ Real-Time Intelligence Evaluation Stream")
    
    if "pro_api_response" in st.session_state:
        res_payload = st.session_state.pro_api_response
        agent_core = res_payload.get("agentic_layer", {})
        risk_score = agent_core.get("risk_score", 0)
        status_verdict = agent_core.get("compliance_status", "Flagged")
        
        # Micro Dashboard Row
        v1, v2 = st.columns(2)
        with v1:
            if risk_score > 60:
                st.error(f"### Score Assessment: {risk_score} / 100 [CRITICAL]")
            else:
                st.success(f"### Score Assessment: {risk_score} / 100 [SECURE]")
        with v2:
            st.warning(f"### System Decision: \n**{status_verdict}**")
            
        st.markdown("---")
        st.markdown("##### 🎯 Core Measurable Action Points (MAPs) Issued")
        for maps in agent_core.get("measurable_action_points", []):
            card_class = "map-card-danger" if risk_score > 50 else "map-card"
            st.markdown(f'<div class="{card_class}"><strong>Execution Directive:</strong> {maps}</div>', unsafe_allow_html=True)
            
        st.markdown("##### 🔬 Deep Computational Error Level Analysis (ELA) Reports")
        for r in res_payload.get("forensics_layer", []):
            st.info(f"📁 **File:** `{r['filename']}` | **Pixel Anomaly Density:** `{r['pixel_anomaly_percentage']}%` | **Tampering Suspicion:** `{r['metadata_tampering_detected']}`")
            
        st.markdown("##### 📜 Audit-Ready Contextual Highlights")
        for item in agent_core.get("explainable_highlights", []):
            st.markdown(f"🔹 {item}")
    else:
        st.markdown(
            "<div style='border: 2px dashed #ccc; padding: 40px; text-align: center; border-radius:10px; color:#888; margin-top:20px;'>"
            "Awaiting Payload Deployment via Left Operational Configuration Window Panel.</div>",
            unsafe_allow_html=True
        )