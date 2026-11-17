import random
import string

# Ім'я латиницею. Довжина пароля = кількість літер в імені.
# Якщо ваше ім'я пишеться інакше (наприклад, Kateryna), змініть тут.
NAME = "Katia"


def generate_password(length):
    """Генерує пароль заданої довжини.

    Пароль обов'язково містить:
    - символ у шістнадцятковому форматі (string.hexdigits: 0-9, a-f, A-F);
    - спеціальний символ (string.punctuation);
    - літеру верхнього регістру (string.ascii_uppercase).
    """
    if length < 3:
        raise ValueError("Довжина пароля має бути не меншою за 3.")

    # по одному обов'язковому символу з кожної групи
    password_chars = [
        random.choice(string.hexdigits),
        random.choice(string.punctuation),
        random.choice(string.ascii_uppercase),
    ]

    # решта символів - з усіх трьох груп разом
    all_chars = string.hexdigits + string.punctuation + string.ascii_uppercase
    for _ in range(length - 3):
        password_chars.append(random.choice(all_chars))

    # перемішуємо, щоб обов'язкові символи не стояли завжди на початку
    random.shuffle(password_chars)
    return "".join(password_chars)


if __name__ == "__main__":
    length = len(NAME)
    print(f"Ім'я: {NAME}, довжина пароля: {length}")

    try:
        password = generate_password(length)
    except ValueError as error:
        print(f"Помилка: {error}")
    else:
        print("Згенерований пароль:", password)