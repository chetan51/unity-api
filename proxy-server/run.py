import web
import json



urls = (
    '/sync', 'sync',
    '/crossdomain.xml', 'crossdomain',
    '/update', 'update'
)

outputData = {}
inputData = {}

timestep = 0



class sync:
  def POST(self):
    global outputData, timestep
    outputData = json.loads(web.input().outputData)
    outputData["timestep"] = timestep
    timestep += 1
    return json.dumps(inputData)


class update:
  def POST(self):
    global inputData, timestep
    inputData = json.loads(web.input().inputData)
    return json.dumps(outputData)


class crossdomain:
  def GET(self):
    with open("crossdomain.xml") as f:
      return f.read()



if __name__ == "__main__":
  app = web.application(urls, globals())
  app.run()