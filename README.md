# pyWebsocketJsonCommunicationPue5

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

An example showing how to connect and communicate with a PUE 5 scale using WebSocket and Json.


# Technology
The repository contains sample project written in the Python.
Sample using liblaries:
* WebSocket client library for Python.
* Json library for Python.

# Working description
After connecting to the scale, you can read the current weight from the currently set platform,
You can also taring and zeroing the current platform. 
Additional controls located on the left side of the panel show the stability of the result and whether the scale is tared, zeroed.

The available options are in the app:
* Taring
* Zeroing
* Changing active platform
* Listing mass from active platform.

# Commands
* {'COMMAND': 'REGISTER_LISTENER', 'PARAM': 'MOD_INFO'} - this command registers the listener on the device which responds with the MOD_INFO command to the connected client automatically after each update of the device data, e.g. weight or time.
* {'COMMAND': 'EXECUTE_ACTION', 'PARAM': 'ActionChangePlatform'} - this command changes the platform.
* {'COMMAND': 'EXECUTE_ACTION', 'PARAM': 'ActionTarring'} - this command tarring the active platform.
* {'COMMAND': 'EXECUTE_ACTION', 'PARAM': 'ActionZeroing'} - this command zeroing the active platform.

# Structure of the MOD_INFO response
![image](https://user-images.githubusercontent.com/46632727/163121941-61360188-f4c5-4ad8-98c6-4c78a6076423.png)
![image](https://user-images.githubusercontent.com/46632727/163122054-aa663e43-6854-4c12-bb61-ebd5b4144f02.png)

# Installation
1. Clone or download this repository.
2. Open project in JestBrains PyCharm.
3. Build and run.

[contributors-shield]: https://img.shields.io/github/contributors/Radwag/pyWebsocketJsonCommunicationPue5.svg?style=for-the-badge
[contributors-url]: https://github.com/Radwag/pyWebsocketJsonCommunicationPue5/contributors
[forks-shield]: https://img.shields.io/github/forks/Radwag/pyWebsocketJsonCommunicationPue5.svg?style=for-the-badge
[forks-url]: https://github.com/Radwag/pyWebsocketJsonCommunicationPue5/network/members
[stars-shield]: https://img.shields.io/github/stars/Radwag/pyWebsocketJsonCommunicationPue5.svg?style=for-the-badge
[stars-url]: https://github.com/Radwag/pyWebsocketJsonCommunicationPue5/stargazers
[issues-shield]: https://img.shields.io/github/issues/Radwag/pyWebsocketJsonCommunicationPue5.svg?style=for-the-badge
[issues-url]: https://github.com/Radwag/pyWebsocketJsonCommunicationPue5/issues
