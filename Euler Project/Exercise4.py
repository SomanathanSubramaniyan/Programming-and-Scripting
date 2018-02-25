# somu  19-Feb-2018
# Exercise 4 : https://projecteuler.net/problem=5

J = 21
i = 1

while J != 0:
    print(J)
    while i <= 20:
        print (i)
        if J % i == 0:
            if i == 20:
                J=0
                break
            else:
                i = i + 1
        else:
            J=J+1
            i = 1
            break

print ("The Smallest possible integer evenly divisible by all number from 1 to 10 is", J)
