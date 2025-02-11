"""
Задача: https://leetcode.com/problems/two-sum/description/
Ограничения:
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
"""
import unittest

def twoSum(nums: list[int], target: int) -> list[int]:
    """
    Функция принимает массив целых чисел и целое число. Возвращает индексы элементов массива, сумма которых равна этому числу.
    :param nums: массив со слагаемыми
    :param target: сумма
    :return: list[int]
    """

    term_dict: dict[int, int] = {}

    for index, num in enumerate(nums):
        term = target - num
        if term in term_dict:
            return [term_dict[term], index]
        term_dict[num] = index
    return []



#print(twoSum([3,-3],0))

"""
Позитивные тесты
"""

"""target > 0 состоит из положительных слагаемых, расположенных подряд."""
assert twoSum([2, 7, 3, 15], 9) == [0, 1]

"""target > 0 состоит из отрицательного и положительного слагаемых, которые расположены не подряд."""
assert twoSum([-19, 20, 5, -36, -10], 10) == [1, 4]

"""target > 0 состоит из положительного и нулевого слагаемых."""
assert twoSum([5, 0, 42, 100, 36], 100) == [1, 3]

"""target < 0 состоит из отрицательных слагаемых."""
assert twoSum([-10, -36, -1, -123, -123, -6, -50], -42) == [1, 5]

"""target < 0 состоит из отрицательного и нулевого слагаемых."""
assert twoSum([-2, -5, -42, 0, -42], -5) == [1, 3]

"""target = 0 состоит из двух нулей, которые образуют дубли в массиве num."""
assert twoSum([0, 0], 0) == [0, 1]

"""target = 0 состоит из противоположных слагаемых."""
assert twoSum([-4, 5, 4], 0) == [0, 2]

"""
Остальные негативные тесты
"""

"""Нет подходящей пары для target > 0."""
assert twoSum([-1, -2, -10, -42], 42) == []

"""Нет подходящей пары для target < 0."""
assert twoSum([1, 2, 10, 42], -42) == []

"""Тест проверяет неверный тип входных данных."""
class TestInvalidData(unittest.TestCase):
    def test_invalid_nums(self):
        with self.assertRaises(TypeError):
            twoSum('1,2', 3)

    def test_invalid_target(self):
        with self.assertRaises(TypeError):
            twoSum([1, 2], [3])


