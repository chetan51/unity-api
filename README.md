# Unity API

Get your Unity application to communicate with a Python client.

# Setup

## Install Unity plugin

1. In your Unity project, import `unity-plugin/API.unitypackage`.
2. Drag the prefab from `Assets/Resources/API` into the Hierarchy.

## Install Python client

1. `cd unity-client`
2. `python setup.py install`

## Run example

1. Start proxy server: `python proxy-server/run.py`
2. (In separate console) Start the example Python client: `python unity-client/examples/echo.py`
3. Run your Unity application.

You should see data being printed to the example Python client console.

# Usage

## Sending data out of Unity into your Python client

Wherever you have data in your scripts to send, call `API.instance.SetOutput`. For example:

    API.instance.SetOutput("position.x", transform.position.x);

## Receiving data into Unity from Python client

Wherever you need to read data that you had sent from your Python client, call `API.instance.GetInput`. For example:

    object force = API.instance.GetInput("force");

## Using Python client

1. Import Fetcher: `from unity_client.fetcher import Fetcher`
2. Make an instance of `Fetcher`: `fetcher = Fetcher()`
3. In a loop, call `fetcher.sync()`

## Sending data out of your Python client into Unity

You can write to the `inputData` dictionary on your `Fetcher` instance. For example:

    fetcher.inputData["force"] = force

## Receiving data into your Python client from Unity

`fetcher.sync()` returns an `outputData` dictionary that contains data sent out from Unity.

# Parameters

Some useful parameters you can adjust:

- On the `API` prefab:
    - `Update Rate` - how quickly Unity sends data to the proxy server
    - `Run Speed` - the rate at which time passes in Unity
    - `Server URL` - the location of the proxy server (so you can run your application remotely)
