from typing import Callable
def log(func: Callable) -> Callable:
  def wrapper(*args, **kwargs) -> Callable:
    print(f"Calling: {func.__name__}")
    print(f"Documentation: {func.__doc__}")
    return func(*args, **kwargs)
  return wrapper


def output(func: Callable) -> Callable:
  def wrapper(*args, **kwargs) -> Callable:
    print(f"Calling: {func.__name__}")
    print(f"Documentation: {func.__doc__}")
    call = func(*args, **kwargs)
    if(type(call) != type(None)):
      print(f"The output of {func.__name__} is {call}")
      
  return wrapper
