# 3rd attempt at writing a manual finder
# this is much simpler
# it uses a key to find the path to the manual
# and then uses that path to open the pdf
# 20 april 2019

from time import sleep
import os
import webbrowser

# dictionary - key is model number and type, value is path to the manual

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
           '2651H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_handy_guide.pdf',
           '3051H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_handy_guide.pdf',
           '3551H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_handy_guide.pdf',
           '4051H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_handy_guide.pdf',
           '3061H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-3061/MX-3061_Handy_Guide.pdf',
           '3071H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-3061/MX-3061_Handy_Guide.pdf',
           '3561H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-3061/MX-3061_Handy_Guide.pdf',
           '3571H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-3061/MX-3061_Handy_Guide.pdf',
           '4061H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-3061/MX-3061_Handy_Guide.pdf',
           '4071H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-3061/MX-3061_Handy_Guide.pdf', 

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
           '2651S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_service_manual.pdf',
           '3051S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_service_manual.pdf',
           '3551S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_service_manual.pdf',
           '4051S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_service_manual.pdf',
           '3061S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_service_manual.pdf',
           '3561S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_service_manual.pdf',
           '4061S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_service_manual.pdf',
           '3071S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_service_manual.pdf',
           '3571S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_service_manual.pdf',
           '4071S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_service_manual.pdf',
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
           'M565S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX M364/MX M364-365N Service Manual.pdf',
           'C4150S': '/media/phil/Phil_Welsby/Manufacturers/Lexmark/C4150/C4150_sm.pdf',
           'C6160S': '/media/phil/Phil_Welsby/Manufacturers/Lexmark/C6160/c6160_sm.pdf',
           'M5255S': '/media/phil/Phil_Welsby/Manufacturers/Lexmark/M52_XX/M52_XX_service.pdf',
           'M5270S': '/media/phil/Phil_Welsby/Manufacturers/Lexmark/M52_XX/M52_XX_service.pdf',

           '6240P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 6240-7040/Parts Guide.pdf',
           '7040P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 6240-7040/Parts Guide.pdf',
           '6540P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 6240-7040/Parts Guide.pdf',
           '6500P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 6500-7500/MX-6500_parts.pdf',
           '7500P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 6500-7500/MX-6500_parts.pdf',
           '6070P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/MX5050-MX6050_parts.pdf',
           '5070P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/MX5050-MX6050_parts.pdf',
           '4070P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/MX5050-MX6050_parts.pdf',
           '3570P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/MX5050-MX6050_parts.pdf',
           '3070P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/MX5050-MX6050_parts.pdf',
           '4060P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/MX5050-MX6050_parts.pdf',
           '3560P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/MX5050-MX6050_parts.pdf',
           '3060P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/MX5050-MX6050_parts.pdf',
           '6050P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/MX5050-MX6050_parts.pdf',
           '5050P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/MX5050-MX6050_parts.pdf',
           '4050P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/MX5050-MX6050_parts.pdf',
           '3550P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/MX5050-MX6050_parts.pdf',
           '3050P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/MX5050-MX6050_parts.pdf',
           '6170P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/MX5050-MX6050_parts.pdf',
           '5170P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/MX5050-MX6050_parts.pdf',
           '4170P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/MX5050-MX6050_parts.pdf',
           '6150P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/MX5050-MX6050_parts.pdf',
           '5150P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/MX5050-MX6050_parts.pdf',
           '4150P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/MX5050-MX6050_parts.pdf',
           '3650P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/MX5050-MX6050_parts.pdf',
           '3150P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/MX5050-MX6050_parts.pdf',
           '2650P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-5050/MX5050-MX6050_parts.pdf',
           '6580P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-6580/MX-6580_7580_parts_guide.pdf',
           '7580P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-6580/MX-6580_7580_parts_guide.pdf',
           '7090P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-7090_8090/MX-7090_8090_parts_guide.pdf',
           '8090P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-7090_8090/MX-7090_8090_parts_guide.pdf',
           '6071P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_parts_manual.pdf',
           '5071P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_parts_manual.pdf',
           '4071P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_parts_manual.pdf',
           '4061P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_parts_manual.pdf',
           '3571P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_parts_manual.pdf',
           '3561P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_parts_manual.pdf',
           '3071P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_parts_manual.pdf',
           '3061P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_parts_manual.pdf',
           '6171P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_parts_manual.pdf',
           '5171P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_parts_manual.pdf',
           '4171P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_parts_manual.pdf',
           '3661P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_parts_manual.pdf',
           '3161P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_parts_manual.pdf',
           '2661P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_parts_manual.pdf',
           '6051P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_parts_manual.pdf',
           '5051P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_parts_manual.pdf',
           '4051P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_parts_manual.pdf',
           '3551P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_parts_manual.pdf',
           '3051P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_parts_manual.pdf',
           '2651P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_parts_manual.pdf',
           '6151P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_parts_manual.pdf',
           '5151P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_parts_manual.pdf',
           '4151P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_parts_manual.pdf',
           '3651P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_parts_manual.pdf',
           '2630P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_parts_manual.pdf',
           'M654P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M754/MXM654-MXM754-KB13_PG_.pdf',
           'M754P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M754/MXM654-MXM754-KB13_PG_.pdf',
           'M904': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M904/MXM904-M1054-M1204_PG.pdf',
           'M1054P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M904/MXM904-M1054-M1204_PG.pdf',
           'M1204P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M904/MXM904-M1054-M1204_PG.pdf',
           'M1055P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M1205/MX-M1205_parts.pdf',
           'M1205P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M1205/MX-M1205_parts.pdf',
           'M560P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M565/MXM364-M365-M464-M465-M564-M565_PG.pdf',
           'M460P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M565/MXM364-M365-M464-M465-M564-M565_PG.pdf',
           'M365P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M565/MXM364-M365-M464-M465-M564-M565_PG.pdf',
           'M465P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M565/MXM364-M365-M464-M465-M564-M565_PG.pdf',
           'M565P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M565/MXM364-M365-M464-M465-M564-M565_PG.pdf',
           'M364P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M565/MXM364-M365-M464-M465-M564-M565_PG.pdf',
           'M464P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M565/MXM364-M365-M464-M465-M564-M565_PG.pdf',
           'M564P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M565/MXM364-M365-M464-M465-M564-M565_PG.pdf',

           'M2630U': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_user_manual.pdf',
           'M3050U': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_user_manual.pdf',
           'M3070U': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_user_manual.pdf',
           'M3550U': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_user_manual.pdf',
           'M3570U': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_user_manual.pdf',
           'M4050U': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_user_manual.pdf',
           'M4070U': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_user_manual.pdf',
           'M5050U': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_user_manual.pdf',
           'M5070U': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_user_manual.pdf',
           'M6050U': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_user_manual.pdf',
           'M6070U': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_user_manual.pdf',
           '2651U': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_user_manual.pdf',
           '3561U': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_user_manual.pdf',
           '3051U': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_user_manual.pdf',
           '3571U': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_user_manual.pdf',
           '3061U': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_user_manual.pdf',
           '4051U': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_user_manual.pdf',
           '3071U': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_user_manual.pdf',
           '4061U': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_user_manual.pdf',
           '3551U': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_user_manual.pdf',
           '4071U': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_user_manual.pdf',
           'C4100U': '/media/phil/Phil_Welsby/Manufacturers/Lexmark/C4150/C4100_C4150_user_manual.pdf',
           'C4150U': '/media/phil/Phil_Welsby/Manufacturers/Lexmark/C4150/C4100_C4150_user_manual.pdf',
           '2651I': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_installation_manual.pdf',
           '3051I': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_installation_manual.pdf',
           '3551I': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_installation_manual.pdf',
           '4051I': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_installation_manual.pdf',
           '3061I': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_installation_manual.pdf',
           '3561I': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_installation_manual.pdf',
           '4061I': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_installation_manual.pdf',
           '3071I': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_installation_manual.pdf',
           '3571I': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_installation_manual.pdf',
           '4071I': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-2651/mx4071_installation_manual.pdf',

           'TOUCH': '/home/phil/Documents/Touch_Panel_Operation.pdf'}


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
    P = Parts Catalogue
    U = User Manual
    I = Installation Manual
    Touch = Touch Panel Operation\n\n''')

    print('''    Enter the model number.
    supperceeded by an 'M' 
    if it is a mono machine.
    Followed by the manual type 
    an 'H' an 'S' a 'P' a 'U' or an 'I'\n
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
