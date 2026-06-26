# 🛡️ DocGuard Sentinel
### Real-Time Multi-Modal Anomaly Detection & Agentic Intelligence Platform for Secure Banking Underwriting

Developed for the **SurakshaCyber Hackathon** hosted by **Canara Bank** on HackerEarth.

---

## 📌 Executive Summary & Problem Statement

In modern digital banking infrastructures, loan underwriting workflows are heavily targeted by sophisticated document forgery, AI-generated fakes, and digital alterations. Traditional rule-based Optical Character Recognition (OCR) systems flag glaring errors but fall short against pixel-level image splicing, cross-document telemetry gaps, and bot-assisted automated applications. 

**DocGuard Sentinel** addresses these systemic structural vulnerabilities by introducing an end-to-end, multi-modal verification paradigm. By combining computer vision error-level forensics, behavioral analytics, and autonomous LLM-driven reasoning, the platform reduces manual evaluation time by **60-70%**, drastically cuts Non-Performing Assets (NPAs), and generates explicit, time-bound **Measurable Action Points (MAPs)** for credit underwriting committees.

---

## 🧠 Core System Architecture

DocGuard Sentinel runs a decoupled, asynchronous multi-layer evaluation framework designed to capture security threats at every point of user interaction:

```text
[ User Ingestion Viewport ] ──► Captures Document Binaries + Interaction Biometrics
                                     │
            ┌────────────────────────┴────────────────────────┐
            ▼                                                 ▼
┌────────────────────────┐                        ┌────────────────────────┐
│  Image Forensics Layer │                        │  Behavioral Analytics  │
├────────────────────────┤                        ├────────────────────────┤
│ • Error Level Analysis │                        │ • Copy/Paste Tracker   │
│ • Pixel-Variance Delta │                        │ • Session Hesitation   │
└───────────┬────────────┘                        └───────────┬────────────
            │                                                 │
            └────────────────────────┬────────────────────────┘
                                     ▼
                  ┌──────────────────────────────────────┐
                  │ Multi-Modal Agentic Reasoning Layer  │
                  ├──────────────────────────────────────┤
                  │ • Gemini 1.5 Flash Context Engine    │
                  │ • Cross-Document Semantic Audit      │
                  └──────────────────┬───────────────────┘
                                     ▼
                  ┌──────────────────────────────────────┐
                  │  Underwriting Verification Console   │
                  ├──────────────────────────────────────┤
                  │ • Risk Indices (0-100)               │
                  │ • Executable Action Directives (MAPs)│
                  └──────────────────────────────────────┘
