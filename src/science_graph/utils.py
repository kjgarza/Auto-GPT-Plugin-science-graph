import json

def reduce_reponse(results):
    reduced_attributes = ['abstract', 'title', 'URL']
    reduced_results = [
        {k: d[k] for k in reduced_attributes if k in d}
        for d in results
    ]
    return flatted_rest_response(reduced_results)

def safe_response(results):
    return json.dumps(results, ensure_ascii=False, indent=4)

def flatted_rest_response(results):
    flattened_results = [
        {
            'title': d.get('title',[''])[0],
            'href': d.get('URL',''),
            'body': d.get('abstract','').replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').strip()
        }
        for d in results
    ]
    return flattened_results


def flatted_graphql_response(results):
    flattened_results = [
        {
            'title': d.get('titles',[''])[0].get('title',''),
            'contentUrl': d.get('contentUrl',''),
            'href': "https://doi.org/{doi}".format(doi=d.get('doi','')),
            'publicationYear': d.get('publicationYear',''),
            'publisher': d.get('publisher',''),
            'body': d.get('descriptions',[''])[0].get('description','').replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').strip()
        }
        for d in results
    ]
    return flattened_results
