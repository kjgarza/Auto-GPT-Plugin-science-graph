import requests
from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport
from .base_api import BaseAPI

class GraphQLAPI(BaseAPI):

    def __init__(self, url, api_key=None):
        super().__init__()
        self.url = url
        self.api_key = api_key
        self.transport = RequestsHTTPTransport(url=self.url, headers=self._get_headers())
        self.client = Client(transport=self.transport, fetch_schema_from_transport=True)

    def _get_headers(self):
        headers = {}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        return headers

    def query(self, query, variables=None):
        query = gql(query)
        try:
            response = self.client.execute(query, variable_values=variables)
            return response
        except Exception as e:
            raise e  # Handle the exception as needed

    # Add any additional utility methods needed for the GraphQL API class
