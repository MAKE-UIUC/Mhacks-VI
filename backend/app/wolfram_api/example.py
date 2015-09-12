import requests
from xml.etree import ElementTree as etree

#Example input : How old is Barack Obama
#Example input_interpretation_output: "age | of Barack Obama (politician) | today"
#Example result_output: "54 years 1 month 8 days"

def query_wolfram(wolfram_input, appid = "3RQELJ-AAYLR3X3WQ", base_url='http://api.wolframalpha.com/v2/query?', headers_input = {'User-Agent':None}):
    #making the request
    url_params = {'input':wolfram_input, 'appid':appid} 
    r = requests.get(base_url, params=url_params, headers=headers_input)
    #parsing the request 
    data_dict = {}
    tree = etree.fromstring(r.text)
    for element_1 in tree.findall('pod'):
        for item_1 in [element_2 for element_2 in list(element_1) if element_2.tag=='subpod']:
            for item_2 in [item_3 for item_3 in list(item_1) if item_3.tag=='plaintext']:
                if item_2.tag=='plaintext':
                    data_dict[element_1.get('title')] = item_2.text
    input_interpretation_output = data_dict["Input interpretation"]
    result_output = data_dict["Result"]

    print input_interpretation_output
    print result_output

#example call 
query_wolfram("How old is Barack Obama")
