def canConstruct(ransomNote: str, magazine: str) -> bool:
    compare_dict: dict = {}

    for letter in ransomNote:
        compare_dict.setdefault(letter, 0)
        compare_dict[letter] += 1

    for letter in magazine:
        if letter not in compare_dict:
            return False
        else:
            compare_dict[letter] -= 1

    for k, v in compare_dict.items():
        if v > 0:
            return False

    return True


print(canConstruct("abcd", "cdbe"))

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

"""Тест проверяет длинные строки."""
assert canConstruct("k" * 10000, "k" * 10000) == True


"""
Остальные тесты
"""

"""Тест для пустой строки"""
assert canConstruct("", "ft") == False

"""Тест с одной буквой в разном регистре. Обработка ошибки нет, поэтому функция верент валидный результат."""
assert canConstruct("n", "N") == False
