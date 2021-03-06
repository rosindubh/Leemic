# function to select which guide to use. Either Handy Guides, Service Manuals or Parts Catalogues
# phil welsby 3 december 2018

def main_menu():

    import os

    # set relevent directory
#    os.chdir('/home/phil/my_python_programs/manual_finder')

    # function to clear screen
    def wiper():
        print('\n' *100)
    # clear screen
    wiper()


    # menu
    print('''\t\t\t\t\t\t\t\t\t        MAIN MENU









\t\t\t\t\t\t\t\t\t(1)   Sharp Handy Guides
    \t\t\t\t\t\t\t\t\t(2)   Sharp Service Manuals
    \t\t\t\t\t\t\t\t\t(3)   Sharp Parts Catalogues
    \t\t\t\t\t\t\t\t\t(4)   Sharp Peripherals
    \t\t\t\t\t\t\t\t\t(5)   IP addresses
    \t\t\t\t\t\t\t\t\t(6)   List of Simulation Codes
    \t\t\t\t\t\t\t\t\t(7)   List of error codes
    \t\t\t\t\t\t\t\t\t(8)   LAMP on Raspberry Pi Setup
    \t\t\t\t\t\t\t\t\t(9)   L4-17/L4-18 parts price comparison
    \t\t\t\t\t\t\t\t\t(10)  Office 365 Settings for Email
    \t\t\t\t\t\t\t\t\t(11)  UART communication issue at JMW
    \t\t\t\t\t\t\t\t\t(12)  Full Calibration
    \t\t\t\t\t\t\t\t\t(13)  Lexmark Acronyms
    \t\t\t\t\t\t\t\t\t(14)  FF-00 notes on MX-6500
    \t\t\t\t\t\t\t\t\t(15)  Sharp maintenance Codes
    \t\t\t\t\t\t\t\t\t(16)  LC17 Signals
    \t\t\t\t\t\t\t\t\t(999) EXIT\n\n\n\n\n''')


    # get input from user
    user_choice = '0'
    user_choice = input('\n\nEnter your selection then press ENTER: ')
    print('\n\n')
    print('Your choice was', user_choice)

    if user_choice == '1':
        handy_guides()
    elif user_choice == '2':
        service_manuals()
    elif user_choice == '3':
        parts_guides()
    elif user_choice == '4':
        peripherals()
##    elif user_choice == '5':
##        ast_ip()
    elif user_choice == '5':
        ip()
    elif user_choice == '6':
        simulation()
    elif user_choice == '7':
        error_codes()
    elif user_choice == '8':
        lamp()
    elif user_choice == '9':
        l4_error()
    elif user_choice == '10':
        Office365()
    elif user_choice == '11':
        uart_jmw()
    elif user_choice == '12':
        full_cal()
    elif user_choice == '13':
        lex_acronyms()
    elif user_choice == '14':
        FF00()
    elif user_choice == '15':
        Maintenance_Codes()
    elif user_choice == '16':
        LC17_signals()

    elif user_choice == '999':
        wiper()
        print('GOODBYE HAVE A NICE DAY...')
        return
    else:
        print(user_choice, 'is not valid')
        input('ENTER to continue...')
        main_menu()
# function to find sharp handy guides
# phil welsby 30th november 2018


########################################################################
#                     THIS PROGRAM HAS A BUG                           #
#                                                                      #
# *** BUG ***                                                          #
# In pixman_region32_init_rect: Invalid rectangle passed               #
# Set a breakpoint on '_pixman_log_error' to debug                     #
# PROGRAM HAS BUG WHEN RUNNING AND SELECTING NUMBERS 24, 25 AND 28     #
# NEED TO DE-BUG THIS ASAP                                             #
#                                                                      #
########################################################################


