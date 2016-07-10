'''
Created on Jun 5, 2016

Module to input yelp data into excel spreadsheet.

@author: austinmatthews
'''
import Yelpgrabber
import yelpper
from openpyxl import load_workbook

theatre_one = 'http://www.yelp.com/biz/century-theatres-rowland-plaza-novato?osq=rowland+theatre' #Theatre 472 


wb = load_workbook(filename = 'Yelpreviews.xlsx')

ws = wb.get_sheet_by_name("472")

#ws['A16'] = 4

theatre = yelpper.TheatrePage(theatre_one)
print 'test',theatre.page_url
print theatre.get_dates()

row_count = 0
for c in ws.rows:
    print 'c:', c, 'last row:', row_count
    row_count += 1 

last_empty_row = row_count + 1

wb.save('Yelpreviews.xlsx')

