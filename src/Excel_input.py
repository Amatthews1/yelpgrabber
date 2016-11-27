'''
Created on Jun 5, 2016

Module to input yelp data into excel spreadsheet.

@author: austinmatthews
'''
import Yelpgrabber
import Theatre_Dir
import yelpper
from openpyxl import load_workbook

theatre_one = 'http://www.yelp.com/biz/century-theatres-rowland-plaza-novato?osq=rowland+theatre' #Theatre 472 

directory = Theatre_Dir.TheatreDirectory()
workbook = load_workbook(filename = 'Yelpreviews.xlsx')

for t_id, t_name in directory.theatres.items():
    t = Yelpgrabber.TheatreData(t_name)
    review_dates = t.get_dates()
    review_ratings = t.get_ratings()
    worksheet = workbook.get_sheet_by_name(str(t_id))

    row_count = 0
    for c in worksheet.rows:
        row_count += 1
    last_empty_row = row_count + 1

    start_row = last_empty_row

    for i, dating in enumerate(review_dates): # dating = date
        row_to_print_in = 'A' + str(last_empty_row + i)
        worksheet[row_to_print_in] = dating
    
    last_empty_row = start_row

    for i, rating in enumerate(review_ratings):
        row_to_print_in = 'B' + str(last_empty_row + i)
        print rating
        worksheet[row_to_print_in] = str(rating)
    
    last_empty_row = start_row        

    workbook.save('Yelpreviews.xlsx')
    break

