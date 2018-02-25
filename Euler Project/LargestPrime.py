# Somu 17 Feb 2018
# Largest Prime number : https://projecteuler.net/problem=3

# Function to validate if a given number is a  prime number
def cprime(i):
    J = 2
    Prime = "yes"
    while J < i:
        if (i % J == 0):
            Prime = "no"
            break
        J = J + 1

    if Prime == "no":
        return Prime
    else:
        return Prime

# Accept a integer number    
i = int (input ("Input a Number to identify its prime factors : "))
J = 2
Factor =""

while (J  < i) :
    if (i % J == 0):
        if (cprime(J) == "yes") :
            if Factor == "":
                Factor = Factor + str(J) 
            else:
                Factor = Factor + ", " + str(J) 
    J = J+1

Factor = Factor 
print (Factor)




