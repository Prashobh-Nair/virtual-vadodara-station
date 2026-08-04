import cv2
import numpy as np

def display_image(window_name: str, img: np.ndarray, wait_key: int = 0) -> None:
    """
    Displays an image using OpenCV GUI window.
    
    Args:
        window_name: Title of the GUI window.
        img: Input NumPy image array.
        wait_key: Key delay in milliseconds (0 for indefinite).
    """
    try:
        cv2.imshow(window_name, img)
        cv2.waitKey(wait_key)
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"[GUI Warning] Display window output fallback: {e}")

def create_pipeline_window(title: str = "Pipeline Test", width: int = 300, height: int = 300) -> np.ndarray:
    """
    Creates a baseline dummy image canvas with text for GUI pipeline testing.
    """
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
