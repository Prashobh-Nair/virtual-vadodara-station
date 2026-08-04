import unittest
import sys
import os

# Add src to python path for testing
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from processing.image_processor import convert_to_grayscale, detect_edges, apply_gaussian_blur
from gui.window import create_pipeline_window

class TestCGIPPipeline(unittest.TestCase):

    def test_create_pipeline_window(self):
        canvas = create_pipeline_window(width=300, height=300)
        self.assertIsNotNone(canvas)

    def test_convert_to_grayscale(self):
        # Test 3-channel input
        dummy_img = [[[0, 0, 0] for _ in range(10)] for _ in range(10)]
        gray_img = convert_to_grayscale(dummy_img)
        self.assertIsNotNone(gray_img)

    def test_detect_edges(self):
        dummy_gray = [[0]*10 for _ in range(10)]
        for i in range(3, 7):
            for j in range(3, 7):
                dummy_gray[i][j] = 255
        edges = detect_edges(dummy_gray, 100, 200)
        self.assertIsNotNone(edges)

    def test_gaussian_blur(self):
        dummy_img = [[[100, 100, 100] for _ in range(10)] for _ in range(10)]
        blurred = apply_gaussian_blur(dummy_img, (3, 3))
        self.assertIsNotNone(blurred)

if __name__ == '__main__':
    unittest.main()
