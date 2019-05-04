# script to read excel sheets
# the idea is to be able to choose which columns to 
# write to the output file and to choose a range of rows
# phil welsby 1 may 2019

import os
from xlrd import open_workbook, XL_CELL_TEXT

# dictionary of conversions from column letter to an interger
Columns_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 
                'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,'N': 14, 'O': 15, 
                'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 
                'W': 23, 'X': 24, 'Y': 26, 'Z': 26, 'AA': 27, 'AB': 28, 'AC': 29,
                'AD': 30, 'AE': 31, 'AF': 32, 'AG': 33, 'AH': 34, 'AI': 35, 'AJ': 36,
                'AK': 37, 'AL': 38, 'AM': 39, 'AN': 40, 'AO': 41, 'AP': 42, 'AQ': 43,
                'AR': 44, 'AS': 45, 'AT': 46, 'AU': 47, 'AV': 48, 'AW': 49, 'AX': 50,
                'AY': 51, 'AZ': 52, 'BA': 53, 'BB': 54, 'BC': 55, 'BD': 56, 'BE': 57,
                'BF': 58, 'BG': 59, 'BH': 60, 'BI': 61, 'BJ': 62, 'BK': 63, 'BL': 64,
                'BM': 65, 'BN': 66, 'BO': 67, 'BP': 68, 'BQ': 69, 'BR': 70, 'BS': 71,
                'BT': 72, 'BU': 73, 'BV': 74, 'BW': 75, 'BX': 76, 'BY': 77, 'BZ': 78 }   #26 LETTERS ADD MORE IF REQUIRED

#variables
space = ' '
new_line = '\n'
L_columns = [] # to be used as list of the columns to be read
num_columns = None
choice = None
string_length = 30
itter_count = 0

# get input from user
file = input('Copy and paste file here: ')
print('File to open is', file)
sheet_num = int(input('Enter sheet number: '))
sheet_num = sheet_num -1
R_start = int(input('Enter the start row: '))
R_start = R_start -1
R_end = int(input('Enter the end row: '))
num_columns = int(input('Enter the number of columns: '))

# populate columns list
for i in range(num_columns):
    choice = input('Enter a column LETTER: ')
    choice = choice.upper()
    conversion = Columns_dict[choice]
    conversion = conversion - 1
#    print('Working please wait...')
    L_columns.append(conversion)
print('Working please wait...')
#open file to write to
with open('/home/phil/Documents/output_file', 'w') as file_out:

    # open workbook
    book = open_workbook(file)
    sheet = book.sheet_by_index(sheet_num)

    for x in range(num_columns):
        cell = sheet.cell(0, L_columns[x])
        file_out.writelines(str(cell.value))
        cell.value = str(cell.value)
        cell_length = len(cell.value)
        diff = string_length - cell_length
        for i in range(diff):
            file_out.writelines(space)
    file_out.writelines(new_line)

    itter_count = 0

    for row in range(R_start, R_end):
        for i in range(num_columns):
            cell = sheet.cell(row, L_columns[itter_count])
            file_out.writelines(str(cell.value))
            cell.value = str(cell.value)
            cell_length = len(cell.value)
            diff = string_length - cell_length
            for i in range(diff):
                file_out.writelines(space)
            itter_count += 1
            if itter_count == num_columns:
                file_out.writelines(new_line)
                itter_count = 0


