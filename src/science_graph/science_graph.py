from .api_factory import APIFactory
from .utils import reduce_reponse, safe_response, flatted_graphql_response
import requests

from . import AutoGPTPluginScienceGraph

plugin = AutoGPTPluginScienceGraph()

class ScienceGraph:
    
    def __init__(self):
        pass  # You can initialize any necessary attributes here
    
    def _search_scholarly_works(self, keyword: str):
        """Search any type of scholarly works by query
        Args:
            keyword (str): The keyword to search
        Returns:
            str: The response from the search in JSON format
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
        return safe_response(flatted_graphql_response(response['works']['nodes']))
    
    def _search_journal_articles(self, keyword: str):
        """Search journal articles by query
        Args:
            keyword (str): The keyword to search
        Returns:
                str: The response from the search in JSON format
        """
        api_instance = APIFactory.create_api('rest')
        response = api_instance.query("works", params={"query.description": keyword})
        return safe_response(reduce_reponse(response['message']['items']))


    def _get_article_or_work(self, href: str):
        """Return the results of a href resolved

        Args:
            href (str): The href to scrape

        Returns:
            str or list: The response from the page
        """
        try:
            response = requests.get(href)
            return response.text
        except requests.exceptions.RequestException as e:
            raise e
        