#!/usr/bin/env python
from alchemyapi import AlchemyAPI
import json


demo_text = 'Five cornfields were randomly selected in each county and within each field, 100 consecutive whorl-stage plants were sampled for any signs of whorl feeding or the presence of European corn borer larvae. An action site was sampled for European corn borer moths near each field by making 100 sweeps with a standard insect sweep net. We characterized action sites as dense stands of tall grasses in roadside ditches or nearby waterways. Within these action sites moths congregate and mating occurs.'
demo_url = 'http://www.refinery29.com/2015/09/93665/apple-keynote-iphone-6s-6s-plus#.hlxatb:YdSn'
demo_html = '<html><head><title>HTML | PARSING</title></head><body><h1>PARSE HERE</h1><p>PARSE HERE</p></body></html>'
image_url = 'http://s1.r29static.com//bin/entry/1ae/x/1473886/image.png'


# Create the AlchemyAPI Object
alchemyapi = AlchemyAPI()

print('')
print('')
print('')
print('############################################')
print('#   Keyword Extraction                     #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.keywords('text', demo_text, {'sentiment': 1})

if response['status'] == 'OK':
    #response['usage'] = ''
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Keywords ##')
    for keyword in response['keywords']:
        print('text: ', keyword['text'].encode('utf-8'))
        print('relevance: ', keyword['relevance'])
        print('sentiment: ', keyword['sentiment']['type'])
        if 'score' in keyword['sentiment']:
            print('sentiment score: ' + keyword['sentiment']['score'])
        print('')
else:
    print('Error in keyword extaction call: ', response['statusInfo'])
