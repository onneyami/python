#№4 функция divide(a,b), возвращающая результат деления a на b
def divide(a, b):
    return a / b

#№8 функция get_positive_integer(), которая запрашивает у пользователя ввод положительного числа
def get_positive_integer():
    input("Enter positive integer: ")
    if int(input("Enter positive integer: ")) < 0:
        return int(input("Enter positive integer: "))

#№12 функция parse_number(value), которая пытается преобразовать
#строку в число и обрабатывает исключение 'ValueError'
def parse_number(value):
    try:
        number = int(value)
        return number
    except ValueError:
        print(f"Error: {value} is not a valid number.")
        return None

#№18 функция convert_to_int(value), которая пытается преобразовать
#строку в целое число и обрабатывает оба типа исключений: 'ValueError' и 'TypeError'
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

#№24 функция get_non_empty_string(), которая запрашивает строку у пользователя
# и выбрасывает исключение, если строка пустая
def get_non_empty_string():
    user_input = input("Enter non-empty string: ").strip()
    if not user_input:
        raise ValueError("Non-empty string cannot be empty.")
    return user_input

#№29 функция write_list_to_file(filename, lst), которая записывает список в файл
# и обрабатывает ошибки

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def write_to_file(filename, lst):
    try:
        with open(filename, "w") as file:
            for item in lst:
                file.write(str(item) + "\n")
        print(f"List is written to {filename}")
    except (IOError, FileNotFoundError):
        print(f"Error: {filename} is not a valid file.")

#№35 функция find_item_in_list(lst, item), которая ищет элемент в списке и
#обрабатывает исключения
def find_item_in_list(lst, item):
    try:
        for item in lst:
            if item == item:
                print(f"Found item {item} in {lst}")
    except:
        print(f"Error: {item} is not a valid item.")
        return None

#№39 функция get_valid_username(), которая проверяет, что имя пользователя
# соответствует заданным критериям
def get_valid_username():
    username = input("Enter username: ").strip()
    if not username:
        raise ValueError("Username cannot be empty.")

#№43 функция filter_positive_numbers(numbers), которая филтрует список и
#возвращает только положительные числа, обрабатывая исключения
def filter_positive_numbers(numbers):
    try:
        for element in numbers:
            if element > 0:
                return element
    except ValueError:
        print(f"Error: {numbers} is not a valid number.")
        return None

#№49 функция log_exceptions(func), которая записывает информацию об исключениях
#в файл при выполнении функции
import traceback #получение подробной информации об исключении
import functools #для wraps

def log_exceptions(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs): #внутренняя функция, которая принимает любые аргументы и ключевые аргументы
        try:
            return func(*args, **kwargs) #вызываем переданную функцию func
        except Exception as e: #исключение перехватывается в переменную e
            with open("error_log.txt", "a", encoding="utf-8") as log_file:
                log_file.write(f"Exception in function '{func.__name__}': {str(e)}\n")
                log_file.write("Traceback:\n")
                log_file.write(traceback.format_exc())
                log_file.write("\n" + "-"*60 + "\n")
            raise  #повторно выбрасываем исключение, чтобы не скрыть его
    return wrapper
