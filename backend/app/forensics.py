import cv2
import numpy as np
from PIL import Image
import io

def perform_ela(image_bytes: bytes, quality: int = 90) -> tuple[bool, float, bytes]:
    """
    Performs Error Level Analysis (ELA) to detect digital alterations.
    """
    # Load image from bytes
    orig_img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    
    # Save temporary compressed version
    compressed_io = io.BytesIO()
    orig_img.save(compressed_io, 'JPEG', quality=quality)
    compressed_io.seek(0)
    compressed_img = Image.open(compressed_io)
    
    # Calculate absolute difference
    orig_array = np.array(orig_img, dtype=np.int16)
    comp_array = np.array(compressed_img, dtype=np.int16)
    diff = np.abs(orig_array - comp_array)
    
    # Scale the differences to make anomalies visible
    max_diff = np.max(diff)
    if max_diff == 0:
        max_diff = 1
    scale = 255.0 / max_diff
    diff = (diff * scale).astype(np.uint8)
    
    # Calculate anomaly score based on high-variance pixel concentrations
    gray_diff = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    _, thresh = cv2.threshold(gray_diff, 35, 255, cv2.THRESH_BINARY)
    anomaly_ratio = np.sum(thresh == 255) / thresh.size
    
    # Flag structural anomalies if ratio passes a 1.5% threshold
    is_tampered = bool(anomaly_ratio > 0.015)
    
    # Convert ELA diff image back to bytes for frontend rendering
    ela_img = Image.fromarray(diff)
    output_io = io.BytesIO()
    ela_img.save(output_io, format="JPEG")
    
    return is_tampered, round(anomaly_ratio * 100, 2), output_io.getvalue()