# sharp handy guides function
def handy_guides():


    import os
    import webbrowser

    # function to clear screen
    def wiper():
        print('\n' * 100)
    # clear screen
    wiper()

    # opening menu listing handy guides

    print('''\t\t\t\t\t\t\t\t\t***SHARP HANDY GUIDE MENU***\n\n\n
\t\t\t\t(1) MX-264N\tMX-314N\t\tMX-354N
\t\t\t\t(2) MX-M363N\tMX-M453N\tMX-M503N



\t\t\t\t(20) MX-1800N\tMX-2300N\tMX-2700N\tMX-3500N\tMX-3501N\tMX-4500N\tMX4501N
\t\t\t\t(21) MX-2310U\tMX3111U
\t\t\t\t(22) MX-2314\tUSE MX-2614/3114
\t\t\t\t(23) MX-2614N\tMX-3114N
\t\t\t\t(24) MX-2301N\tMX-2600N\tMX-3100N
\t\t\t\t(25) MX-2610N\tMX-3110N\tMX-3610N
\t\t\t\t(26) MX-2630N
\t\t\t\t(27) MX-2640N\tMX3140N\t\tMX3640N
\t\t\t\t(28) MX-4112N\tMX-5112N
\t\t\t\t(29) MX-4140\tMX-4141N\tMX-5141N

\t\t\t\t(30) MX-3050N\t\tMX-3550N/MX4050N\tMX-5050N/MX-6050N
\t\t\t\t(31) MX-3060N/MX-3070N\tMX-3560N/3570N\t\tMX-4060N/4070N\t\tMX-5070N/6070N
\t\t\t\t(32) MX-6240N\tMX7040N\t\tMX-6500N\tMX-7500N
\t\t\t\t(33) MX-6580N\tMX-7580N

\t\t\t\t(40) MX-M904\t\tMX-M1054\t\tMX-M1204\t\tMX-M1055\tMX-M1205
\t\t\t\t(41) MX-M365N\t\tMX-M465N\t\tMX-565
\t\t\t\t(42) MX-M904\t\tMX-M1054\t\tMX-M1024\t\tMX-M1055\tMX-M1205
\t\t\t\t(43) MX-B355W\t\tMX-B455W
\t\t\t\t(44) MX-M364N\t\tMX-M365N\t\tMX-M465N\t\tMX-M565N
\t\t\t\t(45) MX-M283N\t\tMX-M363N\t\tMX-M453N\t\tMX-M503N
\t\t\n\n\n\n\n\t\t\t\t(999) MAIN MENU''')





    # path of HDD containing Sharp Manuals
    # /media/phil/Phil_Welsby/Manufacturers/Sharp

    # get input from user
    model_number = None
    model_number = input('\n\n\n\n\nEnter your choice: ')
    #print('Your choice was', model_number)


    try:
        # main program handy guides
        if model_number == '1':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M264/MX-M264NHandyGuide.pdf')
            handy_guides()
        elif model_number == '2':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX M283-363-453-503/Handy Guide/Handyguide Version 1 August 2009.pdf')
            handy_guides()



        elif model_number == '20':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2300-2700/Handy Guide/August 2007 Version 4 revised handy guide (Includes pastel light, Pastel and C-Jupiter).pdf')
            handy_guides()
        elif model_number == '21':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2310-3111/Handy Guide.pdf')
            handy_guides()
        elif model_number == '22':
            print('USE MX-2614/3114 Handy Guide')
            handy_guides()
        elif model_number == '23':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2314-2614-3114/MX2614N-MX3114N462 Handy Guide.pdf')
            handy_guides()
        elif model_number == '24':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2600-3100/Handy Guides/Revised Handy Guide Version 5 July 2010.pdf')
            handy_guides()
        elif model_number == '25':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2610-3110-3610/Handy Guide/Handy-Guide-Aries-MX2610-MX3610.pdf')
            handy_guides()
        elif model_number == '26':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2630/Handy-Guide-Sphinx-MX2630.pdf')
            handy_guides()
        elif model_number == '27':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2640-3140-3640/MX2640N - MX3140N - MX3640N Handy Guide Version 1 April 2013.pdf')
            handy_guides()
        elif model_number == '28':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-4112N_MX-5112N/Handy-Guide-Virgo-MX4112-MX5112.pdf')
            handy_guides()
        elif model_number == '29':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 4140-5141/Handy Guide.pdf')
            handy_guides()


        elif model_number == '30':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/Handy-Guide-Griffin-MX3050N-MX6050N.pdf')
            handy_guides()
        elif model_number == '31':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5070/Handy-Guide-Phoenix-MX3060-MX6070-MX-5070.pdf')
            handy_guides()
        elif model_number == '32':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 6500-7500/Handy Guide Version 3.3.pdf')
            handy_guides()
        elif model_number == '33':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-6580/MX-6580_7580_handy_guide.pdf')
            handy_guides()

        elif model_number == '40':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M1205/MXM1205_handy_guide.pdf')
            handy_guides()
        elif model_number == '41':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M565/Handy-Guide-Orion-Lotus-MXM365N-MXM465N-MXM565N.pdf')
            handy_guides()
        elif model_number == '42':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M904/MX-M904_HG.pdf')
            handy_guides()
        elif model_number == '43':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-B355W_MX-B455W/MX-B355W_MX-B455W_handy_guide.pdf')
            handy_guides()
        elif model_number == '44':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX M364/MX M364-365N Handy Guide.pdf')
            handy_guides()
        elif model_number == '45':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX M283-363-453-503/Handy Guide/Handyguide Version 1 August 2009.pdf')
            handy_guides()
        elif model_number == '999':
            main_menu()
        else:
            print(model_number, 'IS NOT VALID!')
            input('ENTER to continue...')
            handy_guides()
    except ValueError:
        handy_guides()




