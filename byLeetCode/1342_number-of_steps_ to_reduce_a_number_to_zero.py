"""
Given an integer num, return the number of steps to reduce it to zero.
In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/
"""

import unittest


def numberOfSteps(num: int) -> int:
    """
    Вычисляет число шагов для уменьшения числа до нуля. Четное число делится на два, от нечетного отнимается один.

    Условие while num > 0 защищает от бесконечного цикла.

    :param num: натуральное число
    :return: количество шагов до нуля
    """
    steps: int = 0
    while num > 0:
        steps += 1
        num = num // 2 if num % 2 == 0 else num - 1
    return steps


# Позитивные тесты

# Обычное число.
assert numberOfSteps(14) == 6

# Число с последовательными делениями подряд без чередования с вычитанием.
assert numberOfSteps(16) == 5

# Минимальный шаг.
assert numberOfSteps(1) == 1

# Минимальное число с обеими операциями.
assert numberOfSteps(2) == 2

# Большое число и альтернативная запись для целого числа.
assert numberOfSteps(int(10_000_000)) == 31


# Критичные негативные тесты

# Дробное число не запустит бесконечный цикл.
assert numberOfSteps(2.5) == 3

# Отрицательное число не запустит бесконечный цикл.
assert numberOfSteps(-5) == 0


# Остальные негативные тесты

# Ноль - целое число за пределами гарантированного ввода.
assert numberOfSteps(0) == 0

# Нечисловой тип данных.
class TestInvalidInput(unittest.TestCase):

    def test_not_numeric(self):
        with self.assertRaises(TypeError):
            numberOfSteps("5")

    def test_none(self):
        with self.assertRaises(TypeError):
            numberOfSteps(None)

# Вещественное число в альтернативной нотации.
assert numberOfSteps(10e2) == 15
