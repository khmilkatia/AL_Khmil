# my_module.py - мій власний модуль з функціями для роботи з текстом

VOWELS = "аеєиіїоуюяaeiouy"


def count_vowels(text):
    """Повертає кількість голосних літер у тексті (українських і англійських)."""
    return sum(1 for char in text.lower() if char in VOWELS)


def reverse_text(text):
    """Повертає текст у зворотному порядку."""
    return text[::-1]


def is_palindrome(text):
    """Перевіряє, чи є текст паліндромом (без урахування пробілів і регістру)."""
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


def count_words(text):
    """Повертає кількість слів у тексті."""
    return len(text.split())