# function to find sharp service manuals
# phil welsby 1st december 2018


# sharp service manual function
def service_manuals():


    import os
    import webbrowser

    # function to clear screen
    def wiper():
        print('\n' * 100)

    # clear screen
    wiper()

    # opening menu listing service manuals

    print('''\t\t\t\t\t\t\t\t\t***SHARP SERVICE MANUAL MENU***\n\n\n
\t\t\t\t(1) MX-264U\tMX-314U\t\tMX-354U
\t\t\t\t(2) MX-M283N\tMX-M363N\tMX-M453N\tMX-M503N\tMX-M282N/M362N

\t\t\t\t(20) MX-2300/2700N
\t\t\t\t(21) MX-2010U\tMX-2310U\tMX3111U\t\tMX-2610N\tMX-3110N\tMX3610N
\t\t\t\t(22) MX-2314\tUSE MX-2614/3114
\t\t\t\t(23) MX-2614N\tMX-3114N
\t\t\t\t(24) MX-2301N\tMX-2600N\tMX-3100N
\t\t\t\t(25) MX-2610N\tMX-3110N\tMX-3610N
\t\t\t\t(26) MX-2630N
\t\t\t\t(27) MX-2640N\tMX3140N\t\tMX3640N
\t\t\t\t(28) MX-4110N\tMX-5110N\tMX-4111N\tMX-5111N\tMX-4112N\tMX-5112N
\t\t\t\t(29) MX-4140N\tMX-5140N\tMX-4141N\tMX-5141N

\t\t\t\t(30) MX-3050N/3550N/4050N\tMX-3060N/3560N/4060N\t\tMX-3070N/3570N/4070N
\t\t\t\t(31) MX-5050N\tMX-6050N\tMX5070N\t\tMX-6070N
\t\t\t\t(32) MX-6240N\tMX-7040N
\t\t\t\t(33) MX-6500N\tMX-7500N
\t\t\t\t(34) MX-6580N\tMX-7580N

\t\t\t\t(40) MX-M1055\tMX-M1205
\t\t\t\t(41) MX-B355W\tMX-B455W
\t\t\t\t(42) MX-M365N\tMX-M364N\tMX-M465N\tMX-M464N\tMX-M565N\tMX-M564N
\t\t\t\t(43) MX-M283N\tMX-M363N\tMX-M453N\tMX-M503N\tMX-M282N\tMX-M362N
\t\t\t\t(43) MX-M452N\tMX-M502N
\t\t\t\t(44) MX-M904\tMX-M1054\tMX-M1204
\t\t\n\n

\t\t\t\t(999) MAIN MENU''')





    # path of HDD containing Sharp Manuals
    # /media/phil/Phil_Welsby/Manufacturers/Sharp

    # get input from user
    model_number = None
    model_number = input('\n\n\nEnter your choice: ')
    #print('Your choice was', model_number)


    try:
        # main program service manuals
        if model_number == '1':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M264/MX M264N Service Manual.pdf')
            service_manuals()
        elif model_number == '2':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX M283-363-453-503/Service Manual/Updated Service Manual - June 10.pdf')
            service_manuals()
        elif model_number == '20':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2300-2700/Service Manual/2300_Service Manual.pdf')
            service_manuals()
        elif model_number == '21':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2310-3111/Service Manual - Revised May 2011.pdf')
            service_manuals()
        elif model_number == '22':
            print('USE MX-2614N/3114N')
            service_manuals()
        elif model_number == '23':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2314-2614-3114/MX2614N-MX3114N Service.pdf')
            service_manuals()
        elif model_number == '24':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2600-3100/Service Manual/MX2600 - MX3100 Service (complete).pdf')
            service_manuals()
        elif model_number == '25':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2610-3110-3610/Service Manual/MX2310-MX2610-MX3110 Revised Feb 2011 - Service Manual - Complete.pdf')
            service_manuals()
        elif model_number == '26':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2630/service manual.pdf')
            service_manuals()
        elif model_number == '27':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2640-3140-3640/MX2640N-MX3140N-MX3640N - Service Manual Complete - Dec 12.pdf')
            service_manuals()
        elif model_number == '28':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-4112N_MX-5112N/MX4112-5112_SM.pdf')
            service_manuals()
        elif model_number == '29':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 4140-5141/Service Manual Revised June 2014.pdf')
            service_manuals()

        elif model_number == '30':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 3070-3570-4070/Service Manual (Revised February 2016).pdf')
            service_manuals()
        elif model_number == '31':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/MX-5050_service_manual.pdf')
            service_manuals()
        elif model_number == '32':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 6240-7040/MX-6240_service_manual.pdf')
            service_manuals()
        elif model_number == '33':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 6500-7500/Complete Service Manual - All Sections - Updated May 2014.pdf')
            service_manuals()
        elif model_number == '34':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-6580/MX-6580_7580_service_manual.pdf')
            service_manuals()
        elif model_number == '40':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M1205/MX-M1205_service_manual.pdf')
            service_manuals()
        elif model_number == '41':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-B355W_MX-B455W/MX-B355W_MX-B455W_service_manual.pdf')
            service_manuals()
        elif model_number == '42':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX M364/MX M364-365N Service Manual.pdf')
            service_manuals()
        elif model_number == '43':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX M283-363-453-503/Service Manual/Updated Service Manual - June 10.pdf')
            service_manuals()
        elif model_number == '44':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M904/MXM904-M1054-M1204_SM.pdf')
            service_manuals()

        elif model_number == '999':
            main_menu()
        else:
            print(model_number, 'IS NOT VALID!')
            input('ENTER to continue...')
            service_manuals()
    except ValueError:
        service_manuals()


