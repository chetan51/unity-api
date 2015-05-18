import json
import time
import urllib, urllib2



class Fetcher(object):

  def __init__(self,
               url='http://localhost:8080/update'):
    self.url = url

    self.inputData = {}
    self.lastPing = time.time()

    self.timestep = -1
    self.skippedTimesteps = 0


  def sync(self):
    values = {'inputData' : json.dumps(self.inputData)}
    data = urllib.urlencode(values)
    req = urllib2.Request(self.url, data)
    response = urllib2.urlopen(req)
    outputData = json.loads(response.read())

    newTimestep = self.timestep
    if "timestep" in outputData:
      newTimestep = outputData["timestep"]

    if newTimestep == self.timestep:
      return None

    self.skippedTimesteps = newTimestep - (self.timestep + 1)

    self.lastPing = time.time()
    self.timestep = newTimestep

    return outputData
