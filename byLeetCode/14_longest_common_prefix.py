"""
https://leetcode.com/problems/longest-common-prefix/description/

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""

import unittest


def longestCommonPrefix(strs: list[str]) -> str:
    strs.sort()
    first_word: str = strs[0]
    last_word: str = strs[-1]
    for i in range(min(len(first_word), len(last_word))):
        if first_word[i] != last_word[i]:
            return first_word[:i]
    return first_word


# Обычный массив строк с общим префиксом
assert longestCommonPrefix(["flower", "flow", "flight"]) == "fl"

# Обычный массии строк без общего префикса
assert longestCommonPrefix(["dog", "racecar", "car"]) == ""

# Массив с единственной строкой максимальной длины (200 символов)
assert longestCommonPrefix(["i" * 200]) == "i" * 200

# Массив с пустой строкой
assert longestCommonPrefix(["wheal", ""]) == ""

# Массив с несколькими пустыми строками
assert longestCommonPrefix(["", "", ""]) == ""

# Массив со строками из одной буквы и максимальным числом строк
assert longestCommonPrefix(["a"] * 200) == "a"


# Ошибка при передаче неверного типа данных
class TestInvalidInput(unittest.TestCase):
    def test_string(self):
        with self.assertRaises(AttributeError):
            longestCommonPrefix("asd")
