import re


# ---------------------------------------------------------------
# Завдання 1. Власний виняток
# ---------------------------------------------------------------
class EmptyTextError(Exception):
    """Виняток для порожнього тексту."""
    pass


def analyze_text(text):
    """Повертає кількість символів у тексті."""
    if not isinstance(text, str):
        raise TypeError("Аргумент text має бути рядком.")

    if not text.strip():
        raise EmptyTextError("Текст порожній.")

    return len(text)


def task1():
    print("\n=== Завдання 1: analyze_text ===")
    # перевіряємо різні випадки: правильний текст, порожній рядок, не рядок
    test_values = ["Привіт, світе!", "", "   ", 123]

    for value in test_values:
        try:
            result = analyze_text(value)
        except EmptyTextError as error:
            print(f"{value!r}: помилка — {error}")
        except TypeError as error:
            print(f"{value!r}: помилка — {error}")
        else:
            print(f"{value!r}: кількість символів = {result}")


# ---------------------------------------------------------------
# Завдання 2. Регулярний вираз від користувача
# ---------------------------------------------------------------
def task2():
    print("\n=== Завдання 2: регулярні вирази ===")
    pattern = input("Введіть регулярний вираз: ")

    try:
        regex = re.compile(pattern)
    except re.error:
        print("Помилка: регулярний вираз має некоректний синтаксис.")
        return

    text = input("Введіть текст: ")
    matches = regex.findall(text)

    if matches:
        print(f"Знайдено збігів: {len(matches)}")
        print("Збіги:", matches)
    else:
        print("Збігів не знайдено.")


# ---------------------------------------------------------------
# Завдання 3. Читання файлу text55.txt
# ---------------------------------------------------------------
def task3(filename="text55.txt"):
    print("\n=== Завдання 3: читання файлу ===")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Помилка: файл '{filename}' не знайдено.")
    except PermissionError:
        print(f"Помилка: немає доступу до файлу '{filename}'.")
    except UnicodeDecodeError:
        print("Помилка: неможливо прочитати файл у вказаному кодуванні.")
    else:
        print("Вміст файлу:")
        print(text)
        print("-" * 30)

        chars = len(text)
        words = len(text.split())
        lines = len(text.splitlines())

        print(f"Кількість символів: {chars}")
        print(f"Кількість слів: {words}")
        print(f"Кількість рядків: {lines}")


# ---------------------------------------------------------------
# Запуск
# ---------------------------------------------------------------
if __name__ == "__main__":
    task1()
    task2()
    task3()
