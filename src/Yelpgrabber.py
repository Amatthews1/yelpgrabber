'''
Program that grabs comments and amount of rating stars
off of Yelp, for my mom.

Created on Feb 25, 2016

@author: mishasawangwan and austinmatthews
'''

import urllib
import urllib2
from bs4 import BeautifulSoup

def main():
    theatre_one = 'http://www.yelp.com/biz/century-theatres-rowland-plaza-novato?osq=rowland+theatre'
    soup = BeautifulSoup(urllib2.urlopen(theatre_one), 'html.parser')
    
    desc_list = soup('p', {"itemprop":"description"})
    user_name = soup('a', {"class":"user-display-name"})
    ratings = soup('meta', {"itemprop":"ratingValue" })
    
    u_name_and_review_list = []
    rating_list = []
    
    for user, review in zip(user_name, desc_list):
        u_name_and_review_list.append('[' + user.text + ']' + '-- ' + review.text + '\n')
        
    for rating in ratings:
        extracted_rating = rating["content"]
        rating_list.append(extracted_rating)
        
    for c, d in zip(u_name_and_review_list, rating_list):
        print 'Rating of [', d, '] by user', c + "\n"
    


    

if __name__ == '__main__':
    main()
    
    