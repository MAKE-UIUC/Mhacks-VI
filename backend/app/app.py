from flask import Flask, request, jsonify
from alchemyapi import AlchemyAPI
from wolframapi import query_wolfram
from google import images
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

past_results = {}

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

@app.route('/process-keyword', methods=['POST', 'GET'])
def process_keyword():
    error = None
    if request.method == 'POST':
        print request.form['text']
        ret = search_google(request.form['text'], 1)
        w = query_wolfram(request.form['text'])[1]
        for r in ret:
            r['wolfram'] = w
        print ret
        return jsonify(results=ret)

@app.route('/pick-image', methods=['POST', 'GET'])
def pick_image():
    error = None
    if request.method == 'POST':
        if request.form['id'] in past_results:
            return jsonify(results=past_results[request.form['id']])
        else:
            return 'fail'

def format_api_url(query, num):
    return 'https://api.datamarket.azure.com/Bing/Search/v1/Image?$format=json&$top={}&Query=%27{}%27&Options=%27DisableLocationDetection%27'.format(num, urllib.quote_plus(query))

def search_google(query, num):
    imgs = images(query, num)
    ret = []
    for obj in imgs:
        res = {}
        res['id'] = obj['imageId']
        res['img'] = obj['unescapedUrl']
        res['src'] = obj['originalContextUrl']
        res['title'] = obj['title']
        ret.append(res)
    return ret

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
        past_results[res['id']] = res
    return results

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
