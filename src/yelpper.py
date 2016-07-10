''' 
Trying to get theatre output to work

'''


import urllib
import urllib2
from bs4 import BeautifulSoup



class TheatrePage(object):
    def __init__(self, url):
        self.name     = None
        self.page_url = url
        self.id       = None
        self.dates    = []

    def get_dates(self):
        soup = BeautifulSoup(urllib2.urlopen(self.page_url), 'html.parser')
        comment_date = soup('span', {"class":"rating-qualifier"})     # find and return a list of dates for each comment? (need to verify)

        for d in comment_date:
            if d.find("meta"):
                self.dates.append(d.find("meta")["content"])

        return self.dates