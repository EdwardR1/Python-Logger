from math_example import get_sum_factorial_of_digits
from recursive_digits_example import single_digit_of_all_numbers
from input_validation import validate

def iterative_function_calling():
    """
    Example that calls other functions 
    """
    get_sum_factorial_of_digits(123456)


def recursive_function_calling():
    """
    Recursive example of the logger being used when the function calls itself
    """
    single_digit_of_all_numbers(123456)


def exception_function_calling():
    """
    Example with an exception handled
    """
    validate("Please input a number between 0 and 5: ", 0, 5)

def main():
    # iterative_function_calling()
    # recursive_function_calling()
    exception_function_calling()
main()
