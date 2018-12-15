#! /usr/bin/python3
# phil welsby - 18 february 2016

# clear screen
def wiper():
    print('\n' *100)

def carry_on():
    input('Enter to continue...')
    reports()

#! /usr/bin/python3.4
# phil welsby - 19 february 2016

# start menu
def start_menu():
    wiper()
    print('''\t\t\t\t...WELCOME TO A WORLD WITHOUT WINDOWS...\n\n
    \t\t\t   Designed by Phil Welsby.\n\n\n\t\t\t   (c) 2016 PJW products.\n\n\n\n\n\n\n\n\n''')
    print('\t(1)  Input data\n')
    print('\t(2)  Database search\n')
    print('\t(3)  Run Reports\n')
    print('\t(4)  Car Stock\n')
    print('\t(5)  Create Lists\n')
    print('\t(6)  Retrieve job by line number\n\n')
    print('\t(7)  Exit\n\n')


    try:
        choice = ''
        choice = input('\tEnter a number: ')
        choice = int(choice)
        if choice == 1:
            user_input()
        elif choice == 2:
            search()
        elif choice == 3:
            reports()
        elif choice == 4:
            car_stock_menu()
        elif choice == 5:
            lists()
        elif choice == 6:
            job_retreval()
        elif choice == 7:
            return
        else:
            print(choice,'is not a valid option...')
            print()
            input('Press ENTER to continue...')
            start_menu()
    except ValueError:
        start_menu()

from datetime import datetime
now = datetime.now()
def user_input():
    master_text = open("MASTER.txt", "a")

    # get input from the user
    #wiper()
    time = (now.hour, now.minute, now.second)
    date = (now.day, now.month, now.year)
    machine_type = input("Machine type: ")
    fault = input("Fault: ")
    cause = input("Cause: ")
    action = input("Description of work done: ")
    parts = input("Parts: ")
    submit =  input('\n\nENTER y to SUBMIT or ENTER nothing to ABORT...')
    if submit == 'y':
        input('\n\nSUBMITTED')
    else:
        input('\n\nABORTED...')
        start_menu()

    # print the inputted data to the text file MASTER.txt
    print("Date:", date, "Time:", time, "\nMachine type:", machine_type, "\nFault:",fault, "\nCause:",\
    cause, "\nAction:", action, "\nParts:", parts, "\n",file=master_text)

    # close the open file
    master_text.close()
    start_menu() # code added 13/02/2016







    
# get choice from user
def choice():
    r_choice = ('1','2','3', '4','5','6')
    choice = input('\tEnter a number: ')
    if choice in r_choice:
        choice = int(choice)
        print('\n\nYou chose:',choice,'\n')
    else:
        reports()

    if choice == 1:
        machines()
    elif choice == 2:
        faults()
    elif choice == 3:
        causes()
    elif choice == 4:
        actions()
    elif choice == 5:
        parts()
    elif choice == 6:
        start_menu()

# machines
print('\n'*100)
def machines():
    m_count=0
    m_total=0
    line_num=1
    try:
        machines = open('MASTER.txt')
    except:
        input('missing MASTER.txt file... Enter to continue.')
        start_menu()
    for each_line in machines:
        if 'Machine' in each_line:
            print(line_num , each_line, end='')
            m_count+=1
            line_num+=1
            if m_count == 30:
                m_total+=m_count
                print()
                print('sub-Total number of machines:',m_total)
                input()
                wiper()
                print()
                m_count-=m_count

    print('\nTotal number of machines:',m_count+m_total)
    carry_on()


# faults
def faults():
    f_count=0
    f_total=0
    line_num=1
    try:
        faults = open('MASTER.txt')
    except:
        input('missing MASTER.txt file... Enter to continue.')
        start_menu()
    for each_line in faults:
        if 'Fault' in each_line:
            print(line_num, each_line, end='')
            f_count+=1
            line_num+=1
            if f_count == 30:
                f_total +=f_count
                print()
                print('sub-Total number of faults:', f_total)
                input()
                wiper()
                print()
                f_count-=f_count

    print('\nTotal number of faults:',f_count+f_total)
    carry_on()


