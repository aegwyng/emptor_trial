import json
from botocore.vendored import requests
from bs4 import BeautifulSoup

import boto3
#import StringIO

def save_to_s3(bucket_ref, file, data):
    s3 = boto3.resource('s3')
    obj = s3.Object(bucket_ref, file)
    obj.put(Body=json.dumps(data))

def hello(event, context):

    if event.get('url'):
        url = event.get('url')
    else:
        return json.dumps({ 'error' : '\'url\' parameter is required as part of event dictionary.'})

    response = requests.get(url, json={'key': 'value'})
    response.encoding = 'utf-8'
    seach_key = 'title'
    soup = BeautifulSoup(response.text, "html.parser")
    tags = soup.findAll(seach_key)

    body = {
        "url": url,
        "title": str(tags)
    }

    # saving to s3
    #output = StringIO.StringIO()
    output = ''
    for k, v in body.items():
        #output.write(k + ' : ' + v + '.\n')
        output += k + ' : ' + v + '.\n'

    save_to_s3('bucket.test.ale',url,output)


    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
