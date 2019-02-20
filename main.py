import configparser
import random
import time

from datetime import datetime
from datetime import timedelta

from travianApi import TravianApi
from wonderApi import WonderApi

global config
config = configparser.ConfigParser()


def main():
    updated = False
    while True is True:
        travian = TravianApi(config['Travian']['username'],
                             config['Travian']['password'],
                             config['Travian']['WWVillageName'],
                             config['Travian']['linkToDorf2'],
                             config['General']['userAgent'])

        loopWWVillage(travian)
        travian.openMarketplace()

        if travian.checkIsCurrentVillageWW():
            source = travian.getSourcecode()

            wonder = WonderApi(config['Wonder']['username'],
                               config['Wonder']['password'],
                               config['Wonder']['cropToolName'])

            updated = wonder.updateResources(source)

        # Task run every 15 minutes. (900)
        if updated:
            min = int(config['General']['minDelay'])
            max = int(config['General']['maxDelay'])

            if checkNightmode():
                wonder.logActions("[Nightmode] Night detected!")
                min *= int(config['Nightmode']['nightDelayMultiplier'])
                max *= int(config['Nightmode']['nightDelayMultiplier'])

            randomSleep = random.randint(min, max)
            print("Done! Now let me sleep for " + str(randomSleep / 60) + " min ... Next update at "
                  + str(datetime.now() + timedelta(seconds=randomSleep)))

            time.sleep(randomSleep)
            updated = False


def loopWWVillage(travian):
    while not travian.checkIsCurrentVillageWW():
        travian.openWWVillage()


def checkNightmode():
    start = datetime(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day,
                     hour=int(config['Nightmode']['nightStartAt']), minute=0, second=0)
    end = datetime(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day+1,
                   hour=int(config['Nightmode']['nightEndAt']), minute=0, second=0)
    curr = datetime.now()
    return config['Nightmode']['nightEnabled'] in ['True', 'true'] and (start <= curr <= end)


if __name__ == "__main__":
    config.read('config.ini')
    main()