# function to find sharp parts guides
# phil welsby 2nd december 2018





# sharp parts guides function
def parts_guides():


    import os
    import webbrowser

    # function to clear screen
    def wiper():
        print('\n' * 100)
    # clear screen
    wiper()

    # opening menu listing parts guides

    print('''\t\t\t\t\t\t\t\t\t***SHARP PARTS MANUALS MENU***\n\n\n
\t\t\t\t(1) MX-264N\tMX-314N\t\tMX-354N
\t\t\t\t(2) MX-M283N/M363N/M453N\tMX-M503N/M282N/M362N\tMX-M452N/M502N



\t\t\t\t(20) MX-1800N\tMX-2300N\tMX-2700N
\t\t\t\t(21) MX-2310F\tMX-2311FN\tMX-2610FN\tMX-3110FN\tMX-3610FN\tMX-3111F\tMX-3112FN
\t\t\t\t(22) MX-3640N\tMX-3640NR\tMX-3640FN\tMx-3614FN\tMX-3116N\tMX-3115N\tMX-3140N\tMX-3140NR
\t\t\t\t(23) MX-3140FN\tMX-3114N\tMX-3114NR\tMX-3114FN\tMX-2640N\tMX-2640NR\tMX-2640FN\tMX2616N
\t\t\t\t(24) MX-2615N\tMX-2614N\tMX-2614NR\tMX-2514FN\tMX2314N\t\tMX-2314NR
\t\t\t\t(25) MX-2301N\tMX-2600N\tMX-3100N
\t\t\t\t(26) MX-2610N\tMX-3110N\tMX-3610N
\t\t\t\t(27) MX-2630N
\t\t\t\t(28) MX-2640N\tMX3140N\t\tMX3640N
\t\t\t\t(29) MX-4112N\tMX-5112N
\t\t\t\t(30) MX-4140N\tMX-5140N\tMX-4141N\tMX-5141N

\t\t\t\t(31) MX-3050N\tMX-3550N\tMX-4050N\tMX-5050N\tMX-6050N
\t\t\t\t(32) MX-4070N\tMX-3570N\tMX-3070N\tMX-3560N\tMX-3060N\tMX-4050N\tMX-3550N\tMX-3050N
\t\t\t\t(33) MX-5070N\tMX-6070N
\t\t\t\t(34) MX-6540FN\tMX-7040N\tMX-6240N
\t\t\t\t(35) MX-6500N\tMX-7500N
\t\t\t\t(36) MX-6580N\tMX-7580N

\t\t\t\t(40) MX-M1055\tMX-M1205
\t\t\t\t(41) MX-B355W\tMX-B455W
\t\t\t\t(42) MX-M364N\tMX-M365N\tMX-M464N\tMX-M465\t\tMX-M564N\tMX-M565N
\t\t\t\t(43) MX-M283N\tMX-M363N\tMX-M453N\tMX-M503N\tMX-M282N
\t\t\t\t(43) MX-M362N\tMX-M452N\tMX-M502N
\t\t\t\t(44) MX-M904\tMX-M1054\tMX-M1204
\t\t\n\n\t\t\t\t(999) MAIN MENU''')


    # path of HDD containing Sharp Manuals
    # /media/phil/Phil_Welsby/Manufacturers/Sharp

    # get input from user
    model_number = None
    model_number = input('\n\nEnter your choice: ')
    #print('Your choice was', model_number)

    try:
        # main program
        if model_number == '1':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M264/MX M264N Parts Guide.pdf')
            parts_guides()
        elif model_number == '2':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX M283-363-453-503/Parts Guide/MX-M363_parts.pdf')
            parts_guides()



        elif model_number == '20':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2300-2700/Parts Guide/Complete Parts Guide - Revised Nov 11.pdf')
            parts_guides()
        elif model_number == '21':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2310-3111/MX-2310_parts.pdf')
            parts_guides()
        elif model_number == '22':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2314-2614-3114/Parts/MX2614N-MX3114N Parts May 2017.pdf')
            parts_guides()
        elif model_number == '23':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2314-2614-3114/Parts/MX2614N-MX3114N Parts May 2017.pdf')
            parts_guides()
        elif model_number == '24':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2314-2614-3114/Parts/MX2614N-MX3114N Parts May 2017.pdf')
            parts_guides()
        elif model_number == '25':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2600-3100/Parts Manual/MX2301-MX2600-MX3100 Complete Parts Guide.pdf')
            parts_guides()
        elif model_number == '26':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2610-3110-3610/Parts Manual/MX2610N-MX3110N-MX3610N Parts March 12.pdf')
            parts_guides()
        elif model_number == '27':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2630/parts guide.pdf')
            parts_guides()
        elif model_number == '28':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2640-3140-3640/MX-2640-3140-3640 - Main Unit Parts Guide -DEC12.pdf')
            parts_guides()
        elif model_number == '29':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-4112N_MX-5112N/MX4112-5112_PG.pdf')
            parts_guides()
        elif model_number == '30':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 4140-5141/Parts Guide.pdf')
            parts_guides()



        elif model_number == '31':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/MX5050-MX6050_parts.pdf')
            parts_guides()
        elif model_number == '32':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 3070-3570-4070/Parts Guide.pdf')
            parts_guides()
        elif model_number == '33':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5070/mx4070n-mx-5070__parts.pdf')
            parts_guides()
        elif model_number == '34':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 6240-7040/Parts Guide.pdf')
            parts_guides()
        elif model_number == '35':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 6500-7500/MX-6500_parts.pdf')
            parts_guides()
        elif model_number == '36':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-6580/MX-6580_7580_parts_guide.pdf')
            parts_guides()

        elif model_number == '40':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M1205/MX-M1205_parts.pdf')
            parts_guides()
        elif model_number == '41':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-B355W_MX-B455W/MX-B355W_MX-B455W_parts.pdf')
            parts_guides()
        elif model_number == '42':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX M364/MXM364-M365-M464-M465-M564-M565_PG.pdf')
            parts_guides()
        elif model_number == '43':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX M283-363-453-503/Parts Guide/Revised Parts Guide Main Machine - Dec 10.pdf')
            parts_guides()
        elif model_number == '44':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M904/MXM904-M1054-M1204_PG.pdf')
            parts_guides()
        elif model_number == '999':
            main_menu()
        else:
            print(model_number, 'IS NOT VALID!')
            input('ENTER to continue...')
            parts_guides()
    except ValueError:
        parts_guides()


