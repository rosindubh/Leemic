# 3rd attempt at writing a manual finder
# this is much simpler
# it uses a key to find the path to the manual
# and then uses that path to open the pdf
# 20 april 2019

from time import sleep
import os
import webbrowser

# dictionary - key is model number and type, value is path to the manual

dict   =  {'2314H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2314-2614-3114/MX2614N-MX3114N462 Handy Guide.pdf',
           '2614H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2314-2614-3114/MX2614N-MX3114N462 Handy Guide.pdf',
           '3114H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2314-2614-3114/MX2614N-MX3114N462 Handy Guide.pdf',
           '4112H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-4112N_MX-5112N/Handy-Guide-Virgo-MX4112-MX5112.pdf',
           '5112H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-4112N_MX-5112N/Handy-Guide-Virgo-MX4112-MX5112.pdf',
           '2640H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 3140/MX2640N - MX3140N - MX3640N Handy Guide.pdf',
           '3140H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 3140/MX2640N - MX3140N - MX3640N Handy Guide.pdf',
           '3640H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 3140/MX2640N - MX3140N - MX3640N Handy Guide.pdf',
           '6240H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 6500-7500/Handy Guide Version 3.3.pdf',
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
           '2630H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2630/Handy-Guide-Sphinx-MX2630.pdf',
           '4141H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 4140-5141/Handy Guide.pdf',
           '5141H': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 4140-5141/Handy Guide.pdf',
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
           '2640S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 3140/MX2640N-MX3140N-MX3640N - Service Manual Complete - Dec 12.pdf',
           '3140S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 3140/MX2640N-MX3140N-MX3640N - Service Manual Complete - Dec 12.pdf',
           '3640S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 3140/MX2640N-MX3140N-MX3640N - Service Manual Complete - Dec 12.pdf',
           '2614S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2314-2614-3114/MX2614N-MX3114N Service.pdf',
           '3114S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2314-2614-3114/MX2614N-MX3114N Service.pdf',
           '2630S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2630/service manual.pdf',
           'SLX4250S': '/media/phil/Phil_Welsby/Manufacturers/Samsung/B2B Technical Product Information/A3 Colour MFP/SL-X4250/SVC_Manual_MX_X4_eng.pdf',
           'SLX4300S': '/media/phil/Phil_Welsby/Manufacturers/Samsung/B2B Technical Product Information/A3 Colour MFP/SL-X4250/SVC_Manual_MX_X4_eng.pdf',
           'SLX4220S': '/media/phil/Phil_Welsby/Manufacturers/Samsung/B2B Technical Product Information/A3 Colour MFP/SL-X4250/SVC_Manual_MX_X4_eng.pdf',
           '4110S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-4112N_MX-5112N/MX4112-5112_SM.pdf',
           '4141S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 4140-5141/Service Manual Revised June 2014.pdf',
           '5141S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 4140-5141/Service Manual Revised June 2014.pdf',
           '4140S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 4140-5141/Service Manual Revised June 2014.pdf',
           '5141S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 4140-5141/Service Manual Revised June 2014.pdf',
           '5110S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-4112N_MX-5112N/MX4112-5112_SM.pdf',
           '4111S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-4112N_MX-5112N/MX4112-5112_SM.pdf',
           '5111S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-4112N_MX-5112N/MX4112-5112_SM.pdf',
           '4112S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-4112N_MX-5112N/MX4112-5112_SM.pdf',
           '5112S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-4112N_MX-5112N/MX4112-5112_SM.pdf',
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
           'FN21S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-FN22/MXFN21-22-PN13_SM_GB.pdf',
           'FN22S': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-FN22/MXFN21-22-PN13_SM_GB.pdf',
           'C4150S': '/media/phil/Phil_Welsby/Manufacturers/Lexmark/C4150/C4150_sm.pdf',
           'C6160S': '/media/phil/Phil_Welsby/Manufacturers/Lexmark/C6160/c6160_sm.pdf',
           'M5255S': '/media/phil/Phil_Welsby/Manufacturers/Lexmark/M52_XX/M52_XX_service.pdf',
           'M5270S': '/media/phil/Phil_Welsby/Manufacturers/Lexmark/M52_XX/M52_XX_service.pdf',
           '3050VS': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX_3050v/mx-3050v_service_manual.pdf',
           '3550VS': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX_3050v/mx-3050v_service_manual.pdf',
           '4050VS': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX_3050v/mx-3050v_service_manual.pdf',
           '3060VS': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX_3050v/mx-3050v_service_manual.pdf',
           '3560VS': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX_3050v/mx-3050v_service_manual.pdf',
           '4060VS': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX_3050v/mx-3050v_service_manual.pdf',
           '3070VS': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX_3050v/mx-3050v_service_manual.pdf',
           '3570VS': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX_3050v/mx-3050v_service_manual.pdf',
           '4070VS': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX_3050v/mx-3050v_service_manual.pdf',
           '5070VS': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX-5050v/MX-5050_5070v_service_manual.pdf',
           '6070VS': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX-5050v/MX-5050_5070v_service_manual.pdf',
           '5050VS': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX-5050v/MX-5050_5070v_service_manual.pdf',
           '6050VS': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX-5050v/MX-5050_5070v_service_manual.pdf',
           'SLX4250P': '/media/phil/Phil_Welsby/Manufacturers/Samsung/B2B Technical Product Information/A3 Colour MFP/SL-X4250/SLX4250Parts.pdf',
           '4110P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-4112N_MX-5112N/MX4112-5112_PG.pdf',
           '5110P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-4112N_MX-5112N/MX4112-5112_PG.pdf',
           '4111P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-4112N_MX-5112N/MX4112-5112_PG.pdf',
           '5111P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-4112N_MX-5112N/MX4112-5112_PG.pdf',
           '4110P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-4112N_MX-5112N/MX4112-5112_PG.pdf',
           '5110P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-4112N_MX-5112N/MX4112-5112_PG.pdf',
           '4112P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-4112N_MX-5112N/MX4112-5112_PG.pdf',
           '5112P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-4112N_MX-5112N/MX4112-5112_PG.pdf',
           '2640P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2640-3140-3640/MX-2640-3140-3640 - Main Unit Parts Guide -DEC12.pdf',
           '2314P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2314-2614-3114/MX2614N-MX3114N Parts - keep for chris.pdf',
           '2614P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2314-2614-3114/MX2614N-MX3114N Parts - keep for chris.pdf',
           '3114P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2314-2614-3114/MX2614N-MX3114N Parts - keep for chris.pdf',
           '3115P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2640-3140-3640/MX-2640-3140-3640 - Main Unit Parts Guide -DEC12.pdf',
           '2615P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2640-3140-3640/MX-2640-3140-3640 - Main Unit Parts Guide -DEC12.pdf',
           '3640P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2640-3140-3640/MX-2640-3140-3640 - Main Unit Parts Guide -DEC12.pdf',
           '3140P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2640-3140-3640/MX-2640-3140-3640 - Main Unit Parts Guide -DEC12.pdf',
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
           '6070VP': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX_3050v/mx-3050v_parts.pdf',
           '5070VP': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX_3050v/mx-3050v_parts.pdf',
           '4070VP': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX_3050v/mx-3050v_parts.pdf',
           '3570VP': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX_3050v/mx-3050v_parts.pdf',
           '3070VP': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX_3050v/mx-3050v_parts.pdf',
           '4060VP': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX_3050v/mx-3050v_parts.pdf',
           '3560VP': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX_3050v/mx-3050v_parts.pdf',
           '3060VP': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX_3050v/mx-3050v_parts.pdf',
           '6050VP': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX_3050v/mx-3050v_parts.pdf',
           '5050VP': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX_3050v/mx-3050v_parts.pdf',
           '4050VP': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX_3050v/mx-3050v_parts.pdf',
           '3550VP': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX_3050v/mx-3050v_parts.pdf',
           '3050VP': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX_3050v/mx-3050v_parts.pdf',
           'M654P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M754/MXM654-MXM754-KB13_PG_.pdf',
           'M754P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M754/MXM654-MXM754-KB13_PG_.pdf',
           'M904P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M904/MXM904-M1054-M1204_PG.pdf',
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
           'M6070P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_parts_manual.pdf',
           'M5070P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_parts_manual.pdf',
           'M4070P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_parts_manual.pdf',
           'M3570P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_parts_manual.pdf',
           'M3070P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_parts_manual.pdf',
           'M6050P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_parts_manual.pdf',
           'M5050P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_parts_manual.pdf',
           'M4050P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_parts_manual.pdf',
           'M3550P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_parts_manual.pdf',
           'M3050P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_parts_manual.pdf',
           'M2630P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-B-W/MX-M3070/MX-M3070_parts_manual.pdf',
           'FN21P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-FN22/MX-FN22_parts.pdf',
           'FN22P': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX-FN22/MX-FN22_parts.pdf',
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
           '2640I': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2640-3140-3640/MX2640N-MX3140N-MX3640N - Installation Manual Complete - Dec 12.pdf',
           '3140I': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2640-3140-3640/MX2640N-MX3140N-MX3640N - Installation Manual Complete - Dec 12.pdf',
           '3640I': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2640-3140-3640/MX2640N-MX3140N-MX3640N - Installation Manual Complete - Dec 12.pdf',
           '2314I': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2314-2614-3114/MX2614N-MX3114N install.pdf',
           '2614I': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2314-2614-3114/MX2614N-MX3114N install.pdf',
           '3114I': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 2314-2614-3114/MX2614N-MX3114N install.pdf',
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
           '3050VI': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX_3050v/mx-3050v_installation_guide.pdf',
           '3550VI': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX_3050v/mx-3050v_installation_guide.pdf',
           '4050VI': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX_3050v/mx-3050v_installation_guide.pdf',
           '3060VI': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX_3050v/mx-3050v_installation_guide.pdf',
           '3560VI': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX_3050v/mx-3050v_installation_guide.pdf',
           '4060VI': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX_3050v/mx-3050v_installation_guide.pdf',
           '3070VI': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX_3050v/mx-3050v_installation_guide.pdf',
           '3570VI': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX_3050v/mx-3050v_installation_guide.pdf',
           '4070VI': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX_3050v/mx-3050v_installation_guide.pdf',
           '5070VI': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX-5050v/MX-5050_5070v_installation_manual.pdf',
           '6070VI': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX-5050v/MX-5050_5070v_installation_manual.pdf',
           '5050VI': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX-5050v/MX-5050_5070v_installation_manual.pdf',
           '6050VI': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX-xx50v_60v_70v/MX-5050v/MX-5050_5070v_installation_manual.pdf',
           '6500I': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 6500-7500/Complete Installation Manual including all Peripherals - Updated May 2014.pdf',
           '7500I': '/media/phil/Phil_Welsby/Manufacturers/Sharp/MX Colour/MX 6500-7500/Complete Installation Manual including all Peripherals - Updated May 2014.pdf',
           'TOUCH': '/home/phil/Documents/Touch_Panel_Operation.pdf'}


