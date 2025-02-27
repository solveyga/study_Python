"""
https://leetcode.com/problems/valid-parentheses/description/

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'
"""

import unittest


def isValid(s: str) -> bool:
    """
    Принимает строку и возвращает True, если скобки имеют пары в верном порядке.
    :param s:
    :return: bool
    """
    brackets_dict: dict = {")": "(", "}": "{", "]": "["}
    open_brackets_list: list[str] = []
    for item in s:
        if item in brackets_dict:
            if not open_brackets_list or open_brackets_list[-1] != brackets_dict[item]:
                return False
            open_brackets_list.pop()
        else:
            open_brackets_list.append(item)
    return not open_brackets_list


# Строка из одной пары скобок
assert isValid("()")

# Строка из нескольких пар скобок
assert isValid("()[]{}")

# Строка из некольких одинаковых пар вложенных скобок
assert isValid("((()))")

# Строка из нескольких пар скобок, в том числе вложенных
assert isValid("([{}()][]){}")

# Строка максимальной длины
assert isValid("[()]" * 26)

# Строка из пары скобок разного типа
assert not isValid("(]")

# Строка из одной открывающей скобки не будет валидной. Минимальная длина строки
assert not isValid("{")

# Строка из одной закрывающей скобки не будет валидной
assert not isValid("]")

# Строка из нескольких пар с лишней открывающей скобкой
assert not isValid("([{}()][])({}")

# Строка из нескольких пар с лишней закрывающей скобкой
assert not isValid("([{}()][]){)}")

# Строка с нарушенным порядком скобок
assert not isValid("([{}()][])({)}")

# Пустая строка
assert isValid("")

# Строка с символами, отличными от скобок
assert not isValid("()not[]only{}brackets")

# Невалидный тип данных


class TestInvalifInput(unittest.TestCase):
    def test_integer(self):
        with self.assertRaises(TypeError):
            isValid(123)
