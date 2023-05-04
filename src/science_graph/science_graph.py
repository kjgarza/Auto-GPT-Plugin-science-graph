from .api_factory import APIFactory
from . import AutoGPTPluginScienceGraph

plugin = AutoGPTPluginScienceGraph()

class ScienceGraph:
    
    def __init__(self):
        pass  # You can initialize any necessary attributes here
    
    def _search_scholarly_works(self, keyword):
        api_instance = APIFactory.create_api('graphql')
        return api_instance.query(
            """
            query ($keyword: String!) {
                works(keyword: $keyword) {
                    titles{
                      title
                    }
                    contentUrl
                    doi
                    publicationYear
                    publisher
                    descriptions{
                      description
                    }
                }
            }
            """,
            {"keyword": keyword},
        )
    
    def _search_journal_articles(self, keyword):
        api_instance = APIFactory.create_api('rest')
        return api_instance.query("works", params={"query": keyword})
        
