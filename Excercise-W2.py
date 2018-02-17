# Excercise 1 (week1) ::  Somu  :: 22-01-2018
# Adapted from:  Ian McLoughlin 's Source code
# A program that displays Fibonacci numbers.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  return i

# Test the function with the following value.
# My name is Somanathan, so the first and last letter of my name (S + N = 19 + 14) give the number  33

x = 33 
ans = fib(x)
print("Fibonacci number", x, "is", ans)

# Excercise 2 (week2) ::  Somu  :: 29-02-2018
# My Surname is Subramaniyan. 
# The First and Last character digits are summed up. Fibonacci numbers are displayed for that number

name = "Subramaniyan"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)
