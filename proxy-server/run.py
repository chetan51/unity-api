import web
import json



urls = (
    '/init', 'init',
    '/sync', 'sync',
    '/crossdomain.xml', 'crossdomain',
    '/update', 'update'
)

outputNames = []
outputTypes = []
inputNames = []
inputTypes = []

outputData = {}
inputData = {}



class init:
  def POST(self):
    global outputNames, outputTypes, inputNames, inputTypes
    outputNames = json.loads(web.input().outputNames)
    outputTypes = json.loads(web.input().outputTypes)
    inputNames = json.loads(web.input().outputNames)
    inputTypes = json.loads(web.input().outputTypes)



class sync:
  def POST(self):
    global outputData
    outputData = json.loads(web.input().outputData)
    print inputData
    return json.dumps(inputData)


class update:
  def POST(self):
    global inputData
    inputData = json.loads(web.input().inputData)
    return json.dumps(outputData)


class crossdomain:
  def GET(self):
    with open("crossdomain.xml") as f:
      return f.read()



if __name__ == "__main__":
  app = web.application(urls, globals())
  app.run()