# program to open Sharp PDF Handy Guide manuals
# 6th may 2018 - phil welsby

import os
import webbrowser

def wiper():
    print('\n' * 100)

wiper()

# menu
print('''                        Sharp Handy Guides
1) AR-M201      6) MX2301N      12)MX-5500N      17) MX-C310      23) MX-M350U      29) MX-3050N
                   MX2600N         MX-6200N          MX-C311          MX-M450U          MX-3550N
2) AR-M160         MX3100N         MX-7000N          MX-C380                            MX-4050N
   AR-M205                         MX-6201N          MX-C381      24) MX-M550U          MX-5050N
                7) MX-2610N        MX-7001N                           MX-M620U          MX-6050N
3) AR-M236         MX-3110N                      18) MX-M160D         MX-M700U
   AR-M256         MX-3610N     13)MX-5500N          MX-M200D                       30)
   AR-M276                         MX-6200N                       25) MX-M623N          MX-3060N
   AR-M316      8) MX-2614N        MX-7000N      19) MX-M182D         MX-M753N          MX-3070N
                   MX-3114N        MX-6201N          MX-M202D                           MX-3560N
4) MX-1800N                        MX-7001N          MX-M232D     26) MX-M850           MX-3570N
   MX-2300N     9) MX-2640N                                           MX-M950           MX-4060N
   MX-2700N        MX-3140N     14)MX-6240N      20) MX-M260          MX-M1100          MX-4070N
   MX-3500N        MX-3640N        MX-7040N          MX-M310                            MX-5070N
   MX-3501N                                                       27) MX-M904           MX-6070N
   MX-4500N     10)MX-4112N     15)MX-B382       21) MX-M264N         MX-M1054
   MX-4501N        MX-5112N        MX-B382P          MX-M314N         MX-M1204
                                                     MX-M354N
5) MX-2310U     11)MX-4140N     16)MX-C250F                        28) 
   MX-3111U        MX-4141N        MX-C300W      22) MX-M363N          
                   MX-5141N                          MX-M453            
                                                     MX-M503N           

                                                     ''')      
model_num = None
model_num = input('Enter a catagory number: ')

print('\n\n\nYou selected catagory', model_num, '\n\n\n')
os.chdir('/media/pi/500GB_HDD/manuals/Sharp/HG')

if model_num == '1':
    webbrowser.open_new('ARM201.pdf')
elif model_num == '2':
    webbrowser.open_new('ARM205 HG.pdf')
elif model_num == '3':
    webbrowser.open_new('ARM276-236-256-316 HG.pdf')
elif model_num == '4':
    webbrowser.open_new('MX1800-MX2300-MX2700-MX3500-MX3501-MX4500-MX4501.pdf')
elif model_num == '5':
    webbrowser.open_new('MX2310U-MX3111.pdf')
elif model_num == '6':
    webbrowser.open_new('MX2600 - MX3100.pdf')
elif model_num == '7':
    webbrowser.open_new('MX2610N-MX3110N-MX3610N.pdf')
elif model_num == '8':
    webbrowser.open_new('MX2614N-MX3114 HG.pdf')
elif model_num == '9':
    webbrowser.open_new('MX2640-MX3140-MX3640956.pdf')
elif model_num == '10':
    webbrowser.open_new('MX4112N - MX5112N.pdf')
elif model_num == '11':
    webbrowser.open_new('MX4140N-MX5141N-HG.pdf')
elif model_num == '12':
    webbrowser.open_new('MX5500N-MX7000N.pdf')
elif model_num == '13':
    webbrowser.open_new('MX6201N-MX7001N.pdf')
elif model_num == '14':
    webbrowser.open_new('MX6240N-MX7040N HG.pdf')
elif model_num == '15':
    webbrowser.open_new('MX-B382 Handy Guide.pdf')
elif model_num == '16':
    webbrowser.open_new('MXC250 - MXC300671.pdf')
elif model_num == '17':
    webbrowser.open_new('MXC310 - MXC381.pdf')
elif model_num == '18':
    webbrowser.open_new('MX M160D- M200D Handy Guide.pdf')
elif model_num == '19':
    webbrowser.open_new('MXM182-232 handy Guide.pdf')
elif model_num == '20':
    webbrowser.open_new('MXM260-M310 handy guide.pdf')
elif model_num == '21':
    webbrowser.open_new('MXM264 Handy Guide.pdf')
elif model_num == '22':
    webbrowser.open_new('MXM283-363-503 Handy Guide.pdf')
elif model_num == '23':
    webbrowser.open_new('MXM350-450 Handy Guide.pdf')
elif model_num == '24':
    webbrowser.open_new('MXM550-620 Handy Guide.pdf')
elif model_num == '25':
    webbrowser.open_new('MXM623-753 Handy Guide.pdf')
elif model_num == '26':
    webbrowser.open_new('MXM850-950-1100 Handy Guide.pdf')
elif model_num == '27':
    webbrowser.open_new('MX M904 - M1204 HG.pdf')
# number 28 here
elif model_num == '29':
    webbrowser.open_new('Handy-Guide-Griffin-MX3050N-MX6050N.pdf')
elif model_num == '30':
    webbrowser.open_new('Handy-Guide-Phoenix-MX3060-MX6070.pdf')









else:
    print('That CATAGORY is not in the list...')



    
