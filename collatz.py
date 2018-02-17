# Somu 05-02-2018
# Collatz: https://en.wikipedia.org/wiki/Collatz_conjecture


# Function to calcuate Collatz conjecture
def collatz(number):
    if number % 2 == 0:
        number = number/2
    elif number % 2 == 1:
        number = 3*number+1
    return number

# Enter the number to display the collatz conjecture
Limit = int(input("Enter a number "))
while Limit > 1 :
    print ( Limit )
    Limit = collatz(Limit)     
print (Limit )
