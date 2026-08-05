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

def display_image(window_name: str, img, wait_key: int = 0) -> None:
    """
    Displays an image using OpenCV or PIL GUI window.
    """
    if HAS_OPENCV and isinstance(img, np.ndarray):
        try:
            cv2.imshow(window_name, img)
            cv2.waitKey(wait_key)
            cv2.destroyAllWindows()
            return
        except Exception as e:
            print(f"[GUI Warning] OpenCV GUI display window unavailable: {e}")
            
    if HAS_PIL and hasattr(img, 'show'):
        try:
            img.show(title=window_name)
            return
        except Exception as e:
            print(f"[GUI Warning] PIL image display unavailable: {e}")
            
    print(f"[GUI Fallback] Rendering output window '{window_name}' (Saved to file)")

def create_pipeline_window(title: str = "Pipeline Test", width: int = 800, height: int = 500):
    """
    Creates a styled baseline dummy image canvas with team details matching reference specification.
    """
    if HAS_OPENCV:
        canvas = np.zeros((height, width, 3), dtype=np.uint8)
        
        cv2.putText(canvas, 'Virtual Vadodara Railway Station', (50, 70), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.putText(canvas, 'Baseline Pipeline Test', (50, 120), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(canvas, 'Group Members:', (50, 190), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(canvas, '1. Mayank Adi 24000858', (90, 240), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(canvas, '2. Zeel Vasoya 24001018', (90, 290), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(canvas, '3. Prashobh Nair 24001026', (90, 340), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(canvas, 'Status : Pipeline OK', (50, 430), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.85, (0, 255, 0), 2, cv2.LINE_AA)
        return canvas
    
    if HAS_PIL:
        img = Image.new('RGB', (width, height), (0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        try:
            f_title = ImageFont.truetype('arial.ttf', 28)
            f_sub = ImageFont.truetype('arial.ttf', 22)
            f_head = ImageFont.truetype('arial.ttf', 22)
            f_body = ImageFont.truetype('arial.ttf', 20)
            f_stat = ImageFont.truetype('arial.ttf', 24)
        except Exception:
            f_title = f_sub = f_head = f_body = f_stat = ImageFont.load_default()

        # Render styled text
        draw.text((50, 50), 'Virtual Vadodara Railway Station', fill=(0, 255, 0), font=f_title)
        draw.text((50, 105), 'Baseline Pipeline Test', fill=(255, 255, 255), font=f_sub)
        draw.text((50, 175), 'Group Members:', fill=(255, 255, 0), font=f_head)
        draw.text((90, 225), '1. Mayank Adi 24000858', fill=(255, 255, 255), font=f_body)
        draw.text((90, 270), '2. Zeel Vasoya 24001018', fill=(255, 255, 255), font=f_body)
        draw.text((90, 315), '3. Prashobh Nair 24001026', fill=(255, 255, 255), font=f_body)
        draw.text((50, 400), 'Status : Pipeline OK', fill=(0, 255, 0), font=f_stat)
        
        return img

    # Pure Python list canvas fallback
    canvas = [[[0, 0, 0] for _ in range(width)] for _ in range(height)]
    return canvas
