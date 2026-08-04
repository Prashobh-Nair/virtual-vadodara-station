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
    
    Args:
        window_name: Title of the GUI window.
        img: Input image array.
        wait_key: Key delay in milliseconds (0 for indefinite).
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

def create_pipeline_window(title: str = "Pipeline Test", width: int = 300, height: int = 300):
    """
    Creates a baseline dummy image canvas with text for GUI pipeline testing.
    """
    if HAS_OPENCV:
        canvas = np.zeros((height, width, 3), dtype=np.uint8)
        cv2.putText(
            canvas, 
            'CG & IP Pipeline OK', 
            (20, height // 2), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.7, 
            (0, 255, 0), 
            2
        )
        return canvas
    
    # Pure Python canvas fallback
    canvas = [[[0, 0, 0] for _ in range(width)] for _ in range(height)]
    # Draw simple representation in center
    mid_y = height // 2
    for x in range(20, width - 20):
        canvas[mid_y][x] = [0, 255, 0]
    return canvas
