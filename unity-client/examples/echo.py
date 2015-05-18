from unity_client.fetcher import Fetcher


def run():
  fetcher = Fetcher()

  while True:
    outputData = fetcher.sync()

    if outputData is None:
      continue

    print "Timestep: {0}".format(fetcher.timestep)
    print outputData

    if fetcher.skippedTimesteps > 0:
      print ("Warning: skipped {0} timesteps, "
             "now at {1}").format(fetcher.skippedTimesteps, fetcher.timestep)

    if outputData["reset"]:
      print "Reset."

    print "============"



run()