# causes
def causes():
    c_count=0
    c_total=0
    line_num=1
    try:
        causes = open('MASTER.txt')
    except:
        input('missing MASTER.txt file... Enter to continue.')
        start_menu()
    for each_line in causes:
        if 'Cause' in each_line:
            print(line_num, each_line, end='')
            c_count+=1
            line_num+=1
            if c_count == 30:
                c_total +=c_count
                print()
                print('sub-Total number of causes:', c_total)
                input()
                wiper()
                print()
                c_count-=c_count

    print('\nTotal number of causes:',c_count+c_total)
    carry_on()

# actions
def actions():
    a_count=0
    a_total=0
    line_num=1
    try:
        actions = open('MASTER.txt')
    except:
        input('missing MASTER.txt file... Enter to continue.')
        start_menu()
    for each_line in actions:
        if 'Action' in each_line:
            print(line_num, each_line, end='')
            a_count+=1
            line_num+=1
            if a_count == 30:
                a_total+=a_count
                print()
                print('sub-Total number of actions:', a_total)
                input()
                wiper()
                print()
                a_count-=a_count

    print('Total number of actions:',a_count+a_total)
    carry_on()

# parts
def parts():
    p_count=0
    p_total=0
    line_num=1
    try:
        parts = open('MASTER.txt')
    except:
        input('missing MASTER.txt file... Enter to continue.')
        start_menu()
    for each_line in parts:
        if 'Parts' in each_line:
            print(line_num, each_line, end='')
            p_count+=1
            line_num+=1
            if p_count == 30:
                p_total+=p_count
                print()
                print('sub-Total number of parts:', p_total)
                input()
                wiper()
                print()
                p_count-=p_count


    print('Total number of parts:',p_count+p_total)
    carry_on()











# search
def search():
        wiper()
        choice = 0
        choice = input('DATABASE\nEnter your search... ')
        if choice == '':
            search()
        else:
            master_list = []
            count = 0
            try:
                    data = open('MASTER.txt')
                    for each_line in data:
                            try:
                                    (heading, content) = each_line.split(':', 1)
                                    content = content.strip()
                                    master_list.append(content)
                            except ValueError:
                                    pass
            except IOError:
                    print('file missing')

            for i in master_list:
                if choice in i:
                    count+=1
                    print(i)

            print('\n\ncount =', count)
        input('\nPress ENTER to continue...')
        start_menu()







# reports menu
def reports():
    # print instructions to the screen
    wiper()
    print('\t\t\t***REPORT RUNNER***')
    print('\n\n\n\n\t(1) All Machines\t\t\n')
    print('\t(2) All Faults  \t\t\n')
    print('\t(3) All Causes  \t\t\n')
    print('\t(4) All Actions \t\t\n')
    print('\t(5) All Parts   \t\t\n')
    print('\t(6) Return to Main Menu\n\n')
    choice()

# car stock
def stock():
    print('\n'*100)
    part_number = input('Part number: ')
    quantity = input('Quantity: ')
    description = input('Description: ')
    inventory = open('inventory.txt', 'a')
    submit_abort = input('\n\nY to add stock to inventory   -or Enter to abort... ')

    if submit_abort == 'Y':
        print('PART NUMBER:', part_number, '        QUANTITY = ', quantity, '        DESCRIPTION = ', description , file = inventory)
        inventory.close()
        input('ADDED to inventory...')
        car_stock_menu()
    else:
        car_stock_menu()


def car_stock_menu():
    print('\n'*100)
    print('\t\t\t***CAR STOCK***\n\n\n\n\n')
    print('\t\t\t***IMPORTANT***\n\n\t\t\tALWAYS RUN WITH CAPS LOCK ON...\n\n')
    print('''\t\t(1) Enter stock item into inventory\n 
          \t(2) Search car stock Inventory\n
          \t(3) Return to Main Menu\n\n\n\nEnter choice...''', end = '')
    choice = input()
    if choice == '1':
        stock()
    elif choice == '2':
        car_stock_search()
    elif choice == '3':
        start_menu()
    else:
        car_stock_menu()