# function to find peripheral manuals
# phil welsby 8th december


# sharp peripherals function
def peripherals():


    import os
    import webbrowser

    # function to clear screen
    def wiper():
        print('\n' * 100)
    # clear screen
    wiper()

    # opening peripherals

    print('''\t\t\t\t\t\t\t\t\t***SHARP PERIPHERALS MENU***\n\n\n
\t\t\t\t(1) MX-DE12\tMX-DE13\tMX-DE14 service
\t\t\t\t(2) MX-DE12\tMX-DE13\tMX-DE14 parts
\t\t\t\t(3) MX-TR19 parts
\t\t\t\t(4) MX-TR19 N parts
\t\t\t\t(5) MX-DE28 service
\t\t\t\t(6) MX-DE28 parts
\t\t\t\t(7) MX-DE28N service
\t\t\t\t(8) MX-DE28N parts
\t\t\t\t(9) MX-FN10 service
\t\t\t\t(10) MX-FN10 parts
\t\t\t\t(11) MX-BM50 service
\t\t\t\t(12) MX-BM50 parts
\t\t\t\t(13) MX-BM50 installation
\t\t\t\t(14) MX-FN27N service
\t\t\t\t(15) MX-FN27N parts
\t\t\t\t(16) MX-FN28 MX-FN29\tMX-PN15 service
\t\t\t\t(17) MX-FN28 MX-FN29\tMX-PN15(A/B/C/D) parts
\t\t\t\t(18) MX-FN21 MX-FN22 service
\t\t\t\t(19) MX-FN21 MX-FN22 parts
\t\t\t\t(20) MX-FX11 service

\t\t\t\t(999) Exit''')





    # path of HDD containing Sharp Manuals
    # /media/phil/Phil_Welsby/Manufacturers/Sharp

    # get input from user
    model_number = None
    model_number = input('\n\n\n\n\nEnter your choice: ')
    #print('Your choice was', model_number)


    try:
        # main program
        if model_number == '1':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-DE12_DE13_DE14/MXDE12-DE13-DE14_service_manual.pdf')
            peripherals()
        elif model_number == '2':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-DE12_DE13_DE14/MX-DE12-DE13-DE14_parts.pdf')
            peripherals()
        elif model_number == '3':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-TR19/MX-TR19_parts.pdf')
            peripherals()
        elif model_number == '4':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-TR19/MX-TR19_N_parts.pdf')
        elif model_number == '5':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-DE28/MX-DE28_SM.pdf')
            peripherals()
        elif model_number == '6':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-DE28/mxde28_pg.pdf')
            peripherals()
        elif model_number == '7':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-DE28/MX-DE28N_SM.pdf')
            peripherals()
        elif model_number == '8':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-DE28/MX-DE28N_parts.pdf')
            peripherals()
        elif model_number == '9':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-FN10/MXFN10-PNX5A-B-C-D-RBX1_SM_GB.pdf')
            peripherals()
        elif model_number == '10':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-FN10/mxfn10_parts.pdf')
            peripherals()
        elif model_number == '11':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-BM50/MXBM50-FD50-TM50-CF50_SM.pdf')
            peripherals()
        elif model_number == '12':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-BM50/MX-BM50_parts.pdf')
            peripherals()
        elif model_number == '13':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-BM50/MX-BM50_installation_manual.pdf')
            peripherals()
        elif model_number == '14':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-FN27/MX-FN27_service.pdf')
            peripherals()
        elif model_number == '15':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-FN27/MX-FN27_parts.pdf')
            peripherals()
        elif model_number == '16':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-FN28/MX-FN28_sevice_manual.pdf')
            peripherals()
        elif model_number == '17':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-FN28/MX-FN28_parts_manual.pdf')
            peripherals()
        elif model_number == '18':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-FN21/mx-fn21_mx-fn22_service.pdf')
            peripherals()
        elif model_number == '19':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-FN21/mx-fn21_mx-fn22_parts.pdf')
            peripherals()
        elif model_number == '20':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-FX11/00ZMXFX11_S2E.pdf')
            peripherals()
        elif model_number == '999':
            main_menu()
        else:
            print(model_number, 'IS NOT VALID!')

            input('ENTER to continue...')
            peripherals()
    except ValueError:
        peripherals()


    # short script to display IP addresses of customer machines
    # phil welsby 14th december 2018



