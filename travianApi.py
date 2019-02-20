import datetime
from robobrowser import RoboBrowser


class TravianApi:
    def __init__(self, user, pasw, WWVillage, serverLink, useragent):
        self.serverLink = serverLink
        self.browser = RoboBrowser(history=True,
                                   parser='html.parser',
                                   user_agent=useragent)
        self.WWVillage_Name = WWVillage
        self.browser.open(serverLink)
        self.loggin(user, pasw)

    def travianLink(self, destination=""):
        if '.php' in destination:
            return self.serverLink[:-9] + destination

        return self.serverLink + destination

    def loggin(self, user, pasw):
        self.logActions('Opening login page (%s)' % self.travianLink())
        self.browser.open(self.travianLink())

        self.logActions("Logging as '%s'" % user)
        form = self.browser.get_form(action='dorf1.php')
        form["name"] = user
        form["password"] = pasw

        self.browser.session.headers['Referer'] = self.travianLink("dorf2.php")
        self.browser.submit_form(form)

        self.logActions("Logged in successfully!")

    def openWWVillage(self):
        try:
            WWLink = self.browser.get_link(self.WWVillage_Name).get('href')
        except:
            print("Can NOT found WW Village named '"+self.WWVillage_Name+"'\nMake sure name is right.")
            exit(0)

        self.browser.open(self.travianLink(WWLink))
        self.logActions("Navigated to '%s' (%s)" % (self.WWVillage_Name, WWLink))

    def openMarketplace(self):
        link = 'build.php?t=5&id=36'
        self.browser.open(self.travianLink(link))
        self.logActions('Opened up Marketplace (%s)' % self.travianLink(link))

    def getSourcecode(self):
        self.logActions("Source code has been copied and passed")
        return self.browser.parsed

    def checkIsCurrentVillageWW(self):
        nameField = '#villageNameField'
        currentVillage = ""
        try:
            currentVillage = self.browser.select(nameField)[0].text
            isCurrVillageWW = self.WWVillage_Name in currentVillage

            self.logActions('Is current village \'%s\' => %s' % (self.WWVillage_Name, isCurrVillageWW))
        except Exception as e:
            print("Something went wrong? (ID: "+nameField+")")
            print(str(e))

        return isCurrVillageWW

    def logActions(self, action):
        print('[%s | travianAPI] %s' % (datetime.datetime.now(), action))
