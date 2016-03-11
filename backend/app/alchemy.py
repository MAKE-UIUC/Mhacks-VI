import json
import requests

key = ""

def entities(text):      
    base_url = "http://access.alchemyapi.com/calls/text/TextGetRankedNamedEntities"
    url_params = {'sentiment': 0, 'apikey': key , 'outputMode': "json", 'text': text} 
    r = requests.get(base_url, params=url_params)
    j = json.loads(r.text)
    # print j
    result_array = []
    for indx, entities in enumerate(j["entities"]):
    	result_array.append(str(j["entities"][indx]["text"]))
    return result_array