##def ast_ip():
##    #clear screen
##    def wiper():
##        print('\n' * 100)
##    wiper()
##
##    # open file containing IP addresses
##    ip_address_file = open('/home/phil/Documents/IP_ADDRESSES', 'r')
##    whole_file = ip_address_file.read()
##    print(whole_file)
##    ip_address_file.close()
##    input('Enter to continue')
##    main_menu()

def ip():
    #clear screen
    def wiper():
        print('\n' * 100)
    wiper()

    # sub menu fo ip addresses
    print('''\t\t\t\t\t\t\t\tIP ADDRESS SUB MENU\n\n\n\n
\t\t\t\t\t(1) AST
\t\t\t\t\t(2) Palletower
\t\t\t\t\t(3) Oxley
\t\t\t\t\t(4) Borough Care


''')
    ip_choice = input('Enter your selection then press ENTER...')
    if ip_choice == '1':
        ip_file = open('/home/phil/Documents/AST_IP_ADDRESSES')
        ip_file_whole = ip_file.read()
        print(ip_file_whole)
        ip_file.close()
        input('Enter to continue...')
        main_menu()
    elif ip_choice == '2':
        ip_file = open('/home/phil/Documents/PALLETOWER_IP_ADDRESSES')
        ip_file_whole = ip_file.read()
        print(ip_file_whole)
        ip_file.close()
        input('Enter to continue...')
        main_menu()
    elif ip_choice == '3':
        ip_file = open('/home/phil/Documents/OXLEY_IP_ADDRESSES')
        ip_file_whole = ip_file.read()
        print('\n\n', ip_file_whole)
        ip_file.close()
        input('Enter to continue...')
        main_menu()
    elif ip_choice == '4':
        ip_file = open('/home/phil/Documents/BOURGHCARE_IP_ADDRESSES')
        ip_file_whole = ip_file.read()
        print('\n\n', ip_file_whole)
        ip_file.close()
        input('Enter to continue...')
        main_menu()
    else:
        print(ip_choice, 'is not a valid choice')
        input()
        main_menu()




  # short script to open a text file containig a list of simulation codes for Sharp MFP's

