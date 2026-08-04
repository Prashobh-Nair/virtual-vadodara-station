import cv2
import numpy as np

def convert_to_grayscale(img: np.ndarray) -> np.ndarray:
    """
    Converts a BGR image to Grayscale.
    """
    if len(img.shape) == 2:
        return img
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def detect_edges(img_gray: np.ndarray, low_threshold: int = 100, high_threshold: int = 200) -> np.ndarray:
    """
    Applies Canny Edge Detection to a grayscale image.
    """
    return cv2.Canny(img_gray, low_threshold, high_threshold)

def apply_gaussian_blur(img: np.ndarray, kernel_size: tuple = (5, 5), sigma_x: float = 0) -> np.ndarray:
    """
    Applies Gaussian Blur to smooth an image.
    """
    return cv2.GaussianBlur(img, kernel_size, sigma_x)

def equalize_histogram(img_gray: np.ndarray) -> np.ndarray:
    """
    Applies Histogram Equalization to enhance image contrast.
    """
    return cv2.equalizeHist(img_gray)
