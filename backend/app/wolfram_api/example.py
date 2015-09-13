import requests

from xml.etree import ElementTree as etree

#Example input : How old is Barack Obama
#Example input_interpretation_output: "age | of Barack Obama (politician) | today"
#Example result_output: "54 years 1 month 8 days"

def query_wolfram(wolfram_input, appid = "3RQELJ-AAYLR3X3WQ", base_url='http://api.wolframalpha.com/v2/query?', headers_input = {'User-Agent':None}, pod_index_input = "1,2"):
    #making the request
    url_params = {'input':wolfram_input, 'appid':appid , 'podindex':pod_index_input} 
    r = requests.get(base_url, params=url_params, headers=headers_input)
    response = r.text.encode('ascii', 'ignore')


    #parsing the request 
    data_dict = {}
    tree = etree.fromstring(response)
    for element_1 in tree.findall('pod'):
        for item_1 in [element_2 for element_2 in list(element_1) if element_2.tag=='subpod']:
            for item_2 in [item_3 for item_3 in list(item_1) if item_3.tag=='plaintext']:
                if item_2.tag=='plaintext':
                    data_dict[element_1.get('title')] = item_2.text
    
    input_interpretation_output = "WolframAlpha couldn't intepret the query :("
    result_output = "WolframAlpha couldn't give a result"    
    try:
        input_interpretation_output = data_dict["Input interpretation"]
    except:
        pass

    input_interpretation_index = None
    input_information_index = None
    input_index = None

    try: 
        input_interpretation_index = list(data_dict.keys()).index('Input interpretation')
    except:
        input_interpretation_index = None
    try: 
        input_index = list(data_dict.keys()).index('Input')
    except:
        input_index = None    
    try:
        input_information_index = list(data_dict.keys()).index('Input information')
    except:
        input_information_index = None

    if input_interpretation_index == 0 or input_information_index == 0 or input_index == 0:
        result_output = data_dict[list(data_dict.keys())[1]]
    elif  input_interpretation_index == 0 or input_information_index == 1 or input_index == 1:
        result_output = data_dict[list(data_dict.keys())[0]]
    else:
        pass
    return input_interpretation_output, result_output
#example call 
# print query_wolfram("How old is Barack Obama")[1]
# print query_wolfram("Population of Africa")[1]
# print query_wolfram("moving from Urbana to San Francisco with a salary of $250,000")[1]
print query_wolfram("Information about Barack Obama")[1]
