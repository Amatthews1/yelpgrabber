'''
Created on Jun 5, 2016

Module to input yelp data into excel spreadsheet.

@author: austinmatthews
'''

from openpyxl import load_workbook
wb = load_workbook(filename = 'Yelpreviews.xlsx')



print wb.get_sheet_names()
