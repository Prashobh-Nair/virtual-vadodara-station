try:
    import cv2  # type: ignore
    import numpy as np  # type: ignore
    HAS_OPENCV = True
except ImportError:
    HAS_OPENCV = False
    cv2 = None
    np = None

def convert_to_grayscale(img):
    """
    Converts a BGR image to Grayscale.
    """
    if HAS_OPENCV and isinstance(img, np.ndarray):
        if len(img.shape) == 2:
            return img
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Pure Python / List Fallback
    if isinstance(img, list):
        h, w = len(img), len(img[0])
        gray = [[0]*w for _ in range(h)]
        for y in range(h):
            for x in range(w):
                pixel = img[y][x]
                if isinstance(pixel, (list, tuple)) and len(pixel) >= 3:
                    # Grayscale formula: 0.114*B + 0.587*G + 0.299*R
                    gray[y][x] = int(0.114 * pixel[0] + 0.587 * pixel[1] + 0.299 * pixel[2])
                else:
                    gray[y][x] = int(pixel)
        return gray
    return img

def detect_edges(img_gray, low_threshold: int = 100, high_threshold: int = 200):
    """
    Applies Canny Edge Detection to a grayscale image.
    """
    if HAS_OPENCV and isinstance(img_gray, np.ndarray):
        return cv2.Canny(img_gray, low_threshold, high_threshold)
    
    # Pure Python Edge Detection Fallback (Sobel / Gradient magnitude)
    if isinstance(img_gray, list):
        h, w = len(img_gray), len(img_gray[0])
        edges = [[0]*w for _ in range(h)]
        for y in range(1, h - 1):
            for x in range(1, w - 1):
                dx = img_gray[y][x+1] - img_gray[y][x-1]
                dy = img_gray[y+1][x] - img_gray[y-1][x]
                mag = min(255, int((dx*dx + dy*dy)**0.5))
                edges[y][x] = 255 if mag > 50 else 0
        return edges
    
    return img_gray

def apply_gaussian_blur(img, kernel_size: tuple = (5, 5), sigma_x: float = 0):
    """
    Applies Gaussian Blur to smooth an image.
    """
    if HAS_OPENCV and isinstance(img, np.ndarray):
        return cv2.GaussianBlur(img, kernel_size, sigma_x)
    return img

def equalize_histogram(img_gray):
    """
    Applies Histogram Equalization to enhance image contrast.
    """
    if HAS_OPENCV and isinstance(img_gray, np.ndarray):
        return cv2.equalizeHist(img_gray)
    return img_gray
