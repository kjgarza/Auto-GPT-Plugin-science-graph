from .graphql_api import GraphQLAPI
from .rest_api import RestAPI
import config

class APIFactory:

    @staticmethod
    def create_api(api_type):
        if api_type == 'graphql':
            return GraphQLAPI(url=config.packg_config['pid_graph_api']['base_url'])
        elif api_type == 'rest':
            return RestAPI(base_url=config.packg_config['crossref_api']['base_url'])
        else:
            raise ValueError(f"Unsupported API type: {api_type}")