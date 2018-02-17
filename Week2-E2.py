stringex = "Somanathan"
print (stringex)

print ("first 5 character","'", stringex[:5],"'", end=" ")
print (" 5th to Last", "'",stringex[5:],"'", end="")
print (stringex[:5]+stringex[5:])

family = ["Anu", "Somu", "Ajay"]

print (  end=" \n" )
print (family[2][0])
print (family[2][1])
print (family[2][2])
print (family[2][3])
print ( end=" \n" )

import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break    # This condition is the correct guess!

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))