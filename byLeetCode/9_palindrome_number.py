"""
https://leetcode.com/problems/palindrome-number/description/
-2^31 <= x <= 2^31 - 1
"""

import unittest


def isPalindrome(x: int) -> bool:
    """
    Проверяет, является ли число палиндромом.
    :param x: - проверяемое число
    :return: bool: true, если число палиндом
    """
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reverse_half = 0

    while x > reverse_half:
        reverse_half = reverse_half * 10 + x % 10
        x //= 10

    return x == reverse_half or x == reverse_half // 10


# Обычный палиндом из нечетного числа цифр.
assert isPalindrome(12321)


# Обычный палиндом из четного числа цифр.
assert isPalindrome(123321)

# Минимальный ненулевой палиндром.
assert isPalindrome(5)

# Нулевой палиндром.
assert isPalindrome(0)

# Палиндром из одинаковых цифр.
assert isPalindrome(111111)

# Число, оканчивающееся на ноль, не будет палиндромом.
assert not isPalindrome(100)

# Отрицательное число не будет палиндромом, даже если его модуль - палиндром.
assert not isPalindrome(-123321)

# Максимальное число из условия не будет палиндромом.
assert not isPalindrome(2147483647)

# Минимальное число из условия не будет палиндромом.
assert not isPalindrome(-2147483648)


class TestInvalidInput(unittest.TestCase):
    def test_string(self):
        with self.assertRaises(TypeError):
            isPalindrome("12321")
