# main_modules.py
# Програма використовує одразу кілька модулів:
#   1) math     - стандартний (математика)
#   2) random   - стандартний (випадкові числа)
#   3) datetime - стандартний (дата й час)
#   + my_module - власний модуль (має лежати в тій самій папці)

import math
import random
from datetime import datetime

import my_module


def main():
    # --- datetime ---
    now = datetime.now()
    print("Поточна дата й час:", now.strftime("%d.%m.%Y %H:%M:%S"))

    # --- random ---
    number = random.randint(1, 100)
    print("Випадкове число від 1 до 100:", number)

    # --- math ---
    print(f"Квадратний корінь з {number}: {math.sqrt(number):.2f}")
    print("Факторіал числа 5:", math.factorial(5))

    # --- власний модуль ---
    text = input("Введіть текст: ")
    print("Кількість слів:", my_module.count_words(text))
    print("Кількість голосних:", my_module.count_vowels(text))
    print("Текст навпаки:", my_module.reverse_text(text))

    if my_module.is_palindrome(text):
        print("Це паліндром.")
    else:
        print("Це не паліндром.")


if __name__ == "__main__":
    main()