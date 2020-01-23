# 1 jan 2020 - phil welsby
# program that gives a bar chart

from random import randint
import matplotlib.pyplot as plot

def value_count(aValue,aList):
    noccur = 0
    for value in aList :
        if value == aValue :
            noccur += 1
    return noccur

parts = set()
#all_parts = ['mx-312gr', 'mx-510mk', 'mx-51gvba', 'mx-31grsa']
all_parts = ['MX-510B1', 'MX-510TL', 'PSEL-1134FCZZ', 'PSEL1133FCZ1', 'VHi0MFP2504C', 'MX-230B1', 'PHHEZ0844QSZZ',
              'MX-600FB', 'MX-607LH', 'MX-600FB', 'MX-607LH', 'MX-230B1', 'LPLTP0159QSZZ', 'MX-36GRSA', 'MX-36GRSA',
              'MX-36GRSA', 'MX-36GRSA', 'MX-230MK', 'MX-230MK', 'MX-230MK', 'MX-230MK', 'MX-230TL', 'MX-230MK',
              'MX-36GRSA', 'MX-31GRSA', 'MX-31GRSA', 'MX-31GRSA', 'MX-31GRSA', 'MX-510MK', 'MX-510MK', 'MX-510MK',
              'MX-510MK', 'MX-510TL', 'AR-620RT', 'AR-620RT', 'AR-620RT', 'AR-620RT', 'JC90-01063A', 'NROLR2126FCZZ',
              'NROLR2125FCZZ', 'NROLR2120FCZZ', 'NGERH2122FCZZ', 'MX-361FB', 'MX-510LH', 'MX-310B2', 'MX-510WB',
              'NROLR2126FCZZ', 'NROLR2125FCZZ', 'NROLR2120FCZZ', 'KNROLR1311FCZZ', 'KNROLR1311FCZZ', 'KNROLR1312FCZZ',
              'MX-620WB', 'MX-510WB', 'NGERH2122FCZZ', 'MX-230MK', 'MX-230MK', 'MX-230MK', 'MX-36GRSA', 'MX-36GRSA', 'MX-36GRSA',
              'AR-620RT', 'MX-510WB', 'MX-510LH', 'MX-361FB', 'MX-36GRSA', 'MX-36GRSA', 'MX-36GRSA', 'MX-230MK', 'MX-230MK',
              'MX-230MK', 'MX-360WB', 'MX-230LH', 'AR-620RT', 'JC90-01032A', 'JC73-00340A', 'MX-60GRSA', 'MX-607MK',
              'NROLR2126FCZZ', 'NROLR2125FCZZ', 'NROLR2120FCZZ', 'MX-600FB', 'MX-607LH']
for i in all_parts:
    parts.add(i)
x = int(len(parts))

counts =[]

for score in parts:
    counts.append(value_count(score,all_parts))

y=0

for i in parts:
    print(y,i, '= ', counts[y])
    y+=1

plot.bar(range(x), counts, align='center', alpha=0.5)

plot.xticks(range(x))
plot.ylabel('Quantity')
plot.title('Parts Count')

plot.show()
plot.savefig(fname="Parts Count")

#################################################################





