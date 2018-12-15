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



\t\t\t\t(30) MX-3050N\tMX-3550N\tMX4050N\t\tMX-5050N\tMX-6050N
\t\t\t\t(31) MX-4070N\tMX-3570N\tMX-3070N\tMX-3560N\tMX-3060N\tMX-4050N\tMX-3550N\tMX-3050N
\t\t\t\t(32) MX-6540FN\tMX-7040N\tMX-6240N



\t\t\t\t(40) MX-M1055\tMX-M1205
\t\t\n\n\n\n\n\t\t\t\t(999) To Exit''')


    # path of HDD containing Sharp Manuals
    # /media/phil/Phil_Welsby/Manufacturers/Sharp

    # get input from user
    model_number = None
    model_number = input('\n\n\n\n\nEnter your choice: ')
    print('Your choice was', model_number)

    try:
        # main program
        if model_number == '1':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M264/MX M264N Parts Guide.pdf')
        elif model_number == '2':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX M283-363-453-503/Parts Guide/MX-M363_parts.pdf')



        elif model_number == '20':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2300-2700/Parts Guide/Complete Parts Guide - Revised Nov 11.pdf')
        elif model_number == '21':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2310-3111/MX-2310_parts.pdf')
        elif model_number == '22':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2314-2614-3114/Parts/MX2614N-MX3114N Parts May 2017.pdf')
        elif model_number == '23':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2314-2614-3114/Parts/MX2614N-MX3114N Parts May 2017.pdf')
        elif model_number == '24':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2314-2614-3114/Parts/MX2614N-MX3114N Parts May 2017.pdf')
        elif model_number == '25':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2600-3100/Parts Manual/MX2301-MX2600-MX3100 Complete Parts Guide.pdf')
        elif model_number == '26':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2610-3110-3610/Parts Manual/MX2610N-MX3110N-MX3610N Parts March 12.pdf')
        elif model_number == '27':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2630/parts guide.pdf')
        elif model_number == '28':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2640-3140-3640/MX-2640-3140-3640 - Main Unit Parts Guide -DEC12.pdf')


        elif model_number == '30':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/MX5050-MX6050_parts.pdf')
        elif model_number == '31':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 3070-3570-4070/Parts Guide.pdf')
        elif model_number == '32':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 6240-7040/Parts Guide.pdf')
        elif model_number == '40':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M1205/MX-M1205_parts.pdf')
        elif model_number == '999':
            wiper()
            print('GOODBYE HAVE A NICE DAY...')
            return
        else:
            print(model_number, 'IS NOT VALID!')

        input('ENTER to continue...')
        parts_guides()
    except ValueError:
        parts_guides()


parts_guides() 
