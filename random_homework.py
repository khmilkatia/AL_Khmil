"""Робота з модулем random."""

import random

# Заміни на справжній список своєї групи
students = ["Анна", "Богдан", "Поліна", "Максим", "Дарина", "Наталя", "Ілля", "Катерина"]


def task0():
    print("=== Завдання 0: random(), randint(), choice() ===")
    print("random.random():", random.random())            # дробове число від 0 до 1
    print("random.randint(1, 10):", random.randint(1, 10))  # ціле число від 1 до 10 включно
    print("random.choice(['a', 'b', 'c']):", random.choice(["a", "b", "c"]))  # випадковий елемент списку


def task1():
    print("\n=== Завдання 1: випадковий студент (5 разів) ===")
    for i in range(1, 6):
        print(f"Спроба {i}:", random.choice(students))


def task2():
    print("\n=== Завдання 2: кілька студентів без повторів ===")
    chosen = random.sample(students, 3)
    print("Обрані студенти:", chosen)


def flip_coin():
    return random.choice(["орел", "решка"])


def count_flips(times):
    """Підкидає монету times разів, повертає словник з підрахунком."""
    result = {"орел": 0, "решка": 0}
    for _ in range(times):
        result[flip_coin()] += 1
    return result


def task3():
    print("\n=== Завдання 3: гра з монеткою ===")
    print("Одне підкидання:", flip_coin())
    for times in (100, 1000):
        result = count_flips(times)
        print(f"{times} підкидань -> орел: {result['орел']}, решка: {result['решка']}")


def task4():
    print("\n=== Завдання 4*: камінь-ножиці-папір ===")
    options = ["камінь", "ножиці", "папір"]
    beats = {"камінь": "ножиці", "ножиці": "папір", "папір": "камінь"}
    score = {"ти": 0, "комп'ютер": 0}

    for round_number in range(1, 4):
        player = input(f"Раунд {round_number}/3. Камінь, ножиці чи папір? ").strip().lower()
        if player not in options:
            print("Потрібно ввести: камінь, ножиці або папір. Раунд пропущено.")
            continue
        computer = random.choice(options)
        print("Комп'ютер обрав:", computer)
        if player == computer:
            print("Нічия!")
        elif beats[player] == computer:
            print("Ти виграла раунд!")
            score["ти"] += 1
        else:
            print("Комп'ютер виграв раунд.")
            score["комп'ютер"] += 1

    player_score = score["ти"]
    computer_score = score["комп'ютер"]
    print(f"Рахунок: ти {player_score} : {computer_score} комп'ютер")


if __name__ == "__main__":
    task0()
    task1()
    task2()
    task3()
    task4()