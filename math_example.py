from Logger import log, output

@log
def factorial(n: int) -> int:
  """
  Solve the factorial of some number
  :param n – the number to get the factorial of
  :return the factorial of n
  """
  f = 1
  for i in range(1, n + 1):
    f *= i
  return f

@log
def getDigits(n: int) -> list:
  """
  Return a list of the digits of a number
  :param n – the number to find the digits of
  :return a list of the digits
  """
  digits = []
  while(n > 0):
    digits.append(n % 10)
    n //= 10
  digits = digits[::-1]
  return digits


@output
def get_sum_factorial_of_digits(n: int) -> int:
  """
  Get the sum of the factorial of each digit in a given number
  :param n – the number to find the value of
  :return the sum of the factorial of all the digits
  """
  return sum(map(factorial, getDigits(n)))




