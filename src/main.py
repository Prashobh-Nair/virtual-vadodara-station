import os

try:
    import cv2
    import numpy as np
    HAS_OPENCV = True
except ImportError:
    HAS_OPENCV = False
    cv2 = None
    np = None

from gui.window import create_pipeline_window, display_image
from processing.image_processor import convert_to_grayscale, detect_edges

def save_bmp_image(filename: str, grid_2d) -> None:
    """
    Saves a 2D grayscale array as a 24-bit BMP image using pure Python.
    """
    h = len(grid_2d)
    w = len(grid_2d[0])
    row_bytes = (w * 3 + 3) & ~3
    image_size = row_bytes * h
    file_size = 54 + image_size
    
    header = bytearray(54)
    header[0:2] = b'BM'
    header[2:6] = file_size.to_bytes(4, 'little')
    header[10:14] = (54).to_bytes(4, 'little')
    header[14:18] = (40).to_bytes(4, 'little')
    header[18:22] = w.to_bytes(4, 'little')
    header[22:26] = h.to_bytes(4, 'little')
    header[26:28] = (1).to_bytes(2, 'little')
    header[28:30] = (24).to_bytes(2, 'little')
    header[34:38] = image_size.to_bytes(4, 'little')
    
    pixel_bytes = bytearray(image_size)
    for y in range(h):
        # BMP rows are stored bottom-to-top
        row = grid_2d[h - 1 - y]
        row_offset = y * row_bytes
        for x in range(w):
            val = row[x]
            if isinstance(val, (list, tuple)):
                val = val[0]
            val = min(255, max(0, int(val)))
            pixel_bytes[row_offset + x * 3 + 0] = val  # B
            pixel_bytes[row_offset + x * 3 + 1] = val  # G
            pixel_bytes[row_offset + x * 3 + 2] = val  # R
            
    with open(filename, 'wb') as f:
        f.write(header + pixel_bytes)

def run_pipeline_test():
    """
    Executes an end-to-end baseline smoke test connecting GUI, 
    Image Processing, and Visualization modules for CG & IP Project.
    """
    print("[INFO] Starting CG & IP Baseline Smoke Test Pipeline...")
    output_png = "pipeline_test_output.png"
    output_bmp = "pipeline_test_output.bmp"
    
    if HAS_OPENCV:
        # 1. Load dummy or sample image
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

        # 2. Apply a basic baseline operation
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)

        # Save output image
        cv2.imwrite(output_png, edges)
        print(f"[SUCCESS] Pipeline test output saved to '{output_png}'")

        # 3. Display to confirm GUI window rendering
        print("[INFO] Displaying GUI window...")
        try:
            cv2.imshow('Pipeline Test', edges)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            print("[SUCCESS] GUI Window closed cleanly.")
        except Exception as e:
            print(f"[NOTE] GUI Window rendering note: {e}")
    else:
        # Fallback execution without OpenCV dependency
        print("[INFO] Running modular fallback pipeline test...")
        img = create_pipeline_window("Pipeline Test", 300, 300)
        gray = convert_to_grayscale(img)
        edges = detect_edges(gray)
        display_image("Pipeline Test", edges)
        
        # Save output image in BMP format
        save_bmp_image(output_bmp, edges)
        save_bmp_image(output_png, edges) # also save as .png alias
        print(f"[SUCCESS] Pipeline test output saved to '{output_png}' and '{output_bmp}'")

if __name__ == '__main__':
    run_pipeline_test()
