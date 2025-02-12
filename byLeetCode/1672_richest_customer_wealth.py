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
