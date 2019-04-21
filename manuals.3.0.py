# 3rd attempt
# 20 april 2019

import os
import webbrowser

# dictionary or models and manuals
request = {'6240H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 6500-7500/Handy Guide Version 3.3.pdf',
           '6500H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 6500-7500/Handy Guide Version 3.3.pdf',
           '7040H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 6500-7500/Handy Guide Version 3.3.pdf',
           '7500H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 6500-7500/Handy Guide Version 3.3.pdf',
           '3050H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/Handy-Guide-Griffin-MX3050N-MX6050N.pdf',
           '3550H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/Handy-Guide-Griffin-MX3050N-MX6050N.pdf',
           '4050H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/Handy-Guide-Griffin-MX3050N-MX6050N.pdf',
           '5050H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/Handy-Guide-Griffin-MX3050N-MX6050N.pdf',
           '6050H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/Handy-Guide-Griffin-MX3050N-MX6050N.pdf',
           '3060H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5070/Handy-Guide-Phoenix-MX3060-MX6070-MX-5070.pdf',
           '3070H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5070/Handy-Guide-Phoenix-MX3060-MX6070-MX-5070.pdf',
           '3560H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5070/Handy-Guide-Phoenix-MX3060-MX6070-MX-5070.pdf',
           '3570H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5070/Handy-Guide-Phoenix-MX3060-MX6070-MX-5070.pdf',
           '4060H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5070/Handy-Guide-Phoenix-MX3060-MX6070-MX-5070.pdf',
           '4070H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5070/Handy-Guide-Phoenix-MX3060-MX6070-MX-5070.pdf',
           '5070H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5070/Handy-Guide-Phoenix-MX3060-MX6070-MX-5070.pdf',
           '6070H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5070/Handy-Guide-Phoenix-MX3060-MX6070-MX-5070.pdf',
           '6580H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-6580/MX-6580_7580_handy_guide.pdf',
           '7580H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-6580/MX-6580_7580_handy_guide.pdf',
           '7090H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-7090_8090/MX-7090_8090_handy_guide.pdf',
           '8090H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-7090_8090/MX-7090_8090_handy_guide.pdf',
          'M3070H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_HandyGuide.pdf',
          'M3570H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_HandyGuide.pdf',
          'M4070H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_HandyGuide.pdf',
          'M5070H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_HandyGuide.pdf',
          'M6070H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_HandyGuide.pdf'}


# function to clear screen
def wiper():
    print('\n' * 100)

# clear screen
wiper()

# get model and type
def main():
    print(''' 
      MMMMMMM   AAAAAA   NN   N   U    U   AAAAAA   L
      M  M  M   A    A   N N  N   U    U   A    A   L
      M  M  M   AAAAAA   N  N N   U    U   AAAAAA   L
      M     M   A    A   N   NN   U    U   A    A   L
      M     M   A    A   N   NN   UUUUUU   A    A   LLLLLL


      FFFFFFF   IIIIII   NN   N   DDDDD    EEEEEE   RRRRR
      F           II     N N  N   D    D   E        R    R
      FFFF        II     N  N N   D    D   EEEE     RRRRRR
      F           II     N   NN   D    D   E        R   R
      F         IIIIII   N   NN   DDDDD    EEEEEE   R    R
''')

    print('''    Key:
    M = Mono
    H = Handy Guide
    S = Sevice Manual
    P = Parts Catalogue\n\n''')
    print('''    Enter the model number.
    supperceeded by an 'M' 
    if it is a mono machine.
    Followed by the manual type 
    an 'H' an 'S' or a 'P'\n
    eg: 3070H would request the MX-3070 handy guide
       M3070H would request the MX-M3070 handy guide\n\n''')

    try:
        choice = input('>>> ')
        choice = choice.upper()
        manual = request[choice]
        webbrowser.open_new(manual)
        input('Enter to continue...')
        wiper()
        main()
    except:
        print('No manual for', choice)
        input('Enter to continue...')
        wiper()
        main()

main()
