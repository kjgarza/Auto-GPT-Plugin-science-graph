import json

def reduce_reponse(results):
    reduced_attributes = ['abstract', 'title', 'URL']
    reduced_results = [
        {k: d[k] for k in reduced_attributes if k in d}
        for d in results
    ]
    return reduced_results

def safe_response(results):
    safe_results = json.dumps(results, ensure_ascii=False, indent=4)
    return safe_results