import requests
import json

myurl = "http://neuralmechanics.ai/analitika/nlp/sentiment/"
body = {'data': 'Ang pangit mo hahaha'}

r = requests.post(myurl, auth=('nmdev', 'nmdev'), verify=True, json=body)

json.loads(r.content)
