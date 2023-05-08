import json
from jinja2 import Template

def reduce_reponse(results: list):
    reduced_attributes = ['abstract', 'title', 'URL']
    reduced_results = [
        {k: d[k] for k in reduced_attributes if k in d}
        for d in results
    ]
    return flatted_rest_response(reduced_results)

def safe_json_response(results):
    return json.dumps(results, ensure_ascii=False, indent=4)

def flatted_rest_response(results: list):
    flattened_results = [
        {
            'title': d.get('title',[''])[0],
            'url': d.get('URL',''),
            'abstract': d.get('abstract','').replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').strip()
        }
        for d in results
    ]
    return flattened_results


def flatted_graphql_response(results: list):
    flattened_results = [
        {
            'title': d.get('titles',[''])[0].get('title',''),
            'contentUrl': d.get('contentUrl',''),
            'url': "https://doi.org/{doi}".format(doi=d.get('doi','')),
            'publicationYear': d.get('publicationYear',''),
            'publisher': d.get('publisher',''),
            'abstract': d.get('descriptions',[''])[0].get('description','').replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').strip()
        }
        for d in results
    ]
    return flattened_results

def templated_response(results: list):

    jinja_string = """{{title}}:
    Total results: {{ results|length }}
    {% for result in results %}
    Title: {{ result.title }}
    Abstract: {{ result.abstract }}
    Url: {{ result.url }}
    {% endfor %}

    These results include the following fields: title, Abstract, and url. You can use url to get more information about the result. For example, you can use url to get the result's full text and to reference the result in your own work.
    """

    template = Template(jinja_string)

    return template.render(title="Search Results", results=results)


def format_response(results: list, format: str):
    if format == 'json':
        return safe_json_response(results)
    elif format == 'text':
        return templated_response(results)
    else:
        return templated_response(results)