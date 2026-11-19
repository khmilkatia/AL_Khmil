"""Статистика за текстом із Браунського корпусу української мови.

Текст береться з https://github.com/brown-uk/corpus (папка data/good)
і зберігається поруч зі скриптом у файлі text.txt.

Запуск:
    python3 corpus_stats.py
"""

import re

FILENAME = "corpus_text.txt"

# Слово: літери, всередині можуть бути апостроф або дефіс (м'яч, будь-який).
WORD_RE = re.compile(r"[^\W\d_]+(?:['’ʼ-][^\W\d_]+)*")


def read_text(filename):
    """Читає текст із файлу (UTF-8) і повертає рядок."""
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def get_words(text):
    """Повертає список слів у нижньому регістрі."""
    return WORD_RE.findall(text.lower())


def count_words(text):
    """Кількість слів у тексті."""
    return len(get_words(text))


def word_counts(text):
    """Словник {слово: скільки разів зустрілось}."""
    counts = {}
    for word in get_words(text):
        counts[word] = counts.get(word, 0) + 1
    return counts


def count_unique_words(text):
    """Кількість унікальних слів."""
    return len(word_counts(text))


def word_frequency_percent(text):
    """Частотний словник у відсотках: {слово: частка від усіх слів, %}.

    Слова впорядковані від найчастіших до найрідших.
    """
    counts = word_counts(text)
    total = sum(counts.values())
    if total == 0:
        return {}
    ordered = sorted(counts.items(), key=lambda pair: (-pair[1], pair[0]))
    return {word: round(number * 100 / total, 2) for word, number in ordered}


def shortest_words(text):
    """Список найкоротших слів (унікальних), їх може бути кілька."""
    words = word_counts(text)
    if not words:
        return []
    min_len = min(len(word) for word in words)
    return sorted(word for word in words if len(word) == min_len)


def longest_words(text):
    """Список найдовших слів (унікальних), їх може бути кілька."""
    words = word_counts(text)
    if not words:
        return []
    max_len = max(len(word) for word in words)
    return sorted(word for word in words if len(word) == max_len)


def letter_counts(text):
    """Словник {літера: скільки разів зустрілась}."""
    counts = {}
    for char in text.lower():
        if char.isalpha():
            counts[char] = counts.get(char, 0) + 1
    return counts


def used_letters(text):
    """Відсортований список літер, що використовувались у тексті."""
    return sorted(letter_counts(text))


def most_frequent_letters(text):
    """Літера (або літери, якщо їх кілька), що зустрічалась найчастіше."""
    counts = letter_counts(text)
    if not counts:
        return []
    top = max(counts.values())
    return sorted(letter for letter, number in counts.items() if number == top)


def main():
    try:
        text = read_text(FILENAME)
    except FileNotFoundError:
        print(f"Файл '{FILENAME}' не знайдено. Збережіть текст поруч зі скриптом.")
        return
    except UnicodeDecodeError:
        print("Файл має бути в кодуванні UTF-8.")
        return

    if not get_words(text):
        print("У тексті немає слів.")
        return

    print("Кількість слів:", count_words(text))
    print("Кількість унікальних слів:", count_unique_words(text))

    print("\nНайчастіші слова (%):")
    for word, percent in list(word_frequency_percent(text).items())[:10]:
        print(f"  {word:<15} {percent}%")

    print("\nНайкоротші слова:", shortest_words(text))
    print("Найдовші слова:", longest_words(text))
    print("\nЛітери, що використовувались:", " ".join(used_letters(text)))
    print("Літера, що зустрічалась найчастіше:", most_frequent_letters(text))


if __name__ == "__main__":
    main()