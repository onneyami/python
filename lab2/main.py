# №4 function divide(a, b) that returns the result of dividing a by b
def divide(a, b):
    return a / b

# №8 function get_positive_integer() that prompts the user to enter a positive number
def get_positive_integer():
    input("Enter positive integer: ")
    if int(input("Enter positive integer: ")) < 0:
        return int(input("Enter positive integer: "))

# №12 function parse_number(value) that tries to convert
# a string to a number and handles 'ValueError' exception
def parse_number(value):
    try:
        number = int(value)
        return number
    except ValueError:
        print(f"Error: {value} is not a valid number.")
        return None

# №18 function convert_to_integer(value) that tries to convert
# a string to an integer and handles both 'ValueError' and 'TypeError' exceptions
def convert_to_integer(value):
    try:
        number = int(value)
        return number
    except ValueError:
        print(f"Error: {value} is not a valid number.")
        return None
    except TypeError:
        print(f"TypeError: {value} is not a valid number.")
        return None

# №24 function get_non_empty_string() that prompts the user for a string
# and raises an exception if the string is empty
def get_non_empty_string():
    user_input = input("Enter non-empty string: ").strip()
    if not user_input:
        raise ValueError("Non-empty string cannot be empty.")
    return user_input

# №29 function write_list_to_file(filename, lst) that writes a list to a file
# and handles errors

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def write_to_file(filename, lst):
    try:
        with open(filename, "w") as file:
            for item in lst:
                file.write(str(item) + "\n")
        print(f"List is written to {filename}")
    except (IOError, FileNotFoundError):
        print(f"Error: {filename} is not a valid file.")

# №35 function find_item_in_list(lst, item) that searches for an item in a list and
# handles exceptions
def find_item_in_list(lst, item):
    try:
        for item in lst:
            if item == item:
                print(f"Found item {item} in {lst}")
    except:
        print(f"Error: {item} is not a valid item.")
        return None

# №39 function get_valid_username() that checks if the username
# meets the specified criteria
def get_valid_username():
    username = input("Enter username: ").strip()
    if not username:
        raise ValueError("Username cannot be empty.")

# №43 function filter_positive_numbers(numbers) that filters a list and
# returns only positive numbers, handling exceptions
def filter_positive_numbers(numbers):
    try:
        for element in numbers:
            if element > 0:
                return element
    except ValueError:
        print(f"Error: {numbers} is not a valid number.")
        return None

# №49 function log_exceptions(func) that logs exception information
# to a file when executing a function
import traceback  # get detailed exception information
import functools  # for wraps

def log_exceptions(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):  # inner function that accepts any arguments and keyword arguments
        try:
            return func(*args, **kwargs)  # call the passed function func
        except Exception as e:  # catch the exception in variable e
            with open("error_log.txt", "a", encoding="utf-8") as log_file:
                log_file.write(f"Exception in function '{func.__name__}': {str(e)}\n")
                log_file.write("Traceback:\n")
                log_file.write(traceback.format_exc())
                log_file.write("\n" + "-"*60 + "\n")
            raise  # re-raise the exception so it’s not suppressed
    return wrapper