# search car stock
def car_stock_search():
        wiper()

        choice = 0
        choice = input('CAR STOCK DATABASE\nEnter your search...\n ')
        if choice == '':
            car_stock_search()
        else:
            stock_master_list = []
            count = 0
            try:
                    data = open('inventory.txt')
                    for each_line in data:
                            try:
                                    (heading, content) = each_line.split(':', 1)
                                    content = content.strip()
                                    stock_master_list.append(content)
                            except ValueError:
                                    pass
            except IOError:
                    print('\n\ninventory.txt file is missing UNABLE to COMPLETE SEARCH...')

            for line in stock_master_list:
                if choice in line:
                    count+=1
                    if count == 40:
                        input('Enter to continue...')
                        count-=count
                    print(line)

            print('\n\nsearch returns ', count, 'find/finds')
        input('\nEnter to continue...')
        car_stock_menu()

# create lists as txt files
# extract info from MASTER.txt and create individual lists
# containing all items for each heading
# 23 february 2016 - phil welsby

def lists():
    try:
        test = open('MASTER.txt')
    except:
        input('\nCannot create lists no MASTER.txt\nEnter to continue...')
        start_menu()

    # test file to print line numbers for each line

    # dates
    count=0
    fout = open('dates.txt', 'w')
    data = open('MASTER.txt')
    for each_line in data:
        if 'Date' in each_line:
            count+=1
            fout.write(str(count))
            fout.write(each_line)
    fout.close()
    data.close()
            
    # machines numbered
    count = 0
    fout = open('machines.txt', 'w')
    data = open('MASTER.txt')
    for each_line in data:
        if 'Machine type' in each_line:
            count +=1
            fout.write(str(count))
            fout.write(each_line)
    fout.close()
    data.close()
    
    # faults numbered
    count = 0
    fout = open('faults.txt', 'w')
    data = open('MASTER.txt')
    for each_line in data:
        if 'Fault' in each_line:
            count +=1
            fout.write(str(count))
            fout.write(each_line)
    fout.close()
    data.close()

    # causes numbered
    count = 0
    fout = open('causes.txt', 'w')
    data = open('MASTER.txt')
    for each_line in data:
        if 'Cause' in each_line:
            count +=1
            fout.write(str(count))
            fout.write(each_line)
    fout.close()
    data.close()

    # actions numbered
    count = 0
    fout = open('actions.txt', 'w')
    data = open('MASTER.txt')
    for each_line in data:
        if 'Action' in each_line:
            count+=1
            fout.write(str(count))
            fout.write(each_line)
    fout.close()
    data.close()

    # parts numbered
    count = 0
    fout = open('parts.txt', 'w')
    data = open('MASTER.txt')
    for each_line in data:
        if 'Parts' in each_line:
            count+=1
            fout.write(str(count))
            fout.write(each_line)
    fout.close()
    data.close()
    start_menu()
    # end of test



# phil welsby - 25 february 2016
# program which scans 5 individual files and retieves data based in the line number
# entered by the user

def job_retreval():
    # clear screen
    wiper()

    # get user input
    line_num = input('Enter line number: ')

    # machines
    request = line_num+'Machine type'
    data = open('machines.txt')
    for each_line in data:
        (heading, content) = each_line.split(':')
        if heading == request:
            print(heading, content, end='')
    data.close()

    # faults
    request = line_num+'Fault'
    data = open('faults.txt')
    for each_line in data:
        (heading, content) = each_line.split(':')
        if heading == request:
            print(heading, content, end='')
    data.close()

    # causes
    request = line_num+'Cause'
    data = open('causes.txt')
    for each_line in data:
        (heading, content) = each_line.split(':')
        if heading == request:
            print(heading, content, end='')
    data.close()

    # actions
    request = line_num+'Action'
    data = open('actions.txt')
    for each_line in data:
        (heading, content) = each_line.split(':')
        if heading == request:
            print(heading, content, end='')
    data.close()

    # parts
    request = line_num+'Parts'
    data = open('parts.txt')
    for each_line in data:
        (heading, content) = each_line.split(':')
        if heading == request:
            print(heading, content, end='')
    data.close()
    input('Enter to continue')
    start_menu()



start_menu()
