# 3rd attempt at writing a manual finder
# this is much simpler
# it uses a key to find the path to the manual
# and then uses that path to open the pdf
# 20 april 2019

from time import sleep
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
          'M6070H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_HandyGuide.pdf',
          'M654H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M754/Handy-Guide-Taurus-MXM654-MXM754.pdf',
          'M754H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M754/Handy-Guide-Taurus-MXM654-MXM754.pdf',
          'M904H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M904/MX-M904_HG.pdf',
          'M1054H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M904/MX-M904_HG.pdf',
          'M1204H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M904/MX-M904_HG.pdf',
          'M1055H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M904/MX-M904_HG.pdf',
          'M1205H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M904/MX-M904_HG.pdf',
          'M365H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M565/Handy-Guide-Orion-Lotus-MXM365N-MXM465N-MXM565N.pdf',
          'M465H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M565/Handy-Guide-Orion-Lotus-MXM365N-MXM465N-MXM565N.pdf',
          'M565H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M565/Handy-Guide-Orion-Lotus-MXM365N-MXM465N-MXM565N.pdf',

          '6240S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 6240-7040/MX-6240_service_manual.pdf',
          '7040S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 6240-7040/MX-6240_service_manual.pdf',
          '6500S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 6500-7500/MX6500-7500_SM_latest.pdf',
          '7500S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 6500-7500/MX6500-7500_SM_latest.pdf',
          '3050S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 3070-3570-4070/Service Manual (Revised February 2016).pdf',
          '3550S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 3070-3570-4070/Service Manual (Revised February 2016).pdf',
          '4050S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 3070-3570-4070/Service Manual (Revised February 2016).pdf',
          '3060S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 3070-3570-4070/Service Manual (Revised February 2016).pdf',
          '3560S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 3070-3570-4070/Service Manual (Revised February 2016).pdf',
          '4060S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 3070-3570-4070/Service Manual (Revised February 2016).pdf',
          '3070S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 3070-3570-4070/Service Manual (Revised February 2016).pdf',
          '3570S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 3070-3570-4070/Service Manual (Revised February 2016).pdf',
          '4070S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 3070-3570-4070/Service Manual (Revised February 2016).pdf',
          '5070S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/MX-5050_service_manual.pdf',
          '6070S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/MX-5050_service_manual.pdf',
          '5050S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/MX-5050_service_manual.pdf',
          '6050S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/MX-5050_service_manual.pdf',
          '6580S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-6580/MX-6580_7580_service_manual.pdf',
          '7580S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-6580/MX-6580_7580_service_manual.pdf',
          '7090S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-7090_8090/MX-7090_8090_service.pdf',
          '8090S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-7090_8090/MX-7090_8090_service.pdf',
          'M3070S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_service_manual.pdf',
          'M3570S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_service_manual.pdf',
          'M4070S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_service_manual.pdf',
          'M5070S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_service_manual.pdf',
          'M6070S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_service_manual.pdf',
          'M3050S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_service_manual.pdf',
          'M3550S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_service_manual.pdf',
          'M4050S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_service_manual.pdf',
          'M5050S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_service_manual.pdf',
          'M6050S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_service_manual.pdf',
          'M654S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M754/MXM654-M754_SM.pdf',
          'M754S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M754/MXM654-M754_SM.pdf',
          'M904S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M904/MXM904-M1054-M1204_SM.pdf',
          'M1054S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M904/MXM904-M1054-M1204_SM.pdf',
          'M1204S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M904/MXM904-M1054-M1204_SM.pdf',
          'M1055S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M1205/MX-M1205_service_manual.pdf',
          'M1205S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M1205/MX-M1205_service_manual.pdf',
          'M365S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX M364/MX M364-365N Service Manual.pdf',
          'M364S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX M364/MX M364-365N Service Manual.pdf',
          'M465S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX M364/MX M364-365N Service Manual.pdf',
          'M464S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX M364/MX M364-365N Service Manual.pdf',
          'M565S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX M364/MX M364-365N Service Manual.pdf',
          'M564S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX M364/MX M364-365N Service Manual.pdf',
          'M465S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX M364/MX M364-365N Service Manual.pdf',
          'M565S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX M364/MX M364-365N Service Manual.pdf',}


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

#    try:
#        choice = input('>>> ')
#        choice = choice.upper()
#        manual = request[choice]
#        webbrowser.open_new(manual)
#        input('Enter to continue...')
#        wiper()
#        main()
#    except:
#        print('No manual for', choice)
#        input('Enter to continue...')
#        wiper()
#        main()

    choice = input('>>> ')
    if choice == '999':
        print('Goodbye...')
        sleep(3)
        wiper()
    else:
        try:
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
