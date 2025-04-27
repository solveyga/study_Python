"""
Задача: https://leetcode.com/   problems/search-insert-position/description/
Ограничения:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums contains distinct values sorted in ascending order.
-10^4 <= target <= 10^4
"""


def searchInsert(nums: list[int], target: int) -> int:
    """
    Функция принимает отсортированный список целых чисел и искомое число и возвращаает позицию искомого числа,
    если оно есть  в списке или если бы оно было в списке.
    :param nums: отсортированный список целых чисел
    :param target: искомое число
    :return: позиция искомого числа
    """
    left = 0
    right = len(nums) - 1
    while left != right:
        mid = (right - left) // 2 + left
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    if nums[right] >= target:
        return right
    else:
        return right + 1


# target есть внутри массива
assert (searchInsert([1, 3, 5, 6], 5)) == 2

# target - наибольшее число массива
assert (searchInsert([1, 3, 5, 6], 6)) == 3

# target - наименьшее число массива
assert (searchInsert([1, 3, 5, 6], 1)) == 0

# target равен нулю и отсутствует, его место слева перед массивом
assert (searchInsert([1, 3, 5, 6], 0)) == 0

# target - отрицательное число, отсутствует в массиве, его место внутри массива
assert (searchInsert([-5, -3, 1, 3, 5, 6], -2)) == 2

# target отсутсвует и равен максимально допустимому значению, его место справа за массивом
assert (searchInsert([1, 3, 5, 6], 10_000)) == 4

# массив минимальной длины, содержащий target
assert (searchInsert([3], 3)) == 0

# массив максимальной длины
assert (searchInsert(nums=list(range(-10_000, 0)), target=-10_000)) == 0
