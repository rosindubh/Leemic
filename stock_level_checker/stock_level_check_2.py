# program to keep check on parts fitted from vehicle and stock replenisment
# 12 dec 2019 - phil welsby

# import datetime
from datetime import datetime

# function to clear screen
def wiper():
    print('\n' * 50)

# files that part numbers and quantities are to be written to
master_text = open('MASTER.txt', 'a')
used_parts = open('usedParts.txt', 'a')
all_parts = open('allParts.txt', 'a')
# clear screen
wiper()

# get customer and machine type from user
customer = input('Enter customer: ')
machine_type = input('Enter machine type: ')

# function to add parts and quantities to 3 text files (MASTER.txt, usedParts.txt and allParts.txt)
def get_input():
    # files that part numbers and quantities are to be written to
    master_text = open('MASTER.txt', 'a')
    used_parts = open('usedParts.txt', 'a')
#    all_parts = open('allParts.txt', 'a')

    # get user imput
    now = datetime.now()
    date = (now.day, now.month, now.year)
    part_number = input('Enter part number: ')
    num = int(input('Enter quantity: '))

    # print inputted data to the MASTER.txt and  usedParts.txt 
    print('Date:', date, '\tCustomer:', customer, '\tMachine', machine_type, '\tPart Number:', part_number, '\tQuantity:', num, '\n', file = master_text)
    master_text.close()
    for i in range(num):
        print(part_number, file = used_parts)
    used_parts.close()

# continue yes or no
    continue_input = input('Continue y/n ')
    if continue_input == 'y':
        get_input()
    else:
        print('Goodbye...')
        inventory()


def inventory():
    # code to produce a full list of all parts fitted with no duplicates
    # program to get a list of all parts fitted without duplicates
    # 14 dec 2019 - phil welsby

    import os

    full_list = set()

    used_parts = open('/home/phil/stock_level_checker/usedParts.txt', 'r')
    all_parts = open('/home/phil/stock_level_checker/allParts.txt', 'a')

    for i in used_parts:
        full_list.add(i)
    for i in full_list:
        print(i, file = all_parts)
    all_parts.close()
    used_parts.close()


get_input()
