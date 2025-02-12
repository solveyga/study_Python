"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
https://leetcode.com/problems/running-sum-of-1d-array/description/
"""

import unittest


def running_sum(nums: list[int]) -> str:
    for i in range(1, len(nums)):
        nums[i] = nums[i - 1] + nums[i]
    return f"Массив с текущей суммой: {nums}"


# Позитивные тесты

# Тест проверяет массив минимальной длины.
assert running_sum([1]) == "Массив с текущей суммой: [1]"

# Тест проверяет массив отрицательных чисел.
assert running_sum([-5, -10, -2, -4]) == "Массив с текущей суммой: [-5, -15, -17, -21]"

# Тест проверяет обычный массив с отрицательными и положительными числами и нулем.
assert (
    running_sum([-5, -1_000, 0, 42])
    == "Массив с текущей суммой: [-5, -1005, -1005, -963]"
)

# Тест проверяет массив одинаковых чисел.
assert running_sum([1, 1, 1, 1, 1]) == "Массив с текущей суммой: [1, 2, 3, 4, 5]"

# Тест проверяет массив дробных чисел с повторами значений и натуральное число.
assert (
    running_sum([-42.5, 42.5, -42.5, 42])
    == "Массив с текущей суммой: [-42.5, 0.0, -42.5, -0.5]"
)

# Тест проверяет длинный массив.
assert (
    running_sum([1] * 1000) == f"Массив с текущей суммой: {[i for i in range(1, 1001)]}"
)

# Негативные тесты. Функция не обрабатывает исключения.

# Тест проверяет пустой массив.
assert running_sum([]) == "Массив с текущей суммой: []"

# Тест проверяет, что строковые значения просто конкатенируются, если функция не проверяет типы.
assert running_sum(["0", "3"]) == "Массив с текущей суммой: ['0', '03']"


# Тест проверяет ошибку, когда передан не массив.
class TestString(unittest.TestCase):
    def test_string(self):
        with self.assertRaises(TypeError):
            running_sum("string")


# Тест проверяет ошибку при передаче словаря.
class TestDict(unittest.TestCase):
    def test_dict(self):
        with self.assertRaises(TypeError):
            running_sum({"a": 1, "b": 2})


# Тест проверяет ошибку при передаче кортежа.
class TestTuple(unittest.TestCase):
    def test_tuple(self):
        with self.assertRaises(TypeError):
            running_sum([5, None])
        running_sum((1, 2, 3))


# Тест проверяет None среди подходящих типов данных.
class TestNone(unittest.TestCase):
    def test_string(self):
        with self.assertRaises(TypeError):
            running_sum([5, None])
