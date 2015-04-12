import urllib
import urllib2
import json



url = 'http://localhost:8080/update'
inputData = {}



while True:
  values = {'inputData' : json.dumps(inputData)}
  data = urllib.urlencode(values)
  req = urllib2.Request(url, data)
  response = urllib2.urlopen(req)
  outputData = json.loads(response.read())

  inputData = {}
  if 'position' in outputData:
    inputData['position'] = outputData['position']
