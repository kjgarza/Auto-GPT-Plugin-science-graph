import unittest
import requests
from unittest.mock import Mock, patch
from src.science_graph.base_api import BaseAPI

class TestBaseAPI(unittest.TestCase):

    def setUp(self):
        self.api = BaseAPI()

    def test_get_successful(self):
        with patch('requests.get') as mock_get:
            mock_get.return_value = Mock(status_code=200, json=lambda: {"result": "success"})
            response = self.api._get('https://example.com/api/test')
            self.assertEqual(response, {"result": "success"})

    def test_get_error_handling(self):
        with patch('requests.get') as mock_get:
            mock_get.side_effect = requests.exceptions.RequestException
            with self.assertRaises(requests.exceptions.RequestException):
                self.api._get('https://example.com/api/test')

    # Add similar tests for _post and _parse_response methods

if __name__ == '__main__':
    unittest.main()