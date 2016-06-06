'''
Program that grabs comments and amount of rating stars
off of Yelp, for my mom.

Created on Feb 25, 2016

@author: mishasawangwan and austinmatthews
'''

import urllib
import urllib2
from bs4 import BeautifulSoup
from openpyxl import load_workbook


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
    
    
    theatre_list = [theatre_one, theatre_two, theatre_three, theatre_four, theatre_five, theatre_six, theatre_seven, theatre_eight, theatre_nine, 
                    theatre_ten, theare_eleven, theatre_twelve, theatre_thirteen, theatre_fourteen, theatre_fifteen, theatre_sixteen, theatre_seventeen, 
                    theatre_eighteen, theatre_nineteen]
    
    for theatre in theatre_list:
        
        soup = BeautifulSoup(urllib2.urlopen(theatre), 'html.parser')                                 # parse html using beautiful soup  
          
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
    
    
    