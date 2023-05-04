import unittest
from src.science_graph.api_factory import APIFactory
from src.science_graph.graphql_api import GraphQLAPI
from src.science_graph.rest_api import RestAPI

class TestAPIFactory(unittest.TestCase):

    def test_create_graphql_api(self):
        api_instance = APIFactory.create_api('graphql')
        self.assertIsInstance(api_instance, GraphQLAPI)

    def test_create_some_other_api(self):
        api_instance = APIFactory.create_api('rest')
        self.assertIsInstance(api_instance, RestAPI)

    def test_create_invalid_api(self):
        with self.assertRaises(ValueError):
            APIFactory.create_api('invalid_api')

if __name__ == '__main__':
    unittest.main()