# function to clear screen
def wiper():
    '''A function to clear the screen'''
    print('\n' * 100)

# clear screen
wiper()

# main program
def main():
    '''This is the main function, starts the program'''
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
    SHARP MODELS
    M = Mono
    V = 'V' version of Sharp model eg: 3070V
    H = Handy Guide
    S = Sevice Manual
    P = Parts Catalogue
    U = User Manual
    I = Installation Manual
    Touch = Touch Panel Operation
    SAMSUNG MODELS ADD PREFIX ie (SLX)\n\n''')

    print('''    Enter the model number, superceeded by an 'M' if it is a mono machine.
    Followed by a V if it is a Sharp V model
    Then add the manual type, an 'H' an 'S' a 'P' a 'U' or an 'I'\n
    eg: 3070H  would request the MX-3070 handy guide
        M3070H would request the MX-M3070 handy guide
        3070VP would request the MX-3070V parts catalogue
        Note   Handy Guide for 'V' models is the same an 'N' type\n\n''')

    # get user input

    choice = input('>>> ')
    choice = choice .upper()
    if choice == '999':
        print('Goodbye...')
        sleep(1.5)
        wiper()
    elif choice == 'KEYS':
   # elif choice == 'keys' or choice == 'KEYS':	# this is  a hidden command not visible on the openenig credits
        list_of_keys = []                       # it displays a list of all the keys in the dictionary
        for k in dict:
            list_of_keys.append(k)
        list_of_keys.sort()
        for item in list_of_keys:
            print(item)
        input('Enter to continue...')
        wiper()
        main()
    else:
        try:
           # choice = choice.upper()
            manual = dict[choice]
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
