from .api_factory import APIFactory
from .utils import reduce_reponse, safe_response
import json
from . import AutoGPTPluginScienceGraph

plugin = AutoGPTPluginScienceGraph()

class ScienceGraph:
    
    def __init__(self):
        pass  # You can initialize any necessary attributes here
    
    def _search_scholarly_works(self, keyword):
        api_instance = APIFactory.create_api('graphql')
        response = api_instance.query(
            """
            query ($keyword: String!) {
                works(query: $keyword) {
                    nodes {
                        titles(first: 1) {
                            title
                        }
                        contentUrl
                        doi
                        publicationYear
                        publisher
                        descriptions(first: 1) {
                            description
                        }
                    }
                }
            }
            """,
            {"keyword": keyword},
        )
        return safe_response(response['works']['nodes'])
    
    def _search_journal_articles(self, keyword):
        api_instance = APIFactory.create_api('rest')
        response = api_instance.query("works", params={"query": keyword})
        return safe_response(reduce_reponse(response['message']['items']))
