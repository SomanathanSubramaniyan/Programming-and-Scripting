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

# Test the function with the following value.
x = 33  # My name is Somanathan, so the first and last letter of my name (S + N = 19 + 14) give the number  33
ans = fib(x)
print("Fibonacci number", x, "is", ans)