def simulation():
    #clear screen
    def wiper():
        print('\n' * 100)
    wiper()



    #open file containing list of simulation codes
    simulation_file = open('/home/phil/Documents/SIMULATION', 'r')
    simulation_whole_file = simulation_file.read()
    print(simulation_whole_file)
    simulation_file.close()
    input('Enter to continue...')
    main_menu()

   # short script to open a text file containig a list of error codes for Sharp MFP's

def error_codes():
    #clear screen
    def wiper():
        print('\n' * 100)
    wiper()

    #open file containing list of error codes
    error_codes_file = open('/home/phil/Documents/ERROR_CODES', 'r')
    error_codes_whole_file = error_codes_file.read()
    print(error_codes_whole_file)
    error_codes_file.close()
    input('Enter to continue...')
    main_menu()


    # short script to open instructions on how to instaal a LAMP stack on a araspberry pi

def lamp():
    #clear screen
    def wiper():
        print('\n' * 100)
    wiper()

    #open file containing instructions and print to screen
    lamp_file = open('/home/phil/Documents/LAMP_stack_on_raspberry_Pi3', 'r')
    lamp_whole_file = lamp_file.read()
    print(lamp_whole_file)
    lamp_file.close()
    input('Enter to continue...')
    main_menu()


def l4_error():
    #clear screen
    def wiper():
        print('\n' * 100)
    wiper()

    #open file containing L4-17 L4-18 price comparison and print to screen
    l4_file = open('/home/phil/Documents/L4-17_L4-18_parts_cost_comparison', 'r')
    l4_whole_file = l4_file.read()
    print(l4_whole_file)
    l4_file.close()
    input('\n\nEnter to continue...')
    main_menu()

