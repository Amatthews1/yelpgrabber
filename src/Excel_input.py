'''
Created on Jun 5, 2016

Module to input yelp data into excel spreadsheet.

@author: austinmatthews
'''
import Yelpgrabber
from openpyxl import load_workbook
wb = load_workbook(filename = 'Yelpreviews.xlsx')

ws = wb.get_sheet_by_name("471")

#ws['A16'] = 4

row_count = 0
for c in ws.rows:
    print 'c:', c, 'last row:', row_count
    row_count += 1 

last_empty_row = row_count + 1

wb.save('Yelpreviews.xlsx')

