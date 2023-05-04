from .graphql_api import GraphQLAPI
from .rest_api import RestAPI
# import settings as config

class APIFactory:

    @staticmethod
    def create_api(api_type):
        if api_type == 'graphql':
            return GraphQLAPI(url="https://api.datacite.org/graphql")
        elif api_type == 'rest':
            return RestAPI(base_url="https://api.crossref.org/")
        else:
            raise ValueError(f"Unsupported API type: {api_type}")