from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json
from app.forensics import perform_ela
from app.compliance import analyze_documents_and_generate_maps

app = FastAPI(title="DocGuard Sentinel Engine")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/v1/analyze")
async def analyze_pipeline(
    files: list[UploadFile] = File(...),
    behavior: str = Form(...)
):
    try:
        behavior_data = json.loads(behavior)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid behavior JSON payload format.")
    
    forensics_results = []
    file_contents = []
    
    for file in files:
        bytes_data = await file.read()
        file_contents.append(bytes_data)
        
        # 1. Run Structural Error Level Analysis
        is_tampered, score, _ = perform_ela(bytes_data)
        forensics_results.append({
            "filename": file.filename,
            "metadata_tampering_detected": is_tampered,
            "pixel_anomaly_percentage": score
        })
        
    # 2. Run Cross-Document Reasoning & Agentic Risk Analysis
    agent_output = analyze_documents_and_generate_maps(file_contents, behavior_data)
    
    # Combine signals into final verdict payload
    return {
        "forensics_layer": forensics_results,
        "agentic_layer": agent_output
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)