"""
https://leetcode.com/problems/add-binary/description

Constraints:
1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""

import unittest


def addBinary(a: str, b: str) -> str:
    """
    Функция возвращает строку с суммой переданных двоичных чисел
    :param a: str, первое слагаемое
    :param b: str, второе слагаемое
    :return: str,их сумма в двоичном представлении
    """
    return format(int(a, 2) + int(b, 2), "b")


# Общая проверка
assert (addBinary("101", "1010")) == "1111"

# Числа с одинаковым количеством разрядов
assert (addBinary("100", "101")) == "1001"

# Числа с сложением единиц в одинаковых разрядах
assert (addBinary("111", "11111")) == "100110"

# Сложение первого слагаемого с нулем не должно менять слагаемое
assert (addBinary("101", "0")) == "101"

# Сложение второго слагаемого с нулем не должно менять слагаемое
assert (addBinary("0", "100")) == "100"

# Тест проверяет перенос разрядов при сложении числа из единиц с единицей
assert (addBinary("11111", "1")) == "100000"

# Сложение чисел минимальной длины, не равных нулю
assert (addBinary("1", "1")) == "10"

# Сложение чисел минимальной длины
assert (addBinary("0", "0")) == "0"

# Сложение чисел максимальной длины
assert (addBinary("1" * 10_000, "1" * 10_000)) == "1" * 10_000 + "0"


class TestInvalid(unittest.TestCase):
    def test_invalid_number(self):
        with self.assertRaises(ValueError):
            addBinary("102", "1")

    def test_invalid_int(self):
        with self.assertRaises(TypeError):
            addBinary(123, 456)
