'''
Created on Jun 5, 2016

Module to input yelp data into excel spreadsheet.

@author: austinmatthews
'''

from openpyxl import load_workbook
wb = load_workbook(filename = 'Yelpreviews.xlsx')

print wb.get_sheet_names()

ws = wb.get_sheet_by_name("392")

<<<<<<< HEAD
print ws
=======
print wb.get_sheet_names()

ws = wb.get_sheet_by_name('392')

ws['A23'] = 4

wb.save('Yelpreviews.xlsx')
>>>>>>> branch_austin
