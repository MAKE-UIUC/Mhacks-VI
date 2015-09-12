from flask import Flask, request, jsonify
from alchemyapi import AlchemyAPI
import requests
import urllib
import base64
import json

app = Flask(__name__)
alchemyapi = AlchemyAPI()

bing_api_key = ''
with open('bing_api_key.txt') as f:
    bing_api_key = f.readline().strip()
    bing_api_key = base64.b64encode(':{0}'.format(bing_api_key))
#    bing_api_key = base64.b64encode('{0}:{0}'.format(bing_api_key))

@app.route('/')
def index():
    return "Hello world!"

@app.route('/process-text', methods=['POST', 'GET'])
def process_text():
    error = None
    if request.method == 'POST':
        response = alchemyapi.keywords('text', request.form['text'], {'sentiment': 1})

        if response['status'] == 'OK':
            if len(response['keywords']) == 1:
                return jsonify(results=search_bing(response['keywords'][0]['text'], 10))
            else:
                res1 = search_bing(response['keywords'][0]['text'], 5)
                res2 = search_bing(response['keywords'][1]['text'], 5)
                results = res1 + res2
                return jsonify(results=results) 

def format_api_url(query, num):
    return 'https://api.datamarket.azure.com/Bing/Search/v1/Image?$format=json&$top={}&Query=%27{}%27&Options=%27DisableLocationDetection%27'.format(num, urllib.quote_plus(query))

def search_bing(query, num):
    url = format_api_url(query, num)
    headers = {'Authorization': 'Basic ' + bing_api_key}
    r = requests.get(url, headers=headers)
    #r = requests.get(url, auth=('', bing_api_key))
    objs = r.json()['d']['results']
    results = []
    for obj in objs:
        res = {}
        res['id'] = obj['ID']
        res['img'] = obj['MediaUrl']
        res['src'] = obj['SourceUrl']
        res['title'] = obj['Title']
        results.append(res)
    return results

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
