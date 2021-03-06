#!/usr/bin/python3


from time import sleep
import os
import webbrowser

# program to find manuals for machines at work
# phil welsby 17 april 2019

# to add a Sharp Manual
# first add all the model number to the list called MODELS
# next add the same model numbers to their own list inside the sharp function (handy/service/parts)
# create a list with the model numbers for the manual you are setting up
# add an if statement to get the model_number variable entered by the user
# then add a webbrowser.open_new('<absolute path'>) to open the pdf
# finally add an input() request to halt the program followed by the main() function

# set variables
MAKE = ['SHARP', 'SAMSUNG', 'LEXMARK', '999']
SHARP_TYPE = ['999', 'HANDY', 'SERVICE', 'PARTS']
SAMSUNG_TYPE = ['SERVICE', 'PARTS']
MODELS = ['999', '654', '754', '904', '1054', '1204', '1055', '1205', '3050', '3550', '4050', '5050', '6050', '3060', '3070', '3560', '3570', '4060',
          '4070', '5070', '6070', '6240', '7040', '6500', '7500', '6580', '7580', '6170', '5170', 
          '4170', '6150', '5150', '4150', '3650', '3150', '2650', 'C4150', 'C6160', 'M5255', 'M5270']

# function to clear screen
def wiper():
    print('\n' * 100)

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
# sharp handy function
def sharp_handy():
    wiper()
    print('\t\t\t\tEnter the model number')
    model_number = input('\t\t\t\t>>>')
    if model_number not in MODELS:
        print('No Handy Guide available for', model_number)
        sleep(3)
        sharp_handy()

    # CR4 machines
    GRIFFIN = ['3050', '3550', '4050', '5050', '6050']
    PHOENIX = ['3060', '3070', '3560', '3570', '4060', '4070', '5070', '6070']
    POLARIS = ['6240', '7040', '6500', '7500']
    POLARIS2 = ['6580', '7580']
    HERCULES = ['904', '1054', '1204', '1055', '1205']
    TAURUS = ['654', '754']
    if model_number in GRIFFIN:
        webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/Handy-Guide-Griffin-MX3050N-MX6050N.pdf')
        input('Enter to continue...')
        main()
    elif model_number in PHOENIX:
        webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5070/Handy-Guide-Phoenix-MX3060-MX6070-MX-5070.pdf')
        input('Enter to continue...')
        main()
    elif model_number in POLARIS:
        webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 6500-7500/Handy Guide Version 3.3.pdf')
        input('Enter to continue...')
        main()
    elif model_number in POLARIS2:
        webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-6580/MX-6580_7580_handy_guide.pdf')
        input('Enter to continue...')
        main()
    elif model_number in HERCULES:
        webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M904/MX-M904_HG.pdf')
        input('Enter to continue...')
        main()
    elif model_number in TAURUS:
        webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M754/Handy-Guide-Taurus-MXM654-MXM754.pdf')
        input('Enter to continue...')
        main()
    elif model_number == '999':
        print('Returning to main menu...')
        sleep(3)
        main()
# sharp service function
def sharp_service():
    wiper()
#    print('this is the Sharp service function')
    SERVICE_1 = ['3050', '3550', '4050', '3060', '3560', '4060', '3070', '3570', '4070']
    SERVICE_2 = ['5050', '6050', '5070', '6070']
    SERVICE_3 = ['6580', '7580']
    SERVICE_4 = ['6500', '7500']
    SERVICE_5 = ['6240', '7040']
    HERCULES = ['904', '1054', '1204']
    TAURUS = ['654', '754']
    print('\t\t\t\tEnter the model number')
    model_number = input('\t\t\t\t>>>')
    if model_number not in MODELS:
        print('No Service Manual available for', model_number)
        sleep(3)
        sharp_service()
    if model_number in SERVICE_1:
        webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 3070-3570-4070/Service Manual (Revised February 2016).pdf')
        input('Enter to continue...')
        main()
    elif model_number in SERVICE_2:
        webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5070/MX-5070_service_manual.pdf')
        input('Enter to continue...')
        main()
    elif model_number in SERVICE_3:
        webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-6580/MX-6580_7580_service_manual.pdf')
        input('Enter to continue...')
        main()
    elif model_number in SERVICE_4:
        webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 6500-7500/MX6500-7500_SM_latest.pdf')
        input('Enter to continue...')
        main()
    elif model_number in SERVICE_5:
        webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 6240-7040/MX-6240_service_manual.pdf')
        input('Enter to continue...')
        main()
    elif model_number in HERCULES:
        webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M904/MXM904-M1054-M1204_SM.pdf')
        input('Enter to continue...')
        main()
    elif model_number in TAURUS:
        webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M754/MXM654-M754_SM.pdf')
        input('Enter to continue...')
        main()
    elif model_number == '999':
        print('Returning to main menu...')
        sleep(3)
        main()



# sharp parts function
def sharp_parts():
    wiper()
    SERVICE_1 = ['6070', '5070', '4070', '3570', '3070', '4060', '3560', '3060', '6050', '5050', '4050', 
                 '3550', '3050','6170', '5170', '4170', '6150', '5150', '4150', '3650', '3150', '2650']
    SERVICE_2 = ['6500', '7500']
    HERCULES = ['904', '1054', '1204']
    TAURUS = ['654', '754']
    print('\t\t\t\tEnter the model number')
    model_number = input('\t\t\t\t>>>')
    if model_number not in MODELS:
        print('No Parts Manual available for', model_number)
        sleep(3)
        sharp_parts()
    if model_number in SERVICE_1:
        webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/MX5050-MX6050_parts.pdf')
        input('Enter to continue...')
        main()
    elif model_number in SERVICE_2:
        webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 6500-7500/MX-6500_parts.pdf')
        input('Enter to continue...')
        main()
    elif model_number in HERCULES:
        webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M904/MXM904-M1054-M1204_PG.pdf')
        input('Enter to continue...')
        main()
    elif model_number in TAURUS:
        webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M754/MXM654-MXM754-KB13_PG_.pdf')
        input('Enter to continue...')
        main()
    elif model_number == '999':
        print('Returning to main menu...')
        sleep(3)
        main()


# samsung function
def samsung():
    print('need to write the samsung function to find manual type')
    input('Enter to continue...')
    main()

# lexmark function
def lexmark():
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


main()
