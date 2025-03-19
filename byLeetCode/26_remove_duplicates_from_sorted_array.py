"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

1 <= nums.length <= 3 * 10^4
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
"""


def removeDuplicates(nums: list[int]) -> int:
    """
    Функция принимает массив целых чисел, отсортированных в неубывающем порядке, и возвращает количество уникальных значений.
    :param nums: массив чисел
    :return: int: количество уникальных значений
    """
    k = 0
    for i in range(len(nums)):
        if nums[i] != nums[k]:
            nums[k + 1] = nums[i]
            k += 1
    return k + 1


# Массив с положительными числами и чередующимися дублями
assert (removeDuplicates([1, 1, 2, 2, 5, 5])) == 3

# Массив чисел с нулем и дублями
assert (removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])) == 5

# Массив с отрицательными числами и только уникальными значениями
assert removeDuplicates([-2, -1, 0, 1, 2]) == 5

# Массив минимальной длины
assert removeDuplicates([-100]) == 1

# Массив максимальной длины из одинаковых значений
assert removeDuplicates([100] * 30000) == 1

# Массив с уникальными значениями в начале, в середине и в конце массива
assert removeDuplicates([-1, 2, 2, 3, 4, 4, 5]) == 5
