import unittest
from unittest.mock import MagicMock, patch
from src.science_graph.science_graph import ScienceGraph
from src.science_graph.api_factory import APIFactory
import json
class TestScienceGraph(unittest.TestCase):

    def setUp(self):
        self.pid_science_kg = ScienceGraph()

    def test_search_scholarly_works(self):
        mock_graphql_api = MagicMock()
        mock_graphql_api.query.return_value = {"works": {"nodes": [{"title": "Test Title"}]}}
        
        with patch.object(APIFactory, 'create_api', return_value=mock_graphql_api) as mock_create_api:
            response = self.pid_science_kg._search_scholarly_works("test_keyword")
            self.assertEqual(response, json.dumps( [{"title": "Test Title"}], ensure_ascii=False, indent=4))
            mock_create_api.assert_called_with('graphql')

    def test_search_journal_articles(self):
        mock_rest_api = MagicMock()
        mock_rest_api.query.return_value = {"message":{"items":[{"url": [{"title": "Test Title"}]}]}}
        
        with patch.object(APIFactory, 'create_api', return_value=mock_rest_api) as mock_create_api:
            response = self.pid_science_kg._search_journal_articles("test_keyword")
            self.assertEqual(response, json.dumps([{"url": [{"title": "Test Title"}]}], ensure_ascii=False, indent=4))
            mock_create_api.assert_called_with('rest')

if __name__ == '__main__':
    unittest.main()
