# TravianWonder Tool
This is a tool for http://www.travianwonder.com/ Travian World Wonder crop website.
Script login to Travian account, navigate to World Wonder village and open up the market. After that it copy source code of incoming trades and passes them to Travianwonder website.

You need **Python 3.6 or higher** to run it.

![Tool preview](https://i.imgur.com/Ov1qOBT.png)

# Installation
1. Open terminal and navigate to ``TravianWonder`` folder
2. ``pip3 install -r requirements.txt``
3. ``python3 main.py``

# Config.ini
Here is brief information for each section inside the ``./config.ini``
```ini
[Travian]
username=<Travian Username>
password=<Travian Password>
linkToDorf2=<https://link to dorf2.php>
WWVillageName=<World Wonder village name>

[Wonder]
username=<Travianwonder.com Username>
password=<Travianwonder.com Password>
cropToolName=<Only Crop tool name here>

[General]
userAgent=<Google "What is my useragent" and use it here>
minDelay=<After task completed, sleep X amount of range. Minimum value in seconds>
maxDelay=<After task completed, sleep X amount of range. Maximum value in seconds>

[Nightmode]
nightEnabled=[True|False] <Night time update less often then daytime>
nightDelayMultiplier=<Multiplier value for minDelay and maxDelay. Number only>
nightStartAt=<When night start. Hour number here>
nightEndAt=<When night end at next day. Hour number here>
```
