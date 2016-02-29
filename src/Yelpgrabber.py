'''
Program that grabs comments and amount of rating stars
off of Yelp, for my mom.

Created on Feb 25, 2016

@author: austinmatthews
'''

from BeautifulSoup import BeautifulSoup
import urllib
import urllib2
import webbrowser
import mechanize

def main():
    yelp = 'http://www.yelp.com/biz/century-theatres-rowland-plaza-novato?osq=cinemark+theatre' 
    webbrowser.open(yelp)
    

if __name__ == '__main__':
    main()
    
    