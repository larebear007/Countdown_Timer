# Countdown Timer

import time

print('Welcome to Timer Countdown!\n')

print('This timer will count down by seconds')

# Retrieving countdown #, while checking for numeric value & looping if not
while True:
    number = input('Enter a whole number to countdown: ')
    if number.isnumeric():
        number = int(number)
        print('Starting Timer . . .')
        time.sleep(2)
        break
    else:
        print('Please enter a number for the countdown timer.')

# Timer display
while number > 0:
    print(number)
    time.sleep(1)
    number = number - 1

print('TIMER ENDED !')
