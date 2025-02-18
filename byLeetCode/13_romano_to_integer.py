"""
https://leetcode.com/problems/roman-to-integer/description/
1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999]
"""

import unittest


def romanToInt(s: str) -> int:
    """
    Принимает строку с римским числом и возвращает соответствующее ему арабской число.
    :param s: римское число
    :return: int_num: арабское число
    """
    roman_int_dict: dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    int_num = roman_int_dict[s[-1]]

    for i in range(len(s) - 2, -1, -1):
        if roman_int_dict[s[i]] < roman_int_dict[s[i + 1]]:
            int_num -= roman_int_dict[s[i]]
        else:
            int_num += roman_int_dict[s[i]]
    return int_num


# Обычное число
assert romanToInt("LVIII") == 58

# Число с несколькими единицами подряд
assert romanToInt("VII") == 7

# Число с одинаковыми цифрами, которые в зависимости от позиции вычитаются или складываются
assert romanToInt("MCDXLIX") == 1449

# Минимальное число из одного символа
assert romanToInt("I") == 1

# Минимальное число из двух символов, которое записывается одной арабской цифрой
assert romanToInt("IV") == 4

# Минимальное число из одного символа, которое записывается двумя арабскими цифрами
assert romanToInt("X") == 10

# Максимальное число из условия
assert romanToInt("MMMCMXCIX") == 3999

# Строка с корректными символами, но не соответствующая правилам записи, может вернуть необжиданный результат
assert romanToInt("XXXXVC") == 135


class InvalidInput(unittest.TestCase):

    def test_nondict_string(self):
        """
        тест проверяет ошибку при педеаче строки, в которой есть символы не из словаря
        :return: raises KeyError
        """
        with self.assertRaises(KeyError):
            romanToInt("random string")

    def test_integer(self):
        """
        тест проверяет ошибку при передаче данных, отличных от строки
        :return: raises TypeError
        """
        with self.assertRaises(TypeError):
            romanToInt(1985)

    def test_empty_string(self):
        """
        тест проверяет ошибку при передаче пустой строки
        :return: raises IndexError
        """
        with self.assertRaises(IndexError):
            romanToInt("")
