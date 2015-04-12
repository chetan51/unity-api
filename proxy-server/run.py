import web
import json



urls = (
    '/init', 'init',
    '/sync', 'sync',
    '/crossdomain.xml', 'crossdomain'
)

outputNames = []
outputTypes = []
inputNames = []
inputTypes = []

outputData = {}
inputData = {}



class init:
  def POST(self):
    outputNames = json.loads(web.input().outputNames)
    outputTypes = json.loads(web.input().outputTypes)
    inputNames = json.loads(web.input().outputNames)
    inputTypes = json.loads(web.input().outputTypes)



class sync:
  def POST(self):
    outputData = json.loads(web.input().outputData)
    return json.dumps(inputData)



class crossdomain:
  def GET(self):
    with open("crossdomain.xml") as f:
      return f.read()



if __name__ == "__main__":
  app = web.application(urls, globals())
  app.run()