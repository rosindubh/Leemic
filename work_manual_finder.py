#!/usr/bin/python3

from time import sleep
import os
import webbrowser

# program to find manuals for machines at work

# set variables
MAKE = ['SHARP', 'SAMSUNG', 'LEXMARK']
SHARP_TYPE = ['HANDY', 'SERVICE', 'PARTS']
MODELS = ['3050', '3550', '4050', '5050', '6050']

# function to clear screen
def wiper():
    print('\n' * 100)

# sharp type function
def sharp_type():
    print('need to write the sharp function to find model')
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

# sharp handy function
def sharp_handy():
    wiper()
    print('\t\t\t\tEnter the model number')
    model_number = input('\t\t\t\t>>>')
    if model_number not in MODELS:
        print('No Handy Guide available for', model_number)
        sleep(3)
        sharp_handy()

    if model_number == '3050' or '3550' or '4050' or '5050' or '6050':
        webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/Handy-Guide-Griffin-MX3050N-MX6050N.pdf')
        input('Enter to continue...')
        main()

# sharp service function
def sharp_service():
    wiper()
    print('this is the Sharp service function')

# sharp parts function
def sharp_parts():
    wiper()
    print('this is the Sharp parts function')

# samsung function
def samsung():
    print('need to write the samsung function to find model')

# lexmark function
def lexmark():
    print('need to write the lexmark function to find model')

# get the make and model of the machine from user
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


main()
