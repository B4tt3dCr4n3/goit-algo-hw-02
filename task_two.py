"""Завдання 2. Необхідно розробити функцію, яка приймає рядок як вхідний 
параметр, додає всі його символи до двосторонньої черги (deque з модуля 
collections в Python), а потім порівнює символи з обох кінців черги, щоб 
визначити, чи є рядок паліндромом. Програма повинна правильно враховувати 
як рядки з парною, так і з непарною кількістю символів, а також бути 
нечутливою до регістру та пробілів."""

import re
from collections import deque

def is_palindrome(s):
    """Функція для перевірки, чи є рядок паліндромом"""
    # Видалення всіх символів, крім букв та цифр, і переведення у нижній регістр
    formatted_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    # Створення двосторонньої черги з символів рядка
    char_deque = deque(formatted_s)
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

# Приклад використання
print(is_palindrome("A man, a plan, a canal, Panama!"))  # Повинно вивести True
print(is_palindrome("Not a palindrome"))  # Повинно вивести False
