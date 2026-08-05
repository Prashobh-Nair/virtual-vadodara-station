try:
    import cv2
    import numpy as np
    HAS_OPENCV = True
except ImportError:
    HAS_OPENCV = False
    cv2 = None
    np = None

def display_image(window_name: str, img, wait_key: int = 0) -> None:
    """
    Displays an image using OpenCV GUI window.
    """
    if HAS_OPENCV and isinstance(img, np.ndarray):
        try:
            cv2.imshow(window_name, img)
            cv2.waitKey(wait_key)
            cv2.destroyAllWindows()
            return
        except Exception as e:
            print(f"[GUI Warning] OpenCV GUI display window unavailable: {e}")
    
    print(f"[GUI Fallback] Rendering output window '{window_name}' (Headless / Terminal mode)")

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
    
    # Pure Python canvas fallback
    canvas = [[[0, 0, 0] for _ in range(width)] for _ in range(height)]
    # Accent top border green
    for x in range(width):
        canvas[0][x] = [0, 255, 0]
        canvas[1][x] = [0, 255, 0]
    return canvas
