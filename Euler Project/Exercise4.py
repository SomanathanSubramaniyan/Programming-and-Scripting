# somu  19-Feb-2018
# Exercise 4 : Least Common Multiple
# https://projecteuler.net/problem=5

J = 10
i = 1

# Reason for incrementing while loop by 10: Any number to be divisible by 10 should end with 0
# J is intialised with 10 because of the above reason
# Multiple of 18: should be divisible by 9
# Multiple of 14: Should be divisible by 7
# Multiple of 6:  Should be divisible by 3
while J != 0:
        if J % 9 == 0 and J % 7 == 0 and J % 3 == 0 and J % 5 == 0:
            for i in range(1,21,1):
                if J % i == 0:
                    if i == 20:
                        finalValue = J
                        J = 0
                        break
                else:
                    J =J+10
                    break
        else:
            J = J + 10
print ("The Smallest possible integer evenly divisible by all number from 1 to 20 is", finalValue)


