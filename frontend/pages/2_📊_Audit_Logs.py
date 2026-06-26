import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="DocGuard Sentinel PRO | Audit Logs", layout="wide", page_icon="📊")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("📊 Security Logging & Compliance Auditing Ledger")
st.markdown("Immutable operational telemetry capturing user interaction vectors, forensic scores, and AI decisions.")
st.markdown("---")

# Mock data compilation for structural tracking logs
np.random.seed(42)
logs_count = 15
logs_df = pd.DataFrame({
    "Timestamp": pd.date_range(start="2026-06-23 09:00:00", periods=logs_count, freq="min"),
    "Application Reference ID": [f"APP-2026-{np.random.randint(1000, 9999)}" for _ in range(logs_count)],
    "Session Duration (s)": np.random.randint(15, 180, size=logs_count),
    "Interaction Flags": np.random.randint(0, 5, size=logs_count),
    "Forensic Error Flag": np.random.choice(["TRUE", "FALSE"], size=logs_count, p=[0.3, 0.7]),
    "System Risk Index": np.random.randint(5, 95, size=logs_count),
    "Assigned Vault Status": np.random.choice(["Approved", "Escalated to Credit Committee", "Declined"], size=logs_count, p=[0.6, 0.2, 0.2])
})

# Summary Row Metrics
a1, a2, a3 = st.columns(3)
a1.metric("Average Security Session Evaluation", f"{int(logs_df['Session Duration (s)'].mean())} Seconds")
a2.metric("Total Flagged Anomaly Sessions", f"{int((logs_df['Forensic Error Flag'] == 'TRUE').sum())} Warnings")
a3.metric("System Automation Touchless Ratio", "78.4%")

st.markdown("### 🗄️ Master System Telemetry Index Engine Database Logs")
st.dataframe(logs_df, use_container_width=True)

# Export Data Block UI Element 
st.markdown("---")
st.download_button(
    label="📥 Download System Audit Log Sheet (.CSV)",
    data=logs_df.to_csv(index=False),
    file_name="docguard_sentinel_june2026_audit.csv",
    mime="text/csv",
    use_container_width=False
)