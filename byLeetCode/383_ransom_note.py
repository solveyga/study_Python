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

"""
    for letter in ransomNote:
        compare_dict.setdefault(letter, 0)
        compare_dict[letter] += 1

    for letter in magazine:
        if letter not in compare_dict:
            continue
        else:
            compare_dict[letter] -= 1

    for k, v in compare_dict.items():
        if v > 0:
            return False

    return True
    """


"""
Позитивные тесты
"""

"""Тест проверяет случай, когда строки совпадают."""
assert canConstruct("abcd", "cadb") == True

"""Тест проверяет случай, когда ransomNote невозможно составить из букв magazine."""
assert canConstruct("abcd", "cdbe") == False

"""Тест проверяет случай, обе строки состоят из одной совпадающей буквы."""
assert canConstruct("n", "n") == True

"""Тест проверяет случай, когда во второй строке недостаточно букв."""
assert canConstruct("abcdr", "cadb") == False

"""Тест проверяет случай, когда во второй строке больше букв, в том числе отличный от первой строки."""
assert canConstruct("aa", "aab") == True

"""Тест проверяет длинные строки."""
assert canConstruct("k" * 10000, "k" * 10000) == True


"""
Остальные тесты
"""

"""Тест для пустой строки"""
assert canConstruct("", "ft") == True

"""Тест с одной буквой в разном регистре. Обработка ошибки нет, поэтому функция верент валидный результат."""
assert canConstruct("n", "N") == False
