import requests
import json

myurl = "http://neuralmechanics.ai/analitika/nlp/ner/"
body = {'data': blob}

r = requests.post(myurl, auth=('nmdev', 'nmdev'), verify=True, json=body)

json.loads(r.content)
