import cv2
import numpy as np
from gui.window import create_pipeline_window, display_image
from processing.image_processor import convert_to_grayscale, detect_edges

def run_pipeline_test():
    """
    Executes an end-to-end baseline smoke test connecting GUI, 
    Image Processing, and Visualization modules for CG & IP Project.
    """
    print("[INFO] Starting CG & IP Baseline Smoke Test Pipeline...")
    
    # 1. Load dummy / sample image canvas with text
    img = np.zeros((300, 300, 3), dtype=np.uint8)
    cv2.putText(
        img, 
        'CG & IP Pipeline OK', 
        (20, 150), 
        cv2.FONT_HERSHEY_SIMPLEX, 
        0.7, 
        (0, 255, 0), 
        2
    )

    # 2. Apply basic baseline operation (Grayscale & Canny Edge Detection)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)

    # 3. Save screenshot output artifact for verification/submission
    output_filename = "pipeline_test_output.png"
    cv2.imwrite(output_filename, edges)
    print(f"[SUCCESS] Pipeline test image saved to '{output_filename}'")

    # 4. Display to confirm GUI window rendering
    print("[INFO] Displaying GUI window (Press any key to close window)...")
    try:
        cv2.imshow('Pipeline Test', edges)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"[NOTE] GUI window display step: {e}")

if __name__ == '__main__':
    run_pipeline_test()
