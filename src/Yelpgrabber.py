'''
Program that grabs comments and amount of rating stars
off of Yelp, for my mom.

Created on Feb 25, 2016

@author: mishasawangwan and austinmatthews
'''

import urllib
import urllib2
from bs4 import BeautifulSoup

class TheatreData(object):
    def __init__(self):
        self.name       = None
        self.theatre_id = None
        self.dates      = None
        self.ratings    = None
        self.comments   = None

    def set_name_and_id(self, name, ID):
        self.name = name
        self.theatre_id = ID

    def set_post_dates(self, date_list):
        self.dates = date_list

    def set_post_ratings(self, rating_list):
        self.ratings = rating_list

    def set_post_comments(self, comment_list):
        self.comments = comment_list

    def get_theatre_data(self):
        return [self.name, self.theatre_id, self.dates, self.ratings, self.comments]

def main():
    # page to scrap reviews and ratings from

    theatre_one = 'http://www.yelp.com/biz/century-theatres-rowland-plaza-novato?osq=rowland+theatre' #Theatre 472 
    theatre_two = 'http://www.yelp.com/biz/century-theatres-northgate-san-rafael?osq=cinemark+northgate'#Theatre 470
    theatre_three = 'http://www.yelp.com/biz/cinearts-at-the-empire-san-francisco' #Theatre 392
    theatre_four = 'http://www.yelp.com/biz/century-cinema-16-mountain-view?osq=cinemark+theatre' #Theatre 399
    theatre_five = 'http://www.yelp.com/biz/century-larkspur-landing-cinemas-larkspur?osq=cinemark+theatre' #Theatre 426
    theatre_six = 'http://www.yelp.com/biz/century-theatres-anchorage?osq=cinemark' #Theatre 433
    theatre_seven = 'http://www.yelp.com/biz/century-downtown-12-san-mateo?osq=cinemark' #Theatre 437
    theatre_eight = 'http://www.yelp.com/biz/century-20-theatre-daly-city?osq=cinemark' #Theatre 444
    theatre_nine = 'http://www.yelp.com/biz/century-san-francisco-centre-9-san-francisco?osq=sf+center+cinemark+theatre' #Theatre 467
    theatre_ten = 'http://www.yelp.com/biz/century-cinema-corte-madera-corte-madera?osq=corte+medera+cinemark' #Theatre 468
    theare_eleven = 'http://www.yelp.com/biz/century-regency-san-rafael-2?osq=cinemark+regency' #Theatre 471
    theatre_twelve = 'http://www.yelp.com/biz/cinearts-sequoia-mill-valley' #Theatre 473
    theatre_thirteen = 'http://www.yelp.com/biz/cinearts-palo-alto-square-palo-alto?osq=cinemark' #Theatre 475
    theatre_fourteen = 'http://www.yelp.com/biz/century-20-oakridge-san-jose' #Theatre 477
    theatre_fifteen = 'http://www.yelp.com/biz/century-20-downtown-redwood-city-redwood-city?osq=cinemark+theatre' #Theatre 485
    theatre_sixteen = 'http://www.yelp.com/biz/century-theatres-federal-way-federal-way' #Theatre 493
    theatre_seventeen = 'http://www.yelp.com/biz/century-at-tanforan-san-bruno' #Theatre 494
    theatre_eighteen = 'http://nz.yelp.com/biz/century-olympia-theaters-olympia?sort_by=rating_desc' #Theatre 497
    theatre_nineteen = 'http://www.yelp.com/biz/lincoln-square-cinemas-bellevue-2' #Theatre 1118
    
    #theatre_list_test = [theatre_one]

    theatre_list = [theatre_one, theatre_two, theatre_three, theatre_four, theatre_five, theatre_six, theatre_seven, theatre_eight, theatre_nine, 
                    theatre_ten, theare_eleven, theatre_twelve, theatre_thirteen, theatre_fourteen, theatre_fifteen, theatre_sixteen, theatre_seventeen, 
                    theatre_eighteen, theatre_nineteen]
    

    for theatre in theatre_list:                                 # loop through theatre list and perform yelpgrabbing on each
        soup = BeautifulSoup(urllib2.urlopen(theatre), 'html.parser') # parse html using beautiful soup  

        Theatre = TheatreData()

        desc_list = soup('p', {"itemprop":"description"})             # find and return a list of all user reviews on the page
        user_name = soup('a', {"class":"user-display-name"})          # find and return a list of all user names for each user review
        overall_rate = soup('div', {"itemprop":"aggregateRating"})    # find and return a list of (one) theatre aggregate review
        user_meta = soup('div', {"itemprop":"review" })               # find and return a list of all user ratings for each user review
        comment_date = soup('span', {"class":"rating-qualifier"})     # find and return a list of dates for each comment? (need to verify)

        u_name_and_review_list = []                                   # define lists - list for review by user name
        rating_and_user_list = []                                     # list for rating and matching user
        date_list = []                                                # list for dates
        user_rating_date_list = []                                    # list for user rating and date
        list_final = []                                               # list with all content

        list_of_data_lists = [u_name_and_review_list, rating_and_user_list, date_list, user_rating_date_list, list_final] # group the lists together

        for l in list_of_data_lists:   # iterate through the group to delete the contents of any previous theatres
            del l[:]


        theatre_name = soup.find('h1') # find theatre name
        print 'threatre name:', theatre_name.text
        print 'Comments & Ratings:\n'

        Theatre.set_name_and_id(theatre_name.text, 472) # TODO: associate theatres with IDs

        for user, review in zip(user_name, desc_list):                   # loop through username list and review list in parallel and append to a list
            u_name_and_review_list.append('[' + user.text + ']' + ' -- ' + review.text + '\n')

        for user in user_meta:                                           # extract username and rating and append to a list
            usr = user.find_all("meta")[0]["content"]
            usr_rate = user.find_all("meta")[1]["content"]
            rating_and_user_list.append(usr + " gave rating of: " + usr_rate)

        for d in comment_date:                                           # extract date information and append to date list
            if d.find("meta"):
                date_list.append(d.find("meta")["content"])

        for user_and_rating, date in zip(rating_and_user_list, date_list):                # merge the two lists in the previous two loops
            user_rating_date_list.append(user_and_rating + " on date [" + date + "]")

        for user_rate_date, review in zip(user_rating_date_list, u_name_and_review_list): # merge all data into a final list 
            list_final.append(user_rate_date + " " + review)

        for merged_data in list_final:
            print merged_data

if __name__ == '__main__':
    main()
