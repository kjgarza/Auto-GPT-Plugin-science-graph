import requests

class BaseAPI:

    def __init__(self):
        pass  # You can initialize any necessary attributes here

    def _get(self, url, headers=None, params=None):
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            return self._parse_response(response)
        except requests.exceptions.RequestException as e:
            raise e  # Handle the exception as needed

    def _post(self, url, headers=None, data=None, json=None):
        try:
            response = requests.post(url, headers=headers, data=data, json=json)
            response.raise_for_status()
            return self._parse_response(response)
        except requests.exceptions.RequestException as e:
            raise e  # Handle the exception as needed

    def _parse_response(self, response):
        try:
            return response.json()
        except ValueError as e:
            raise e  # Handle the exception as needed