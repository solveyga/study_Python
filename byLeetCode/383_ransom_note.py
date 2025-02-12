"""
https://leetcode.com/problems/ransom-note/solutions/5821388/video-counting-each-character-2-solutions
"""

from collections import Counter


def canConstruct(ransomNote: str, magazine: str) -> bool:
    ransom_count = Counter(ransomNote)
    magazine_count = Counter(magazine)

    for letter, count in ransom_count.items():
        if magazine_count[letter] < count:
            return False
    return True


# Позитивные тесты

# Тест проверяет случай, когда строки совпадают.
assert canConstruct("abcd", "cadb")

# Тест проверяет случай, когда ransomNote невозможно составить из букв magazine.
assert not canConstruct("abcd", "cdbe")

# Тест проверяет случай, обе строки состоят из одной совпадающей буквы.
assert canConstruct("n", "n")

# Тест проверяет случай, когда во второй строке недостаточно букв.
assert not canConstruct("abcdr", "cadb")

# Тест проверяет случай, когда во второй строке больше букв, в том числе отличный от первой строки.
assert canConstruct("aa", "aab")

# Тест проверяет длинные строки.
assert canConstruct("k" * 10000, "k" * 10000)


# Остальные тесты


# Тест для пустой строки
assert canConstruct("", "ft")

# Тест с одной буквой в разном регистре. Обработка ошибки нет, поэтому функция верент валидный результат.
assert not canConstruct("n", "N")
