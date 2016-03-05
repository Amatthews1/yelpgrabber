'''
Program that grabs comments and amount of rating stars
off of Yelp, for my mom.

Created on Feb 25, 2016

@author: mishasawangwan and austinmatthews
'''

import urllib
import urllib2
from bs4 import BeautifulSoup

# things to add: 1. add dates for all comments 
# then we need to add the rest of the theaters.

def main():
    theatre_one = 'http://www.yelp.com/biz/century-theatres-rowland-plaza-novato?osq=rowland+theatre' # page to scrap reviews and ratings from
    soup = BeautifulSoup(urllib2.urlopen(theatre_one), 'html.parser')                                 # parse html using beautiful soup  
    
    # using the format 'tag', {'attribute', 'attribute-name'} we can find specific html elements on the page
    #theatre_name = soup('h1', {"itemprop":"name"})
    desc_list = soup('p', {"itemprop":"description"})     # creates a list of all the reviews on the page
    user_name = soup('a', {"class":"user-display-name"})  # creates a list of all the user names on the page
    overall_rate = soup('div', {"itemprop":"aggregateRating"})
    user_meta = soup('div', {"itemprop":"review" })       # creates a list of all the ratings on the page
    comment_date = soup('span', {"class":"rating-qualifier"})
    
    u_name_and_review_list = []                           # define lists - first one is for review by user name,
    rating_and_user_list = []
    date_list = []
    user_rating_date_list = []
    
    theatre_name = soup.find('h1')
    print 'threatre name:', theatre_name.text
    print 'theatre overall rating', overall_rate[0].find("meta")["content"], '\n'
    print 'Comments & Ratings:\n'
    
    # loop through username list and review list
    for user, review in zip(user_name, desc_list):                                        # matches corresponding review to user
        u_name_and_review_list.append('[' + user.text + ']' + '-- ' + review.text + '\n') # add both to a new list
        
    for user in user_meta:
        usr = user.find_all("meta")[0]["content"]
        usr_rate = user.find_all("meta")[1]["content"]
        rating_and_user_list.append(usr + " gave rating of: " + usr_rate)
    
    for d in comment_date:
        if d.find("meta"):
            date_list.append(d.find("meta")["content"])
            
    for a, b in zip(rating_and_user_list, date_list):
        user_rating_date_list.append(a + " on date [" + b + "]")
    
    for a,b in zip(user_rating_date_list, u_name_and_review_list):
        print a,b
    
    
if __name__ == '__main__':
    main()
    
    