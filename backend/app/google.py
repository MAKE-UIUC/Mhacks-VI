import json
import requests

key = ""
cx =""

def images(query, results_per_page):      
    base_url = "https://www.googleapis.com/customsearch/v1"
    url_params = {'searchType':"image", 'num': results_per_page , 'q': query, 'key': key, 'cx': cx} 
    r = requests.get(base_url, params=url_params)
    j = json.loads(r.text)
    result_array = []
    for index in xrange(results_per_page):
        result_array.append(j["items"][index]["link"])
    return result_array
