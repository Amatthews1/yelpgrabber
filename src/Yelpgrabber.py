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
    theatre_one = 'http://www.yelp.com/biz/century-theatres-rowland-plaza-novato?osq=rowland+theatre' # page to scrap reviews and ratings from
    soup = BeautifulSoup(urllib2.urlopen(theatre_one), 'html.parser')                                 # parse html using beautiful soup  
    
    # using the format 'tag', {'attribute', 'attribute-name'} we can find specific html elements on the page
    desc_list = soup('p', {"itemprop":"description"})     # creates a list of all the reviews on the page
    user_name = soup('a', {"class":"user-display-name"})  # creates a list of all the user names on the page
    ratings = soup('meta', {"itemprop":"ratingValue" })   # creates a list of all the ratings on the page
    
    u_name_and_review_list = []                           # define lists - first one is for review by user name,
    rating_list = []                                      # the second one is for extracted rating values
    
    # loop through username list and review list
    for user, review in zip(user_name, desc_list):                                        # matches corresponding review to user
        u_name_and_review_list.append('[' + user.text + ']' + '-- ' + review.text + '\n') # add both to a new list
    
    # loop through ratings list    
    for rating in ratings:
        extracted_rating = rating["content"]                                              # extract the 'content' value
        rating_list.append(extracted_rating)                                              # add to new list
    
    # loop through all the lists so far    
    for uname_and_review, rating in zip(u_name_and_review_list, rating_list):             # loop through both lists in parallel
        print 'Rating of [', rating, '] by user', uname_and_review + '\n'                 # output final string for now
    


    

if __name__ == '__main__':
    main()
    
    