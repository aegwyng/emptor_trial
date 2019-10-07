import json
import requests
from bs4 import BeautifulSoup

def hello(event, context):

    if event.get('url'):
        url = event.get('url')#'https://animeflv.net'
    else:
        return json.dumps({ 'error' : '\'url\' parameter is required as part of event dictionary.'})

    response = requests.get(url, json={'key': 'value'})
    response.encoding = 'utf-8'
    seach_key = 'title'
    soup = BeautifulSoup(response.text, "html.parser")
    tags = soup.findAll(seach_key)

    body = {
        "url": url,
        "title": tags
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


print(hello({'url' : 'https://animeflv.net'},''))