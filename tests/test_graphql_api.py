import unittest
from unittest.mock import MagicMock
from src.science_graph.graphql_api import GraphQLAPI

class TestGraphQLAPI(unittest.TestCase):

    def setUp(self):
        self.api_key = '123'
        self.url = 'https://example.com/graphql'
        self.graphql_api = GraphQLAPI(url=self.url, api_key=self.api_key)

    def test_get_headers_with_api_key(self):
        headers = self.graphql_api._get_headers()
        self.assertEqual(headers['Authorization'], f"Bearer {self.api_key}")

    def test_get_headers_without_api_key(self):
        graphql_api = GraphQLAPI(url=self.url)
        headers = graphql_api._get_headers()
        self.assertEqual(headers, {})

    def test_query(self):
        query = 'query { hello }'
        expected_response = {'data': {'hello': 'world'}}
        mock_client = MagicMock()
        mock_client.execute.return_value = expected_response
        self.graphql_api.client = mock_client

        response = self.graphql_api.query(query)

        self.assertEqual(response, expected_response)

    def test_query_with_variables(self):
        query = "query ($name: String!) { hello(name: $name) }"
        variables = {'name': 'John'}
        expected_response = {'data': {'hello': 'Hello John'}}
        mock_client = MagicMock()
        mock_client.execute.return_value = expected_response
        self.graphql_api.client = mock_client

        response = self.graphql_api.query(query, variables)


        self.assertEqual(response, expected_response)

if __name__ == '__main__':
    unittest.main()
