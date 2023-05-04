import requests
from .base_api import BaseAPI

class RestAPI(BaseAPI):

    def __init__(self, base_url, api_key=None):
        super().__init__()
        self.base_url = base_url
        self.api_key = api_key

    def _get_headers(self):
        headers = {}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        return headers

    def query(self, path, params=None):
        url = self.base_url + path
        try:
            response = self._get(url, headers=self._get_headers(), params=params)
            return response
        except requests.exceptions.RequestException as e:
            raise e  # Handle the exception as needed


    # Implement PUT, DELETE, and any additional utility methods

