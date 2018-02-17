#Somu 17-02-18 
#Project reference : https://projecteuler.net/problem=1

i = int(input ("Enter the Number :"))
J = 1
Total = 0

while J < i:
    if  J % 3 == 0:
        Total = Total + J
    elif J % 5 == 0:
        Total = Total + J
    J = J + 1

print ("The Sum of Mutiples of 3 and 5 below " + str(i) + " :" + str(Total))
