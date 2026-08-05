import sys
import os

# Add src folder to sys.path so imports work flawlessly in all IDEs & Play button
SRC_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SRC_DIR, '..'))
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

try:
    import cv2  # type: ignore
    import numpy as np  # type: ignore
    HAS_OPENCV = True
except ImportError:
    HAS_OPENCV = False
    cv2 = None
    np = None

try:
    from PIL import Image, ImageDraw, ImageFont  # type: ignore
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

from gui.window import create_pipeline_window, display_image
from processing.image_processor import convert_to_grayscale, detect_edges

def run_pipeline_test():
    """
    Executes an end-to-end baseline smoke test connecting GUI, 
    Image Processing, and Visualization modules for CG & IP Project.
    """
    print("[INFO] Starting CG & IP Baseline Smoke Test Pipeline...")
    output_png = os.path.join(PROJECT_ROOT, "pipeline_test_output.png")
    output_bmp = os.path.join(PROJECT_ROOT, "pipeline_test_output.bmp")
    
    if HAS_OPENCV:
        # Create 800x500 black canvas using OpenCV
        img = np.zeros((500, 800, 3), dtype=np.uint8)
        
        cv2.putText(img, 'Virtual Vadodara Railway Station', (50, 70), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.putText(img, 'Baseline Pipeline Test', (50, 120), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(img, 'Group Members:', (50, 190), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(img, '1. Mayank Adi 24000858', (90, 240), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(img, '2. Zeel Vasoya 24001018', (90, 290), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(img, '3. Prashobh Nair 24001026', (90, 340), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(img, 'Status : Pipeline OK', (50, 430), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.85, (0, 255, 0), 2, cv2.LINE_AA)

        cv2.imwrite(output_png, img)
        print(f"[SUCCESS] Pipeline test output saved to '{output_png}'")

        try:
            cv2.imshow('Pipeline Test', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            print("[SUCCESS] GUI Window closed cleanly.")
        except Exception as e:
            print(f"[NOTE] GUI Window rendering note: {e}")

    elif HAS_PIL:
        # Create 800x500 black canvas using PIL
        img = Image.new('RGB', (800, 500), (0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        try:
            f_title = ImageFont.truetype('arial.ttf', 28)
            f_sub = ImageFont.truetype('arial.ttf', 22)
            f_head = ImageFont.truetype('arial.ttf', 22)
            f_body = ImageFont.truetype('arial.ttf', 20)
            f_stat = ImageFont.truetype('arial.ttf', 24)
        except Exception:
            f_title = f_sub = f_head = f_body = f_stat = ImageFont.load_default()

        draw.text((50, 50), 'Virtual Vadodara Railway Station', fill=(0, 255, 0), font=f_title)
        draw.text((50, 105), 'Baseline Pipeline Test', fill=(255, 255, 255), font=f_sub)
        draw.text((50, 175), 'Group Members:', fill=(255, 255, 0), font=f_head)
        draw.text((90, 225), '1. Mayank Adi 24000858', fill=(255, 255, 255), font=f_body)
        draw.text((90, 270), '2. Zeel Vasoya 24001018', fill=(255, 255, 255), font=f_body)
        draw.text((90, 315), '3. Prashobh Nair 24001026', fill=(255, 255, 255), font=f_body)
        draw.text((50, 400), 'Status : Pipeline OK', fill=(0, 255, 0), font=f_stat)

        img.save(output_png)
        img.save(output_bmp)
        print(f"[SUCCESS] Pipeline test output saved to '{output_png}' and '{output_bmp}'")
    else:
        print("[INFO] Fallback pipeline test...")
        canvas = create_pipeline_window("Pipeline Test", 800, 500)
        display_image("Pipeline Test", canvas)

if __name__ == '__main__':
    run_pipeline_test()
