import os
from google import genai
from google.genai import types

def analyze_documents_and_generate_maps(file_bytes_list: list[bytes], behavior_metrics: dict) -> dict:
    """
    PRO FEATURE: Performs deep cross-document analysis by cross-verifying data extraction points 
    (e.g. declared form income vs financial data visible in uploaded multi-page documents).
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return {"error": "API Key configuration missing."}
        
    client = genai.Client(api_key=api_key)
    
    # Establish Agent System Directives
    system_instruction = """
    You are the DocGuard Sentinel Pro Intelligence Agent specialized in automated forensic cross-document underwriting.
    Your objective is to ingest user form interaction values, compare them with extracted visual textual evidence from all uploaded files, and perform deep consistency checks.
    
    CRITICAL LOOKUPS:
    1. Cross-verify if the income stated in the application matches structural text fields inside the document images (e.g., Bank Statement ledger balances, ITR total income).
    2. Review behavioral flags: High copy-paste counts or excessive delays indicate potential automated fraud or script-bot extraction.
    3. Look for physical text misalignments, formatting issues, or font discrepancies in the document images.
    """
    
    contents = [system_instruction]
    
    # Load all multi-modal structural file artifacts into execution payload
    for i, file_bytes in enumerate(file_bytes_list):
        contents.append(
            types.Part.from_bytes(
                data=file_bytes,
                mime_type="image/jpeg"
            )
        )
    
    # Inject active programmatic telemetry metadata context directly into the prompt stream
    contents.append(
        f"\n[CRITICAL PARAMETERS] UI Input Declared Income: ${behavior_metrics.get('form_declared_income')}. "
        f"Applicant Target Name: {behavior_metrics.get('applicant_name_field')}. "
        f"Telemetry Profile: Copy-Pastes = {behavior_metrics.get('copy_paste_detected')}, Session Time = {behavior_metrics.get('session_duration_sec')}s."
    )
    
    # Structural JSON Enforcement Scheme
    prompt = """
    Evaluate everything provided above. Output a JSON dictionary with exactly these primitive keys:
    {
       "risk_score": <int from 0 to 100 representing composite risk calculation tracking>,
       "explainable_highlights": ["List of precise reasons explaining the data variances found across documents"],
       "measurable_action_points": ["Explicit, urgent tasks for underwriters with strict time/source tracking tags. Example: 'Flag: Income mismatch in ITR vs Statement - Recommend credit bureau check within 24 hrs'"],
       "compliance_status": "Passed" | "Flagged for Manual Review" | "Rejected"
    }
    """
    contents.append(prompt)
    
    try:
        response = client.models.generate_content(
            model='gemini-1.5-flash',
            contents=contents,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                temperature=0.1  # Low temperature ensures strict adherence to underwriting principles
            )
        )
        import json
        return json.loads(response.text)
    except Exception as e:
        return {
            "risk_score": 50,
            "explainable_highlights": [f"AI Processing Anomaly: {str(e)}"],
            "measurable_action_points": ["System Error: Require manual document package fallback validation."],
            "compliance_status": "Flagged for Manual Review"
        }