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

    # opening menu listing handy guides

    print('''\t\t\t\t\t\t\t\t\t***SHARP PERIPHERALS MENU***\n\n\n
\t\t\t\t(1) MX-DE12\tMX-DE13\tMX-DE14 service
\t\t\t\t(2) MX-DE12\tMX-DE13\tMX-DE14 parts
\t\t\t\t(999) Exit''')
 




    # path of HDD containing Sharp Manuals
    # /media/phil/Phil_Welsby/Manufacturers/Sharp

    # get input from user
    model_number = None
    model_number = input('\n\n\n\n\nEnter your choice: ')
    print('Your choice was', model_number)


    try:
        # main program
        if model_number == '1':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-DE12_DE13_DE14/MXDE12-DE13-DE14_service_manual.pdf')
            peripherals()
        if model_number == '2':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-DE12_DE13_DE14/MX-DE12-DE13-DE14_parts.pdf')
            peripherals()




        elif model_number == '999':
            main_menu()
        else:
            print(model_number, 'IS NOT VALID!')

        input('ENTER to continue...')
        peripherals()
    except ValueError:
        peripherals()

peripherals()



