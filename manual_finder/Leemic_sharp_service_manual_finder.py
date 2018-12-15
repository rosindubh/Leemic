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


\t\t\t\t(30) MX-3050N/3550N/4050N\tMX-3060N/3560N/4060N\t\tMX-3070N/3570N/4070N
\t\t\t\t(31) MX-5050N\t\tMX-6050N\t\tMX5070N\t\t\tMX-6070N
\t\t\t\t(32) MX-6240N\t\tMX-7040N



\t\t\t\t(40) MX-M1055\tMX-M1205
\t\t\n\n\n\n\n

\t\t\t\t(999) To Exit''')
    




    # path of HDD containing Sharp Manuals
    # /media/phil/Phil_Welsby/Manufacturers/Sharp

    # get input from user
    model_number = None
    model_number = input('\n\n\n\n\nEnter your choice: ')
    print('Your choice was', model_number)


    try:
        # main program
        if model_number == '1':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M264/MX M264N Service Manual.pdf')
        elif model_number == '2':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX M283-363-453-503/Service Manual/Updated Service Manual - June 10.pdf')
        elif model_number == '20':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2300-2700/Service Manual/2300_Service Manual.pdf')
        elif model_number == '21':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2310-3111/Service Manual - Revised May 2011.pdf')
        elif model_number == '22':
            print('USE MX-2614N/3114N')
        elif model_number == '23':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2314-2614-3114/MX2614N-MX3114N Service.pdf')
        elif model_number == '24':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2600-3100/Service Manual/MX2600 - MX3100 Service (complete).pdf')
        elif model_number == '25':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2610-3110-3610/Service Manual/MX2310-MX2610-MX3110 Revised Feb 2011 - Service Manual - Complete.pdf')
        elif model_number == '26':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2630/service manual.pdf')
        elif model_number == '27':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2640-3140-3640/MX2640N-MX3140N-MX3640N - Service Manual Complete - Dec 12.pdf')
        elif model_number == '28':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 4112-5112/Service Manual - Complete - Nov 2012.pdf')
        elif model_number == '30':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 3070-3570-4070/Service Manual (Revised February 2016).pdf')
        elif model_number == '31':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/MX-5050_service_manual.pdf')
        elif model_number == '32':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 6240-7040/MX-6240_service_manual.pdf')
        elif model_number == '40':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M1205/MX-M1205_service_manual.pdf')

        elif model_number == '999':
            wiper()
            print('GOODBYE HAVE A NICE DAY...')
            return
        else:
            print(model_number, 'IS NOT VALID!')

        input('ENTER to continue...')
        service_manuals()
    except ValueError:
        service_manuals()



service_manuals()
