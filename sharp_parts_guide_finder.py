# program to find Sharp parts catalogues
# phil welsby - 21st may 2018

import os
import webbrowser

def wiper():
    print('\n' * 100)

wiper()

# menu

print('''
                    PARTS GUIDES\n
1) DX-C310/C311             7) MX-2314N                 14) MX-6540FN
   DX-C380/C381                MX-2614N/3114N               MX-7040N/6240N
   DX-C400/C401                MX-3115N/2615N               MX-MF10,MX-LT10
                               MX-3640N/3640FN              MX-EB15,MX-KB13
2) MX-2300G]MX-2700G           MX-3140N/3140FN              MX-TU14,MX-TR14
   MX-2300N]MX-2700N           MX-2640N/2640FN
   MX-1800N                                             15) MX-M283N/M363N/M453N
                            8) MX-3500FN/MX-3500N           MX-M503N/M282N/M362N
3) MX-2310F/2311FN/2610FN      MX-3501FN/MX-3501N           MX-M452N/M502N
   MX-3110FN/3610FN            MX-4500FN/MX-4500N
   MX-3111F/3112FN             MX-4501FN/MX-4501N
   MX-2310U/2610N
   MX-3110N/3610N           9) MX-4100FN/MX-5000FN
   MX-2010U/1810U/3111U        MX-4101FN/MX-5001FN
                               MX-4100N/MX5000N
                               MX-4101N/MX-5001N
4) MX-2600FG/MX-2600FN         MX-3600FN/MX-KBX2
   MX-3100FG/MX-3100FN
   MX-2600N/MX-2600G        10) MX-4110FN/MX-5110FN
   MX-3100N/MX-3100G            MX-4111FN/MX-5111FN
   MX-2301FN/MX-2301N           MX-4110N/MX-5110N
   MX-KBX1                      MX-4111N/MX-5111N
                                MX-4112N/MX-5112N
5) MX-2310F/2311FN/2610FN       MX-KB11
   MX-3110FN/3610FN
   MX-3111F/3112FN          11) MX-4140FN/MX-5140FN
   MX-2310U                     MX-4141FN/MX-5141FN
   MX-3110N                     MX-4140N/MX-5140N
   MX-2010U/1810U/3111U         MX-4141N/MX-5141N
   MX-TR12/TR13                 MX-K11N/MX-EB11
   MX-KB11
   MX-RP12/HD10/HD11/VR11   12) MX-5500N
                                MX-6200N
6) MX-2314N                     MX-7000N
   MX-2614N/3114N
   MX-3115N/2615N           13) MX-6201N
   MX-3640N/3640FN              MX-7001N
   MX-3140N/3140FN
   MX-2640N/2640FN          
''')                          

# GET INPUT

model_num = None
model_num = input('\nEnter a catagory number: ')

print('\n\n\nYou selected catagory', model_num, '\n\n\n')
os.chdir('/media/pi/500GB_HDD/manuals/Sharp/PM')

# GET MANUAL BASED ON INPUT

if model_num == '1':
    webbrowser.open_new('DXC310-DXC401 Parts.pdf')
elif model_num == '2':
    webbrowser.open_new('MX1800-MX2300-MX2700.pdf')
elif model_num == '3':
    webbrowser.open_new('MX2310U-MX3111.pdf')
elif model_num == '4':
    webbrowser.open_new('MX2600 - MX3100.pdf')
elif model_num == '5':
    webbrowser.open_new('MX2610N-MX3110N-MX3610N.pdf')
elif model_num == '6':
    webbrowser.open_new('MX2614N-MX3114N Parts.pdf')
elif model_num == '7':
    webbrowser.open_new('MX2640-MX3140-MX3640 Parts.pdf')
elif model_num == '8':
    webbrowser.open_new('MX3501-MX4501.pdf')
elif model_num == '9':
    webbrowser.open_new('MX4100-MX5000.pdf')
elif model_num == '10':
    webbrowser.open_new('MX4112N - MX5112N.pdf')
elif model_num == '11':
    webbrowser.open_new('MX4140N-4141-5140-MX5141N-parts-.pdf')
elif model_num == '12':
    webbrowser.open_new('MX5500N-MX7000N.pdf')
elif model_num == '13':
    webbrowser.open_new('MX6201-MX7001 parts.pdf')
elif model_num == '14':
    webbrowser.open_new('MX6240N - MX7040N pm.pdf')
elif model_num == '15':
    os.chdir('/media/pi/500GB_HDD/manuals/Sharp/PM/MXM282-503MXM')
    webbrowser.open_new('MX M363N - Parts.pdf')
##elif model_num == '16':
##    webbrowser.open_new('MX2310U-MX3111.pdf')
##elif model_num == '17':
##    webbrowser.open_new('MX2310U-MX3111.pdf')
##elif model_num == '18':
##    webbrowser.open_new('MX2310U-MX3111.pdf')
##elif model_num == '19':
##    webbrowser.open_new('MX2310U-MX3111.pdf')
##elif model_num == '20':
##    webbrowser.open_new('MX2310U-MX3111.pdf')
##elif model_num == '21':
##    webbrowser.open_new('MX2310U-MX3111.pdf')
