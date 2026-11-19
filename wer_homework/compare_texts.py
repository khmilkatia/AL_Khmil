"""Читає два тексти, обчислює WER і зберігає метрики у JSON-файл.

Запуск:
    python3 compare_texts.py
    python3 compare_texts.py reference.txt hypothesis.txt result.json
"""

import json
import sys

from wer import wer


def read_text(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def main():
    ref_path = sys.argv[1] if len(sys.argv) > 1 else "reference.txt"
    hyp_path = sys.argv[2] if len(sys.argv) > 2 else "hypothesis.txt"
    out_path = sys.argv[3] if len(sys.argv) > 3 else "result.json"

    try:
        reference = read_text(ref_path)
        hypothesis = read_text(hyp_path)
        metrics = wer(reference, hypothesis)
    except FileNotFoundError as error:
        print(f"Файл не знайдено: {error.filename}")
        return
    except ValueError as error:
        print(f"Помилка: {error}")
        return

    with open(out_path, "w", encoding="utf-8") as file:
        json.dump(metrics, file, ensure_ascii=False, indent=2)

    print(f"Еталон: {ref_path}")
    print(f"Розпізнаний текст: {hyp_path}")
    print(f"WER = {metrics['WER']} ({metrics['WER'] * 100:.2f}%)")
    print(f"S (заміни) = {metrics['S']}")
    print(f"D (пропуски) = {metrics['D']}")
    print(f"I (вставки) = {metrics['I']}")
    print(f"N (слів в еталоні) = {metrics['N']}")
    print(f"Метрики збережено у {out_path}")


if __name__ == "__main__":
    main()