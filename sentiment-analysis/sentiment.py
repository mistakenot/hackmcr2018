import os
import requests
import time

endpoint = "https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment"
subscription_key = os.environ['AZURE_TEXT_KEY']

def get_sentiment(text):
    documents = {'documents' : [
        {'id': '1', 'language': 'en', 'text': text}
    ]}
    headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
    response  = requests.post(endpoint, headers=headers, json=documents)
    json = response.json()
    if 'documents' not in json:
        print(json)
        raise ValueError('Wrong response.')
    time.sleep(2)
    sentiment = json['documents'][0]['score']
    return sentiment