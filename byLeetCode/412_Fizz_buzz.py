"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
"""

import unittest

def fizzBuzz(n: int) -> list[str]:
    """
    Функция принимает целое число и проверяет, какие числа от 1 до n делятся на 3 и на 5.
    В результирующий массив попадает FizzBuzz, если оба числа - делители; Fizz, если делитель 3; Buzz, если делитель 5;
    Само число, если оно не делится на 3 или 5.
    :param n:
    :return: list[str]
    """
    return [
        "FizzBuzz" if i % 3 == 0 and i % 5 == 0 else
        "Fizz" if i % 3 == 0 else
        "Buzz" if i % 5 == 0 else
        str(i)
        for i in range(1, n+1)
    ]


"""
Позитивные тесты
"""

"""Тест с первым встречающимся делимым 15."""
assert fizzBuzz(15) == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']

"""Тест нескольких делимых 15, FizzBuzz не только в первом и последнем блоке."""
assert fizzBuzz(45) == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz',
                        '16', '17', 'Fizz', '19', 'Buzz', 'Fizz', '22', '23', 'Fizz', 'Buzz', '26', 'Fizz', '28', '29', 'FizzBuzz',
                        '31', '32', 'Fizz', '34', 'Buzz', 'Fizz', '37', '38', 'Fizz', 'Buzz', '41', 'Fizz', '43', '44', 'FizzBuzz']

"""Тест с минимальным n."""
assert fizzBuzz(1) == ["1"]

"""
Негативные тесты
"""

"""Тест нулевого n."""
assert fizzBuzz(0) == []

"""Тест дробного n."""
class TestFloatN(unittest.TestCase):
    def test_float_n(self):
        with self.assertRaises(TypeError):
            fizzBuzz(2.5)

"""Тест отрицательного n."""
assert fizzBuzz(-5) == []

"""Тест нечислового n."""
class TestStringN(unittest.TestCase):
    def test_string_n(self):
        with self.assertRaises(TypeError):
            fizzBuzz("2.5")


"""
Остальные негативные тесты
"""

"""Тест для None."""
class TestNoneN(unittest.TestCase):
    def test_none_n(self):
        with self.assertRaises(TypeError):
            fizzBuzz(None)

"""Тест для True, которое интерпретируется как 1."""
assert fizzBuzz(True) == ["1"]

"""Тест для False, которое интерпретируется как 0."""
assert fizzBuzz(False) == []

