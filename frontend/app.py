import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="DocGuard Sentinel PRO | Hub", layout="wide", page_icon="🛡️")

# Read structural CSS styling sheet
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Application Sidebar navigation system header
st.sidebar.image("https://img.icons8.com/fluent/100/000000/shield.png", width=80)
st.sidebar.markdown("### **DocGuard Sentinel PRO**\n*Secured Underwriting Infrastructure v2.1*")
st.sidebar.markdown("---")

# Main Page Core Content Frame
st.title("🛡️ DocGuard Sentinel Pro-Tier Console")
st.markdown("### Executive Underwriting & Security Risk Analytics Overview")
st.markdown("---")

# Top Level Summary KPI Grid Row
m1, m2, m3, m4 = st.columns(4)
m1.metric(label="Total Ingested Applications", value="1,482", delta="+12% This Week")
m2.metric(label="System Fraud Catch Rate", value="94.2%", delta="Optimal Precision")
m3.metric(label="Avg Processing Velocity", value="2.4 Mins", delta="-74% Time Reduction", delta_color="inverse")
m4.metric(label="Pending Manual Escalations", value="14 Files", delta="-3 Resolved", delta_color="normal")

st.markdown("### 📊 Operational Risk Distribution Trend lines")
c1, c2 = st.columns([2, 1])

with c1:
    # Time-series Chart generation using Plotly Express
    chart_data = pd.DataFrame({
        'Date': pd.date_range(start='2026-06-01', periods=10, freq='D'),
        'Clean Documents': [110, 125, 140, 135, 150, 165, 155, 170, 185, 190],
        'Anomalous Alerts Caught': [5, 12, 18, 9, 4, 21, 14, 8, 19, 32]
    })
    fig = px.line(chart_data, x='Date', y=['Clean Documents', 'Anomalous Alerts Caught'], 
                  title="Pipeline Processing Categorization Over Time", template="plotly_white",
                  color_discrete_sequence=["#1E88E5", "#E53935"])
    st.plotly_chart(fig, use_container_width=True)

with c2:
    # Distribution Pie
    pie_df = pd.DataFrame({
        'Category': ['Verified Clear', 'ELA Digital Discrepancy', 'Agent Text Conflict', 'Behavior Bot Alert'],
        'Count': [1120, 180, 122, 60]
    })
    fig_pie = px.pie(pie_df, values='Count', names='Category', title="Detected Threat Formats Breakdown",
                     color_discrete_sequence=px.colors.sequential.YlOrRd_r)
    st.plotly_chart(fig_pie, use_container_width=True)

st.markdown("---")
st.markdown("### 📥 Priority Action Underwriting Ingestion Queue")
# Interactive Dataframe mockup showcasing status tracking states
queue_data = pd.DataFrame({
    "Application ID": ["APP-2026-9041", "APP-2026-8992", "APP-2026-8841", "APP-2026-8720"],
    "Applicant Name": ["Aarav Sharma", "Priya Patel", "Vikram Malhotra", "Kabir Singh"],
    "Document Type Bundle": ["ITR + Bank Statement", "Land Deed Registry", "Income Proof + KYC", "Salary Slip"],
    "Threat Vector Flag": ["None - Passed Clear", "Image Forensics (ELA High Match)", "Cross-Doc Revenue Inconsistency", "Rapid Bot Form Autofill"],
    "System Risk Score": [12, 89, 74, 91],
    "Urgency Status": ["Low Priority", "Immediate Drop", "Escalated Review", "Immediate Drop"]
})

def color_status(val):
    if val == "Low Priority": return "background-color: #E8F5E9; color: #2E7D32"
    elif val == "Escalated Review": return "background-color: #FFF8E1; color: #F57F17"
    else: return "background-color: #FFEBEE; color: #C62828"

st.dataframe(queue_data.style.applymap(color_status, subset=['Urgency Status']), use_container_width=True)