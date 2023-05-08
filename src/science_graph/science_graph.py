from .api_factory import APIFactory
from .utils import reduce_reponse, flatted_graphql_response, format_response
import requests

from . import AutoGPTPluginScienceGraph

plugin = AutoGPTPluginScienceGraph()

class ScienceGraph:
    
    def __init__(self):
        pass  # You can initialize any necessary attributes here
    
    def _search_scholarly_works(self, keyword: str, format: str = "text"):
        """Search any type of scholarly works by query
        Args:
            keyword (str): The keyword to search
        Returns:
            The response from the search 
        """
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
        return format_response(flatted_graphql_response(response['works']['nodes']),format=format)
    
    def _search_journal_articles(self, keyword: str,format=format):
        """Search journal articles by query
        Args:
            keyword (str): The keyword to search
        Returns:
            The response from the search 
        """
        api_instance = APIFactory.create_api('rest')
        response = api_instance.query("works", params={"query": keyword})
        return format_response(reduce_reponse(response['message']['items']),format=format)


    def _get_article_or_work(self, url: str):
        """Return the results of a href resolved

        Args:
            url (str): The href to scrape

        Returns:
            The response from the page
        """
        try:
            response = requests.get(url)
            return response.text
        except requests.exceptions.RequestException as e:
            raise e
        