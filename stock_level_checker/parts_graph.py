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
all_parts = ['MX510B1', 'MX510TL', 'PSEL-1134FCZZ', 'PSEL1133FCZ1', 'VHi0MFP2504C', 'MX230B1', 'PHHEZ0844QSZZ',
              'MX-600FB', 'MX-607LH']
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





