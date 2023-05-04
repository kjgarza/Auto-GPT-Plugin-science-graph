from .api_factory import APIFactory
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
                        titles {
                            title
                        }
                        contentUrl
                        doi
                        publicationYear
                        publisher
                        descriptions {
                            description
                        }
                    }
                }
            }
            """,
            {"keyword": keyword},
        )
        return json.dumps(response)
    
    def _search_journal_articles(self, keyword):
        api_instance = APIFactory.create_api('rest')
        response = api_instance.query("works", params={"query": keyword})
        return json.dumps(response)

        
