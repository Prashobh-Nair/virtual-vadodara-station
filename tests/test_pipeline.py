import unittest
import numpy as np
import sys
import os

# Add src to python path for testing
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from processing.image_processor import convert_to_grayscale, detect_edges, apply_gaussian_blur
from gui.window import create_pipeline_window

class TestCGIPPipeline(unittest.TestCase):

    def test_create_pipeline_window(self):
        canvas = create_pipeline_window(width=300, height=300)
        self.assertEqual(canvas.shape, (300, 300, 3))
        self.assertEqual(canvas.dtype, np.uint8)

    def test_convert_to_grayscale(self):
        bgr_img = np.zeros((100, 100, 3), dtype=np.uint8)
        gray_img = convert_to_grayscale(bgr_img)
        self.assertEqual(gray_img.shape, (100, 100))

    def test_detect_edges(self):
        gray_img = np.zeros((100, 100), dtype=np.uint8)
        # Draw a white square in center
        gray_img[30:70, 30:70] = 255
        edges = detect_edges(gray_img, 100, 200)
        self.assertEqual(edges.shape, (100, 100))
        self.assertTrue(np.max(edges) > 0)  # Should detect square borders

    def test_gaussian_blur(self):
        img = np.ones((50, 50, 3), dtype=np.uint8) * 100
        blurred = apply_gaussian_blur(img, (3, 3))
        self.assertEqual(blurred.shape, (50, 50, 3))

if __name__ == '__main__':
    unittest.main()
