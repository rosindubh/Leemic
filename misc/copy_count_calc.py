# program to work out copy count between a previous vist and current
# 15 feb 2020 - phil welsby

def wiper():
    print('\n' * 100)
wiper()

old_bk = int(input('Enter previous black counter: '))
old_col = int(input('Enter previous colour counter: '))
new_bk = int(input('Enter current black meter: '))
new_col = int(input('Enter current colour meter: '))

total_bk = new_bk - old_bk
total_col = new_col - old_col

total_count = total_bk + total_col

print('Total Black  =', total_bk)
print('Total Colour =', total_col)
print('Total Count  =', total_count)
