import urllib.request
import json

body = {'data': 'hello world!'}

myurl = "http://127.0.0.1:3000/nlp/sentiment"
req = urllib.request.Request(myurl)

req.add_header('Content-Type', 'application/json; charset=utf-8')
jsondata = json.dumps(body)
jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
req.add_header('Content-Length', len(jsondataasbytes))

print (jsondataasbytes)
response = urllib.request.urlopen(req, jsondataasbytes)
response