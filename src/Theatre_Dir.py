


class TheatreDirectory:
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
    theatre_eleven = 'http://www.yelp.com/biz/century-regency-san-rafael-2?osq=cinemark+regency' #Theatre 471
    theatre_twelve = 'http://www.yelp.com/biz/cinearts-sequoia-mill-valley' #Theatre 473
    theatre_thirteen = 'http://www.yelp.com/biz/cinearts-palo-alto-square-palo-alto?osq=cinemark' #Theatre 475
    theatre_fourteen = 'http://www.yelp.com/biz/century-20-oakridge-san-jose' #Theatre 477
    theatre_fifteen = 'http://www.yelp.com/biz/century-20-downtown-redwood-city-redwood-city?osq=cinemark+theatre' #Theatre 485
    theatre_sixteen = 'http://www.yelp.com/biz/century-theatres-federal-way-federal-way' #Theatre 493
    theatre_seventeen = 'http://www.yelp.com/biz/century-at-tanforan-san-bruno' #Theatre 494
    theatre_eighteen = 'http://nz.yelp.com/biz/century-olympia-theaters-olympia?sort_by=rating_desc' #Theatre 497
    theatre_nineteen = 'http://www.yelp.com/biz/lincoln-square-cinemas-bellevue-2' #Theatre 1118

    def __init__(self):
        self.theatres = {
            472 : self.theatre_one,
            470 : self.theatre_two,
            392 : self.theatre_three,
            399 : self.theatre_four,
            426 : self.theatre_five,
            433 : self.theatre_six,
            437 : self.theatre_seven,
            444 : self.theatre_eight,
            467 : self.theatre_nine,
            468 : self.theatre_ten,
            471 : self.theatre_eleven,
            473 : self.theatre_twelve,
            475 : self.theatre_thirteen,
            477 : self.theatre_fourteen,
            485 : self.theatre_fifteen,
            493 : self.theatre_sixteen,
            494 : self.theatre_seventeen,
            497 : self.theatre_eighteen,
            1118 : self.theatre_nineteen,
        }