# program to fing sharp service manuals
# phil welsby - 19th may 2018

import os
import webbrowser

def wiper():
    print('\n' * 100)

wiper()

# menu

print('''
                          SERVICE MANUALS
                          
1) MX-2314N    7) MX-2010U    8) MX-2301N             13) MX-M283 N
   MX-2614N       MX-2310U       MX-2600N/3100N           MX-M363 N/U
   MX-3114N       MX-3111U       MX-2600G/3100G           MX-M453 N/U
                  MX-2610U                                MX-M503 N/U
2) MX-2640        MX-3110U    9) MX-2010U
   MX-3140        MX-3610U       MX-2310U             14) MX-4110N/5110N
   MX-3640                       MX-3111U                 MX-4111N/5111N
                                 MX-2610N                 MX-4112N/5112N
3) MX-3050N/3550N/4050N          MX-3110N
   MX-3060N/3560N/4060N          MX-3610N             15) MX-4140N/5140N
   MX-3070N/3570N/4070N                                   MX-4141N/5141N
                              10) MX-2314N
4) MX-4140N/5140N                 MX-2614N
   MX-4141N/5141N                 MX-3114N

5) MX-C310/C311               11) MX-2640N
   MX-C380/C381                   MX-3140N
   MX-C400/C401                   MX-3640N

6) MX-2300/2700 G             12)  MX-3500N/4500N
   MX-2300/2700 N                  MX-3501N/4501N
   
''')

model_num = None
model_num = input('Enter a catagory number: ')

print('\n\n\nYou selected catagory', model_num, '\n\n\n')
os.chdir('/media/pi/500GB_HDD/manuals/Sharp/SM')

if model_num == '1':
    webbrowser.open_new('MX2614N-MX3114N MX2314 SERVICE MANUAL.pdf')
elif model_num == '2':
    webbrowser.open_new('MX2640-MX3140-MX3640 SM.pdf')
elif model_num == '3':
    webbrowser.open_new('MX-4070SM_S1E.pdf')
elif model_num == '4':
    webbrowser.open_new('MX4140N-4141-5140-MX5141 serv.pdf')
elif model_num == '5':
    os.chdir('/media/pi/500GB_HDD/manuals/Sharp/SM/MXC310-381')
    webbrowser.open_new('MXC310 - MXC381 Service.pdf')
elif model_num == '6':
    os.chdir('/media/pi/500GB_HDD/manuals/Sharp/SM/MX2300-MX2700')
    webbrowser.open_new('MX2300-MX2700 Service Manual.pdf')
elif model_num == '7':
    os.chdir('/media/pi/500GB_HDD/manuals/Sharp/SM/MX2310U-MX3111')
    webbrowser.open_new('MX2310U-MX3111 Service Manual.pdf')
elif model_num == '8':
    os.chdir('/media/pi/500GB_HDD/manuals/Sharp/SM/MX2600-MX3100')
    webbrowser.open_new('MX2600 - MX3100 Service.pdf')
elif model_num == '9':
    os.chdir('/media/pi/500GB_HDD/manuals/Sharp/SM/MX2610N-MX3610N')
    webbrowser.open_new('MX2610N-MX3110N-MX3610N Service Manual.pdf')
elif model_num == '10':
    os.chdir('/media/pi/500GB_HDD/manuals/Sharp/SM/MX-2614 -MX3114')
    webbrowser.open_new('MX2614N-MX3114N177.pdf')
elif model_num == '11':
    os.chdir('/media/pi/500GB_HDD/manuals/Sharp/SM')
    webbrowser.open_new('MX2640-MX3140-MX3640 SM.pdf')
elif model_num == '12':
    os.chdir('/media/pi/500GB_HDD/manuals/Sharp/SM/MX3501-MX4501')
    webbrowser.open_new('MX3501N-MX4501N Service Manual.pdf')
elif model_num == '13':
    os.chdir('/media/pi/500GB_HDD/manuals/Sharp/SM/MXM363-MXM503')
    webbrowser.open_new('MX M363N - Service.pdf')
elif model_num == '14':
    os.chdir('/media/pi/500GB_HDD/manuals/Sharp/SM/MX4112-MX5112')
    webbrowser.open_new('MX4112N - MX5112 Service Manual.pdf')
elif model_num == '15':
    os.chdir('/media/pi/500GB_HDD/manuals/Sharp/SM')
    webbrowser.open_new('MX4140N-4141-5140-MX5141 serv.pdf')

    

    

    
