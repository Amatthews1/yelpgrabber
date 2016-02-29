'''
Program that grabs comments and amount of rating stars
off of Yelp, for my mom.

Created on Feb 25, 2016

@author: austinmatthews
'''

import urllib
import urllib2
from bs4 import BeautifulSou

def main():
    theatre_one = 'http://www.yelp.com/biz/century-theatres-rowland-plaza-novato?osq=rowland+theatre'
    soup = BeautifulSoup(urllib2.urlopen(theatre_one), 'html.parser')
    p_list = soup.find_all('p')

    for d in p_list:
        print d
    

if __name__ == '__main__':
    main()
    
    