import json
import requests

def images(query, results_per_page):      
    base_url = "https://ajax.googleapis.com/ajax/services/search/images"
    url_params = {'v':"1.0", 'rsz': results_per_page , 'q': query} 
    r = requests.get(base_url, params=url_params)
    j = json.loads(r.text)
    result_array = []
    for index in xrange(results_per_page):
        string = j["responseData"]["results"][index]["url"]
        result_array.append(string.encode("utf8"))
    return result_array

print images("Andrew Kuznetsov at Illinois", 5)
