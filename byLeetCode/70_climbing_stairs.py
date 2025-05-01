def climbStairs(n: int) -> int:
    prev = 0
    curr = 1
    for i in range(0, n):
        curr += prev
        prev = curr - prev
    return curr


# Значение для первой ступени
assert (climbStairs(1)) == 1

# Не первая ступень, количество способов достичь её равно номеру ступени
assert (climbStairs(2)) == 2

# Первая ступень, у которой количество способов достичь её больше номера ступени
assert (climbStairs(4)) == 5

# Не первая ступень, где количество способов достичь её больше номера ступени
assert (climbStairs(6)) == 13

# Ступень с максимальным номером из условия
assert (climbStairs(45)) == 1836311903