def Office365():
    #clear screen
    def wiper():
        print('\n' * 100)
    wiper()

    #open file containing office 365 email settings
    office365_file = open('/home/phil/Documents/office365_email_settings', 'r')
    office365_whole_file = office365_file.read()
    print(office365_whole_file)
    office365_file.close()
    input('\n\nEnter to continue...')
    main_menu()

def uart_jmw():
    #clear screen
    def wiper():
        print('\n' * 100)
    wiper()
    uart_file = open('/home/phil/Documents/UART_on_MX-FN21', 'r')
    uart_file_whole = uart_file.read()
    print(uart_file_whole)
    uart_file.close()
    input('\n\nEnter to continue...')
    main_menu()

def full_cal():
    #clear screen
    def wiper():
        print('\n' * 100)
    wiper()
    full_cal_file = open('/home/phil/Documents/full_calibration', 'r')
    full_cal_file_whole = full_cal_file.read()
    print(full_cal_file_whole)
    full_cal_file.close()
    input('Enter to continue...')
    main_menu()

def lex_acronyms():
    #clear screen
    def wiper():
        print('\n' * 100)
    wiper()
    lex_acron_file = open('/home/phil/Documents/lexmark_acronyms', 'r')
    lex_acron_file_whole = lex_acron_file.read()
    print(lex_acron_file_whole)
    input('Enter to continue...')
    main_menu()

def FF00():
    #clear screen
    def wiper():
        print('\n' * 100)
    wiper()
    ff00 = open('/home/phil/Documents/MX-6500_double_feed_sensor_notes.txt', 'r')
    ff00_whole = ff00.read()
    print(ff00_whole)
    input('Enter to continue...')
    main_menu()


def Maintenance_Codes():
    #clear screen
    def wiper():
        print('\n' * 100)
    wiper()
    maintenance_codes = open('/home/phil/Documents/maintenance_codes', 'r')
    maintenance_codes_whole = maintenance_codes.read()
    print(maintenance_codes_whole)
    input('Enter to continue...')
    main_menu()


def LC17_signals():
    # clear screen
    def wiper():
        print('\n' * 100)
    wiper()
    lc_17signals = open('/home/phil/Documents/LC17_signals','r')
    lc_17signals_whole = lc_17signals.read()
    print(lc_17signals_whole)
    input('Enter to continue...')
    main_menu()




main_menu()












