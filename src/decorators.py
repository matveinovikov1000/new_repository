def log(filename):
    """Декоратор для логирования функции"""

    def my_decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename is None:
                    if type(result) is int or type(result) is float:
                        print("my_function ok")
            except TypeError:
                print(f"my_function error: сложению подлежат только числа. Inputs: {args}, {kwargs}")
            try:
                result = func(*args, **kwargs)
                if filename is not None:
                    if type(result) is int or type(result) is float:
                        with open(filename, "a", encoding="utf8") as file:
                            file.write("my_function ok\n")
            except TypeError:
                with open(filename, "a", encoding="utf8") as file:
                    file.write(f"my_function error: сложению подлежат только числа. Inputs: {args}, {kwargs}\n")

        return wrapper

    return my_decorator
