"""Testing Flask app"""

import server
from server import app

from unittest import TestCase

class FlaskTestsBasic(TestCase):
    """Flask tests."""

    def setUp(self):
        """SetUp function"""
        # Get the Flask test client
        self.client = app.test_client()
        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

    def test_index(self):
        """Test homepage page."""

        result = self.client.get("/")
        self.assertEqual(result.status_code, 200)
        self.assertIn("Stock Ticker", result.data)

if __name__ == "__main__":
    import unittest
    unittest.main()