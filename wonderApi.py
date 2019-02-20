import datetime

import re
from robobrowser import RoboBrowser


class WonderApi:
    global WWVillage_Name
    WWVillage_Name = "WW Village"

    def __init__(self, user, pasw, linkName):
        self.link = 'http://www.travianwonder.com/%s' % linkName
        self.browser = RoboBrowser(history=True, parser='html.parser')
        self.browser.open(self.link)
        self.loggin(user, pasw)

    def loggin(self, _user, _pasw):
        self.logActions("Logging as '%s'" % _user)
        self.browser.open(self.link + "/admin")

        form = self.browser.get_form(id='loginForm')
        # print(form)
        form['user'] = _user
        form['password'] = _pasw

        # self.browser.session.headers['Referer'] = self.link
        self.browser.submit_form(form)

        self.logActions("Logged in successfully!")

    def updateResources(self, source):
        self.logActions('Prepare update resources')

        resourceLink = self.link + "/resources"
        self.browser.open(resourceLink)

        try:
            form = self.browser.get_form(id='resourcesForm')
            form['htmlCode'].value = str(source)
            # form['htmlCodeFile'].value = open(filename, 'rb')
            # print(form)

            self.browser.submit_form(form)
            self.logActions("Resource update request has been send!")
            return True
        except Exception as e:
            print("Something went wrong when try update resources")
            print(str(e))
        return False

    def updateResourcesReq(self):
        self.logActions('Prepare update resources')
        filename = "C:\\Users\\Root\\AppData\\Local\\Temp\\travian.html"

        resourceLink = self.link + "/resources"
        try:
            self.browser.open(resourceLink, method='post', data={'htmlCode': '',
                                                                 'htmlCodeFile': open(filename, 'rb'),
                                                                 'submitBtn': '  TALLENNA  '})
        except Exception as e:
            print(str(e))


    def logActions(self, action):
        print('[%s | wonderAPI] %s' % (datetime.datetime.now(), action))
