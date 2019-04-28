# script to change an excel file to a text file
# whilst keeping the same layout
# phil welsby 28 april 2019

# import modules
import os
from xlrd import open_workbook,XL_CELL_TEXT

# set variable for path
path = '/home/phil/Environments/excel/'

# get file name to open
file_name = input('Enter file name: ')
file = path + file_name
print('File to be opened is', file)

# variables
new_line = '\n'
space = ' '
count = 0
row = 0
column = 0
STRING_LENGTH = 35

# open workbook
book = open_workbook(file)
sheet = book.sheet_by_index(0)

# get input from user
columns = int(input('Enter number of columns: '))
rows = int(input('Enter number of rows: '))

with open('/media/phil/USB_STICK/output_file.txt', 'w') as write_to_file:

    while row != rows:
        cell = sheet.cell(row, column)
        write_to_file.writelines(str(cell.value))
        cell.value = str(cell.value)
        cell_length = len(cell.value)
        diff = STRING_LENGTH - cell_length
        for i in range(diff):
            write_to_file.writelines(space)
        column = column + 1
        if column == columns:
            write_to_file.writelines(new_line)
            column = 0
            row = row + 1

