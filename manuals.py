#!/usr/bin/python3


from time import sleep
import os
import webbrowser

#dictionaries
handy = {}


# set constants
MAKE = ['SHARP', 'SAMSUNG', 'LEXMARK', '999']
SHARP_TYPE = ['999', 'HANDY', 'SERVICE', 'PARTS']

# program to find manuals
# phil welsby 20 april 2019


# function to clear screen
def wiper():
    print('\n' * 100)


# get the make of the machine from user
# NOTE THIS IS THE MAIN FUNCTION THATS STARTS THE WHOLE PROGRAM
def main():
    wiper()
    print('''\t\t\t\tM    A    N    U    A    L

\t\t\t\tF    I    N    D    E    R\n\n\n\n\n''')
    print('''\t\t\t\tMANUFACTURERS

\t\t\t\tSHARP
\t\t\t\tSAMSUNG
\t\t\t\tLEXMARK

''')
    make = input('\t\t\t\tEnter the manufacturer>>> ')
    make = make.upper()


# check to see if manufacturer is in the list
    if make not in MAKE:
        print('not a recognised manufacturer')
        sleep(3)
        main()
    elif make == 'SHARP':
        sharp_type()
    elif make == 'SAMSUNG':
        samsung()
    elif make == 'LEXMARK':
        lexmark()
    elif make == '999':
        print('Goodbye')
        sleep(3)
        wiper()

# sharp type function
def sharp_type():
    wiper()
    print('''\t\t\t\tChoose the type of manual you want
\t\t\t\tThe choices are:

\t\t\t\tHANDY
\t\t\t\tSERVICE
\t\t\t\tPARTS\n''')
    type_choice = input('\t\t\t\t>>>')
    type_choice = type_choice.upper()
    if type_choice not in SHARP_TYPE:
        print('Invalid choice...')
        sleep(3)
        sharp_type()
    if type_choice == 'HANDY':
        sharp_handy()
    elif type_choice == 'SERVICE':
        sharp_service()
    elif type_choice == 'PARTS':
        sharp_parts()
    elif type_choice == '999':
        print('Returning to main menu...')
        sleep(3)
        main()

def sharp_handy():
    wiper()
    print('sharp handy function here')
    input('Enter to continue...')
    sleep(2)
    main()

def sharp_service():
    wiper()
    print('sharp service function here')
    input('Enter to continue...')
    sleep(2)
    main()

def sharp_parts():
    wiper()
    print('sharp parts function here')
    input('Enter to continue...')
    sleep(2)
    main()


# lexmark function
def lexmark():
    MODELS = ['C4150', 'C6160', 'M5255', 'M5270']
    SERVICE_1 = ['M5255', 'M5270']
    wiper()
    print('\t\t\t\tEnter the model number')
    model_number = input('\t\t\t\t>>>')
    model_number = model_number.upper()
    if model_number not in MODELS:
         print('No manual avaiable for', model_number)
         sleep(3)
         lexmark()
    if model_number == 'C4150':
        webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Lexmark/C4150/C4150_sm.pdf')
        input('Enter to continue...')
        main()
    elif model_number == 'C6160':
        webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Lexmark/C6160/c6160_sm.pdf')
        input('Enter to continue...')
        main()
    elif model_number in SERVICE_1:
        webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Lexmark/M52_XX/M52_XX_service.pdf')
        input('Enter to continue...')
        main()
    elif model_number == '999':
        print('Returning to main menu')
        sleep(3)
        main()

main()


