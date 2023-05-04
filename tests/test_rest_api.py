import unittest
import requests
from unittest.mock import Mock, patch
from src.science_graph.rest_api import RestAPI

class TestRestAPI(unittest.TestCase):

    def setUp(self):
        self.api = RestAPI('https://api.example.com')

    def test_get_successful(self):
        with patch('requests.get') as mock_get:
            mock_get.return_value = Mock(status_code=200, json=lambda: {"data": {"result": "success"}})
            response = self.api._get('/test')
            self.assertEqual(response['data'], {"result": "success"})

    def test_get_error_handling(self):
        with patch('requests.get') as mock_get:
            mock_get.side_effect = requests.exceptions.RequestException
            with self.assertRaises(requests.exceptions.RequestException):
                self.api._get('/test')

    # Add error handling tests for POST, PUT, DELETE, and any additional utility methods

if __name__ == '__main__':
    unittest.main()
