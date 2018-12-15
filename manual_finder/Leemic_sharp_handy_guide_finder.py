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
\t\t\t\t(27) MX-2640\tMX3140N\t\tMX3640N
\t\t\t\t(28) MX-4112N\tMX-5112N

\t\t\t\t(30) MX-3050N\t\tMX-3550N/MX4050N\tMX-5050N/MX-6050N
\t\t\t\t(31) MX-3060N/MX-3070N\tMX-3560N/3570N\t\tMX-4060N/4070N\t\tMX-5070N/6070N
\t\t\t\t(32) MX-6240N\tMX7040N\t\tMX-6500N\tMX-7500N

\t\t\t\t(40) MX-M904\t\tMX-M1054\t\tMX-M1204\t\tMX-M1055\tMX-M1205
\t\t\t\t(41) MX-M365N\t\tMX-M465N\t\tMX-565
\t\t\t\t(42) MX-M904\t\tMX-M1054\t\tMX-M1024\t\tMX-M1055\tMX-M1205
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
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M264/MX-M264NHandyGuide.pdf')
        elif model_number == '2':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX M283-363-453-503/Handy Guide/Handyguide Version 1 August 2009.pdf')



        elif model_number == '20':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2300-2700/Handy Guide/August 2007 Version 4 revised handy guide (Includes pastel light, Pastel and C-Jupiter).pdf')
        elif model_number == '21':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2310-3111/Handy Guide.pdf')
        elif model_number == '22':
            print('USE MX-2614/3114 Handy Guide')
        elif model_number == '23':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2314-2614-3114/MX2614N-MX3114N462 Handy Guide.pdf')
        elif model_number == '24':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2600-3100/Handy Guides/Revised Handy Guide Version 5 July 2010.pdf')
        elif model_number == '25':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2610-3110-3610/Handy Guide/Handy-Guide-Aries-MX2610-MX3610.pdf')
        elif model_number == '26':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2630/Handy-Guide-Sphinx-MX2630.pdf')
        elif model_number == '27':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2640-3140-3640/MX2640N - MX3140N - MX3640N Handy Guide Version 1 April 2013.pdf')
        elif model_number == '28':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 4112-5112/Handy Guide Ver 1C.pdf')


        elif model_number == '30':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/Handy-Guide-Griffin-MX3050N-MX6050N.pdf')
        elif model_number == '31':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5070/Handy-Guide-Phoenix-MX3060-MX6070-MX-5070.pdf')
        elif model_number == '32':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 6500-7500/Handy Guide Version 3.3.pdf')
        
        elif model_number == '40':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M1205/MXM1205_handy_guide.pdf')
        elif model_number == '41':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M565/Handy-Guide-Orion-Lotus-MXM365N-MXM465N-MXM565N.pdf')
        elif model_number == '42':
            webbrowser.open_new('/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M904/MX-M904_HG.pdf')
        elif model_number == '999':
            wiper()
            print('GOODBYE HAVE A NICE DAY...')
            return
        else:
            print(model_number, 'IS NOT VALID!')

        input('ENTER to continue...')
        handy_guides()
    except ValueError:
        handy_guides()




