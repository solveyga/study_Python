"""
https://leetcode.com/problems/length-of-last-word/description/
Constraints:
1 <= s.length <= 10^4
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""

import unittest


def lengthOfLastWord(s: str) -> int:
    return len(s.split()[-1])


# Строка с несколькими словами
assert (lengthOfLastWord("The quick brown fox jumps over the lazy dog")) == 3

# Строка с несколькими пробелами подряд
assert (lengthOfLastWord("   fly me   to   the moon  ")) == 4

# Строка с одним словом из нескольких букв
assert (lengthOfLastWord("incomprehensibilities")) == 21

# Строка с одним словом из одной буквы
assert (lengthOfLastWord("a")) == 1

# Строка с максимальным количеством слов - 10_000. Слова одинаковой длины
assert (lengthOfLastWord("word " * 10_000)) == 4

# Строка с очень длинным последний словом (1_000_000 символов, нет ограничений на длину в условии)
assert (lengthOfLastWord("a" * 1_000_000)) == 1_000_000


# Строка с символами, отличными от английских букв и пробелов (валидный неожиданный результат)
assert (
    lengthOfLastWord(
        "Съещь еще этих мягких французских булок да выпей же чаю 1234567890!"
    )
) == 11


# Негативные тест с неверным типом данных
class TestInvalidInput(unittest.TestCase):
    def test_invalid_input(self):
        with self.assertRaises(AttributeError):
            lengthOfLastWord(123456)
