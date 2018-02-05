# Somu  22-01-2018
# Execution of Ian McLoughlin 's Source code
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
