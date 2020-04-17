from Logger import output


@output
def validate(prompt: str, min: int = 0, max: int = float('inf')) -> int:
    """
    Validate the user input and ensure the user input a number between the minimum and maximum values. Will keep trying if the user inputs an invalid character or a number out of the range.
    :param prompt – the prompt to ask the user in the user input
    :param min – the minimum value – defaults to 0
    :param max – the maximum value – defaults to infinity
    :return int of choice
    """
    try:
        val = int(input(prompt))
        if(val > max or val < min):
            raise TypeError
        return val
    except TypeError:
        """
        out of range failure caught
        """
        print(f"Value not between {min} and {max}")
        return validate(prompt, min, max)
    except ValueError:
        """
        Invalid type caught
        """
        print("Value inputted was not a number! Try again!")
        return validate(prompt, min, max)
