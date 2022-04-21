# Countdown Timer

import time

print('Welcome to Timer Countdown!\n')

print('This timer will count down by seconds')
number = input('Enter a whole number to countdown: ')
number = int(number)
print('Starting Timer . . .')
time.sleep(2)

while number > 0:
    print(number)
    time.sleep(1)
    number = number - 1
print('TIMER ENDED')
