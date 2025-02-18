"""
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i_th customer has in the j_th bank. Return the wealth that the richest customer has.
A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.
https://leetcode.com/problems/richest-customer-wealth/description/
"""


def maximumWealth(accounts: list[list[int]]) -> int:
    """
    Возвращает сумму на всех счетах для самого богатого клиента.
    :param accounts: массив с суммами у клиентов в каждом банке
    :return: int: сумма на всех счетах у бгатейшего клиента
    """
    return max(sum(ith) for ith in accounts)


# Один богатейший клиент, суммы на счетах не равны.
assert maximumWealth([[1, 10, 15], [20, 50, 79], [2, 32, 23]]) == 149
# Один богатейший клиент, суммы на его счетах равны.
assert maximumWealth([[30, 30, 30], [50, 50, 50], [15, 15, 15]]) == 150
# У всех клиентов богатство одинаковое.
assert maximumWealth([[20, 30, 50], [15, 75, 10]]) == 100

# Один богатейший клиент, но у каждого клиента есть счет с одинаковой суммой.
assert maximumWealth([[10, 20, 30], [5, 6, 30], [15, 2, 30]]) == 60

# Один банк и один клиент с минимальной суммой на счете.
assert maximumWealth([[1]]) == 1

# Максимальная сумма одного счета, максимальное количество клиентов и банков, у всех клиентов суммы на счетах и общее богатство равны.
assert maximumWealth([[100] * 50 for item in range(50)]) == 5000
