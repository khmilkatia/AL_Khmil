"""Аналізатор тексту: підрахунок слів, унікальних слів і частотності.

Запуск:
    python text_analyzer.py sample_text.txt --top 10
    python text_analyzer.py sample_text.txt --top 10 --lemmas
"""

import argparse
import re
import sys
from collections import Counter

# Слово: літери, всередині можуть бути апостроф або дефіс (м'яч, будь-який).
WORD_RE = re.compile(r"[^\W\d_]+(?:['’ʼ-][^\W\d_]+)*")


class EmptyTextError(Exception):
    """Текст порожній або не містить жодного слова."""


def read_text(path):
    """Читає текст із файлу (UTF-8). Помилки файлу передаються вище."""
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def tokenize(text):
    """Розбиває текст на слова в нижньому регістрі.

    Кидає EmptyTextError, якщо слів немає.
    """
    words = WORD_RE.findall(text.lower())
    if not words:
        raise EmptyTextError("Текст порожній або не містить слів.")
    return words


def count_words(words):
    """Загальна кількість слів."""
    return len(words)


def count_unique(words):
    """Кількість унікальних слів."""
    return len(set(words))


def word_frequencies(words):
    """Словник частотності слів (Counter)."""
    return Counter(words)


def lemma_frequencies(words):
    """Частотність лем за допомогою pymorphy3 (українська мова).

    Для кожного слова береться найімовірніший розбір, тому при омонімії
    лема може бути неточною (наприклад, «тому» -> «том»).
    """
    try:
        import pymorphy3
    except ImportError as error:
        raise RuntimeError(
            "Бібліотека pymorphy3 не встановлена. "
            "Виконайте: pip install -r requirements.txt"
        ) from error

    morph = pymorphy3.MorphAnalyzer(lang="uk")
    return Counter(morph.parse(word)[0].normal_form for word in words)


def print_top(title, counter, top):
    """Друкує топ-N найчастіших елементів."""
    print(f"\n{title} (топ {top}):")
    for item, number in counter.most_common(top):
        print(f"  {item:<20} {number}")


def build_parser():
    parser = argparse.ArgumentParser(description="Аналіз частотності слів у тексті.")
    parser.add_argument("path", help="шлях до текстового файлу")
    parser.add_argument("--top", type=int, default=10,
                        help="скільки найчастіших слів показати (за замовчуванням 10)")
    parser.add_argument("--lemmas", action="store_true",
                        help="додатково порахувати частотність лем (pymorphy3)")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)

    try:
        text = read_text(args.path)
        words = tokenize(text)
    except FileNotFoundError:
        print(f"Помилка: файл '{args.path}' не знайдено.")
        return 1
    except PermissionError:
        print(f"Помилка: немає доступу до файлу '{args.path}'.")
        return 1
    except IsADirectoryError:
        print(f"Помилка: '{args.path}' — це папка, а не файл.")
        return 1
    except UnicodeDecodeError:
        print("Помилка: файл не в кодуванні UTF-8.")
        return 1
    except EmptyTextError as error:
        print(f"Помилка: {error}")
        return 1

    print(f"Усього слів: {count_words(words)}")
    print(f"Унікальних слів: {count_unique(words)}")
    print_top("Частотність слів", word_frequencies(words), args.top)

    if args.lemmas:
        try:
            lemmas = lemma_frequencies(words)
        except RuntimeError as error:
            print(f"Помилка: {error}")
            return 1
        print(f"\nУнікальних лем: {len(lemmas)}")
        print_top("Частотність лем", lemmas, args.top)

    return 0


if __name__ == "__main__":
    sys.exit(main())
