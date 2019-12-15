import random
from time import sleep


def wiper():
    print('\n' * 100)
wiper()


print('\t\t\t  A simple game to test your thinking\n')
sleep(2)
print('\t\t\t   Find the number between 1 and 100\n')
sleep(2)
print('\t\t\t         You have 10 attempts\n')
sleep(2)

num = random.randint(1, 100)
count = 1
guess = None


try:

    while guess != num:
        print('Attempt number', count)
        if count < 11:
            guess = int(input('Enter a guess: '))
            count += 1
            if guess > num:
                print('\nLOWER\n')
                sleep(1)
            elif guess < num:
                print('\nHIGHER\n')
                sleep(1)
            else:
                if guess == num:
                    print('Correct the number was ' + str(num) + ' it took you ' + str(count) + ' guesses')
                    break
        else:
            wiper()
            count -= 1
            print('You had ' + str(count) + ' Guesses, and didn\'t get it. The answer was', num)
            print('HOW DO YOU GET DRESSED IN THE MORNING? MUPPET!!!')
            break

except ValueError as e:
    print('ERROR you typed', e)
