import web
import json



urls = (
    '/sync', 'sync',
    '/crossdomain.xml', 'crossdomain',
    '/update', 'update'
)

outputData = {}
inputData = {}
client = None



class sync:
  def POST(self):
    global outputData, timestep, resetFlag
    outputData = json.loads(web.input().outputData)
    inputData = client.sync(outputData) or {}
    return json.dumps(inputData)


class crossdomain:
  def GET(self):
    with open("crossdomain.xml") as f:
      return f.read()


class Server(object):
  def __init__(self, cl):
    global client
    client = cl
    app = web.application(urls, globals())
    app.run()