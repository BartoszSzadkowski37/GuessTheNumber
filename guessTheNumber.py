#guessTheNumber

'''

1. User enter range
2. Generate random number from the range
3. User enters the number
4. Check if it's correct
5. Yes --> print and number of tries
6. No --> Back to 3. print number of tries

'''
import random
import pyinputplus as pyip

min = 0
max = 0

print('Enter the range:')
min = pyip.inputInt('From which number (include in range):')
max = pyip.inputInt('To which number (include in range):')

if min < max:
    randomNumber = random.randint(min,max)
else:
    randomNumber = random.randint(max, min)
tries = 0
game = True

while game:

    tries += 1
    answer = pyip.inputInt('Guess the Number: ', min=min, max=max)
    if answer == randomNumber:
        print('You win!, number is: %s, it is your %s tries.' % (randomNumber, tries))
        game = False
    else:
        print('Wrong!, it is your %s tries.' % tries)

