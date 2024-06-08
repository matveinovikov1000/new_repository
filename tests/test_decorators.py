from src.decorators import log


def test_log():
    @log(filename=None)
    def my_function(x, y):
        """Функция для сложения двух чисел"""
        return x + y

    result = my_function(1, 2)
    assert result is None
