from Logger import log, output

@output
def single_digit_of_all_numbers(n: int, s: int = 0) -> int:
  """
  Calculate the single digit sum of all the digits
  :param n – current number
  :param s – sum
  :return Integer of total sum of all digits down to single digit
  """
  if(n == 0):
    if(s > 10):
      return single_digit_of_all_numbers(s, 0)
    return s
  else:
    return single_digit_of_all_numbers(n // 10, s + n % 10)

