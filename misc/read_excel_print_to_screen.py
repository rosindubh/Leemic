def excel_reader():
    # script to read an excel file and print the contents to the screen
    # phil welsby 26 april 2019

    # clear screen function
    def wiper():
        print('\n' * 100)

    # clear screen
    wiper()

    # set variable for list
    L = []

    # set variable for path
    path = '/home/phil/Environments/excel/'

    # import sleep from time
    from time import sleep
    # import the xlrd module
    import xlrd

    # import os to navigate to the folder
    import os

    # get file name to open
    file_name = input('Enter file name: ')
    file = path + file_name
    print('File to be opened is', file)
    #input()

    # open the spreadsheet file (or workbook)
    try:
        workbook = xlrd.open_workbook(file)
    except:
        print('File not found, Enter to continue...')
        input()
        excel_reader()
    # open the first sheet by its index
    worksheet = workbook.sheet_by_index(0)

    # read each row in the worksheet and append as a list into a list
    rows = int(input('Enter the number of rows: '))
    wiper()
    try:
        for row in range(rows):
            L.append(worksheet.row_values(row))
    except:
        print('Out of range, too many rows may be the cause')
        print('You entered', rows, 'Please check your spreadsheet.')
        input('Enter to continue...')
        excel_reader()

    # print out the list
    #print(L)

    # nester function from head first python
    def print_lol(the_list):
        for each_item in the_list:
            if isinstance(each_item, list):
                print_lol(each_item)
            else:
                print(each_item, end = ' ')
        print()
    print_lol(L)
    cont = input('Enter \'Y\' to continue: ')
    cont = cont.upper()
    if cont == 'Y':
        excel_reader()
    else:
        print('Goodbye')
        sleep(2)
        wiper()


excel_reader()
