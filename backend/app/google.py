import json
import requests

def images(query, results_per_page):      
    base_url = "https://ajax.googleapis.com/ajax/services/search/images"
    url_params = {'v':"1.0", 'rsz': results_per_page , 'q': query} 
    r = requests.get(base_url, params=url_params)
    j = json.loads(r.text)
    result_array = []
    for index in xrange(results_per_page):
        result_array.append(j["responseData"]["results"][index])
    return result_array
