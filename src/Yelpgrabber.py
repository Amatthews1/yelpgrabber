'''
Program that grabs comments and amount of rating stars
off of Yelp, for my mom.

Created on Feb 25, 2016

@author: mishasawangwan and austinmatthews
'''

import urllib
import urllib2
import Theatre_Dir
from bs4 import BeautifulSoup

class TheatreData(object):
    def __init__(self, theatre_id):
        self.name       = None
        self.id         = None
        self.dates      = []
        self.ratings    = []
        self.comments   = None
        self.soup = BeautifulSoup(urllib2.urlopen(theatre_id), 'html.parser')

    def get_dates(self):
        comment_date = self.soup('span', {"class": "rating-qualifier"})
        for date in comment_date:                                       # extract date information and append to date list
            if date.find("meta"):
                self.dates.append(date.find("meta")["content"])
        return self.dates

    def get_ratings(self):
        usr_meta = self.soup('div', {"itemprop":"review" })
        for usr_rating in usr_meta:                                           # extract username and rating and append to a list
            #usr = user.find_all("meta")[0]["content"]
            rating = usr_rating.find_all("meta")[1]["content"]
            self.ratings.append(rating)
        return self.ratings

def main():
    directory = Theatre_Dir.TheatreDirectory()

    for theatre_id, theatre in directory.theatres.items():                                 # loop through theatre list and perform yelpgrabbing on each
        soup = BeautifulSoup(urllib2.urlopen(theatre), 'html.parser') # parse html using beautiful soup  

        #Theatre = TheatreData()

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

        #Theatre.name = theatre_name
        #Theatre.id = theatre_id

        for user, review in zip(user_name, desc_list):                   # loop through username list and review list in parallel and append to a list
            u_name_and_review_list.append('[' + user.text + ']' + ' -- ' + review.text + '\n')

        for user in user_meta:                                           # extract username and rating and append to a list
            usr = user.find_all("meta")[0]["content"]
            usr_rate = user.find_all("meta")[1]["content"]
            rating_and_user_list.append(usr + " gave rating of: " + usr_rate)

        for d in comment_date:                                           # extract date information and append to date list
            if d.find("meta"):
                date_list.append(d.find("meta")["content"])
        print date_list
                #Theatre.dates = date_list

        for user_and_rating, date in zip(rating_and_user_list, date_list):                # merge the two lists in the previous two loops
            user_rating_date_list.append(user_and_rating + " on date [" + date + "]")

        for user_rate_date, review in zip(user_rating_date_list, u_name_and_review_list): # merge all data into a final list 
            list_final.append(user_rate_date + " " + review)

        for merged_data in list_final:
            pass
            #print merged_data

if __name__ == '__main__':
    main()
