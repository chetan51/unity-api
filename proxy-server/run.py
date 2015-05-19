import web
import json



urls = (
    '/reset', 'reset',
    '/sync', 'sync',
    '/crossdomain.xml', 'crossdomain',
    '/update', 'update'
)

outputData = {}
inputData = {}

timestep = 0
resetFlag = False



class reset:
  def GET(self):
    global resetFlag
    resetFlag = True
    return "Confirmed"



class sync:
  def POST(self):
    global outputData, timestep, resetFlag
    outputData = json.loads(web.input().outputData)
    outputData["timestep"] = timestep
    outputData["reset"] = resetFlag
    timestep += 1
    resetFlag = False
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