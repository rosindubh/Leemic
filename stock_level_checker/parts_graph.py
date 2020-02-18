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
              'NROLR2126FCZZ', 'NROLR2125FCZZ', 'NROLR2120FCZZ', 'MX-600FB', 'MX-607LH', 'MX-62GRSA', 'MX-750MK', 'AR-620RT',
              'AR-620RT', 'MX-850RT', 'MX-850RT', 'MX-C30GVM', 'MX-C30DR', 'MX-C32U1', 'NROLR1790FCZZ', 'NROLR1791FCZZ',
              'NROLR1792FCZZ', 'NROLR0212QSA1', 'JC93-01287A', 'NROLR2120FCZZ', 'NROLR2125FCZZ', 'NROLR2126FCZZ',
              'MX-36GRSA', 'MX-230MK', 'AR-620RT', 'MX-60GRSA', 'MX-607MK', 'MX-60GUSA', 'MX-601HB', 'PSHEZ7020FCZZ',
              'MX-230LH', 'MX-360WB','MX-60GRSA', 'MX-61GVBA', 'MX-607MK', 'MX-850DF', 'MX-31GRSA', 'MX-510MK', 'AR-620RT',
              'MX-510TL', '72K0FK0', '41X0929', 'MX-61GVBA', 'MX-60GRSA', 'MX-607MK', 'MX-607LH', 'MX-600FB', 'MX-950HK',
              'JC91-01024A', 'JC91-01024A', 'JC90-01032A', 'JC91-01024A', 'MX-60GRSA', 'MX-407MK', 'JC90-01063B', 'JC97-04471A',
              'JC97-04099A', 'JC90-04099A', 'MX-560UH', 'MX-560LH', 'MX-560WC', 'MX-850DF', 'MX-600FB', 'MX-607LH', 'NROLR2120FCZZ',
              'NROLR2125FCZZ', 'NROLR2126FCZZ', 'JC93-00794A', 'MX-607B1', 'MX-607TL', 'KNROLR1311FCZZ', 'KNORLR1311FCZZ', 'KNORLR1312FCZZ
              'GCAB-1353FCB1''
       ]
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





