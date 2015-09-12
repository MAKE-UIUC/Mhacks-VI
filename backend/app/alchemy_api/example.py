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
print('############################################')
print('#   Entity Extraction                      #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.entities('text', demo_text, {'sentiment': 1})

if response['status'] == 'OK':
    response['usage'] = ''
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Entities ##')
    for entity in response['entities']:
        print('text: ', entity['text'].encode('utf-8'))
        print('type: ', entity['type'])
        print('relevance: ', entity['relevance'])
        print('sentiment: ', entity['sentiment']['type'])
        if 'score' in entity['sentiment']:
            print('sentiment score: ' + entity['sentiment']['score'])
        print('')
else:
    print('Error in entity extraction call: ', response['statusInfo'])


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
    response['usage'] = ''
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


print('')
print('')
print('')
print('############################################')
print('#   Concept Tagging                        #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.concepts('text', demo_text)

if response['status'] == 'OK':
    response['usage'] = ''
    print('## Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Concepts ##')
    for concept in response['concepts']:
        print('text: ', concept['text'])
        print('relevance: ', concept['relevance'])
        print('')
else:
    print('Error in concept tagging call: ', response['statusInfo'])


print('')
print('')
print('')
print('############################################')
print('#   Sentiment Analysis                     #')
print('############################################')
print('')
print('')

print('Processing html: ', demo_html)
print('')

response = alchemyapi.sentiment('html', demo_html)

if response['status'] == 'OK':
    response['usage'] = ''
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Document Sentiment ##')
    print('type: ', response['docSentiment']['type'])

    if 'score' in response['docSentiment']:
        print('score: ', response['docSentiment']['score'])
else:
    print('Error in sentiment analysis call: ', response['statusInfo'])


print('')
print('')
print('')
print('############################################')
print('#   Targeted Sentiment Analysis            #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.sentiment_targeted('text', demo_text, 'Denver')

if response['status'] == 'OK':
    response['usage'] = ''
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Targeted Sentiment ##')
    print('type: ', response['docSentiment']['type'])

    if 'score' in response['docSentiment']:
        print('score: ', response['docSentiment']['score'])
else:
    print('Error in targeted sentiment analysis call: ',
          response['statusInfo'])


print('')
print('')
print('')
print('############################################')
print('#   Text Extraction                        #')
print('############################################')
print('')
print('')

print('Processing url: ', demo_url)
print('')

response = alchemyapi.text('url', demo_url)

if response['status'] == 'OK':
    response['usage'] = ''
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Text ##')
    print('text: ', response['text'].encode('utf-8'))
    print('')
else:
    print('Error in text extraction call: ', response['statusInfo'])


print('')
print('')
print('')
print('############################################')
print('#   Author Extraction                      #')
print('############################################')
print('')
print('')

print('Processing url: ', demo_url)
print('')

response = alchemyapi.author('url', demo_url)

if response['status'] == 'OK':
    response['usage'] = ''
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Author ##')
    print('author: ', response['author'].encode('utf-8'))
    print('')
else:
    print('Error in author extraction call: ', response['statusInfo'])


print('')
print('')
print('')
print('############################################')
print('#   Language Detection                     #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.language('text', demo_text)

if response['status'] == 'OK':
    response['usage'] = ''
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Language ##')
    print('language: ', response['language'])
    print('iso-639-1: ', response['iso-639-1'])
    print('native speakers: ', response['native-speakers'])
    print('')
else:
    print('Error in language detection call: ', response['statusInfo'])


print('')
print('')
print('')
print('############################################')
print('#   Title Extraction                       #')
print('############################################')
print('')
print('')

print('Processing url: ', demo_url)
print('')

response = alchemyapi.title('url', demo_url)

if response['status'] == 'OK':
    response['usage'] = ''
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Title ##')
    print('title: ', response['title'].encode('utf-8'))
    print('')
else:
    print('Error in title extraction call: ', response['statusInfo'])


print('')
print('')
print('')
print('############################################')
print('#   Relation Extraction                    #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.relations('text', demo_text)

if response['status'] == 'OK':
    response['usage'] = ''
    print('## Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Relations ##')
    for relation in response['relations']:
        if 'subject' in relation:
            print('Subject: ', relation['subject']['text'].encode('utf-8'))

        if 'action' in relation:
            print('Action: ', relation['action']['text'].encode('utf-8'))

        if 'object' in relation:
            print('Object: ', relation['object']['text'].encode('utf-8'))

        print('')
else:
    print('Error in relation extaction call: ', response['statusInfo'])


print('')
print('')
print('')
print('############################################')
print('#   Text Categorization                    #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.category('text', demo_text)

if response['status'] == 'OK':
    response['usage'] = ''
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Category ##')
    print('text: ', response['category'])
    print('score: ', response['score'])
    print('')
else:
    print('Error in text categorization call: ', response['statusInfo'])


print('')
print('')
print('')
print('############################################')
print('#   Feed Detection                         #')
print('############################################')
print('')
print('')

print('Processing url: ', demo_url)
print('')

response = alchemyapi.feeds('url', demo_url)

if response['status'] == 'OK':
    response['usage'] = ''
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Feeds ##')
    for feed in response['feeds']:
        print('feed: ', feed['feed'])
else:
    print('Error in feed detection call: ', response['statusInfo'])

print('')
print('')


print('')
print('')
print('')
print('############################################')
print('#   Microformats Parsing                   #')
print('############################################')
print('')
print('')

print('Processing url: ', demo_url)
print('')

response = alchemyapi.microformats('url', demo_url)

if response['status'] == 'OK':
    response['usage'] = ''
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Microformats ##')
    for microformat in response['microformats']:
        print('Field: ', microformat['field'].encode('utf-8'))
        print('Data: ', microformat['data'])
        print('')

else:
    print('Error in microformats parsing call: ', response['statusInfo'])

print('')
print('')


print('')
print('')
print('')
print('############################################')
print('#   Image Extraction                       #')
print('############################################')
print('')
print('')

print('Processing url: ', demo_url)
print('')

response = alchemyapi.imageExtraction('url', demo_url)

if response['status'] == 'OK':
    response['usage'] = ''
    print('## Response Object ##')
    response['usage'] = ''
    print(json.dumps(response, indent=4))
    print('')
    print('## Image ##')
    print('Image: ', response['image'])
    print('')

else:
    print('Error in image extraction call: ', response['statusInfo'])

print('')
print('')


print('')
print('')
print('')
print('############################################')
print('#   Image tagging                          #')
print('############################################')
print('')
print('')

print('Processing url: ', image_url)
print('')

response = alchemyapi.imageTagging('url', image_url)

if response['status'] == 'OK':
    response['usage'] = ''
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Keywords ##')
    for keyword in response['imageKeywords']:
        print(keyword['text'], ' : ', keyword['score'])
    print('')
else:
    print('Error in image tagging call: ', response['statusInfo'])

print('')
print('')


print('')
print('')
print('')
print('############################################')
print('#   Taxonomy                               #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.taxonomy('text', demo_text)

if response['status'] == 'OK':
    response['usage'] = ''
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Categories ##')
    for category in response['taxonomy']:
        print(category['label'], ' : ', category['score'])
    print('')

else:
    print('Error in taxonomy call: ', response['statusInfo'])

print('')
print('')


print('')
print('')
print('')
print('############################################')
print('#   Combined                               #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.combined('text', demo_text)

if response['status'] == 'OK':
    response['usage'] = ''
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

    print('')

    print('## Keywords ##')
    for keyword in response['keywords']:
        print(keyword['text'], ' : ', keyword['relevance'])
    print('')

    print('## Concepts ##')
    for concept in response['concepts']:
        print(concept['text'], ' : ', concept['relevance'])
    print('')

    print('## Entities ##')
    for entity in response['entities']:
        print(entity['type'], ' : ', entity['text'], ', ', entity['relevance'])
    print(' ')

else:
    print('Error in combined call: ', response['statusInfo'])

print('')
print('')
