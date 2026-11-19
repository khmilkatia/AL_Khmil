"""Модуль для обчислення Word Error Rate (WER).

WER = (S + D + I) / N, де
    S — кількість замін слів (substitutions),
    D — кількість пропущених слів (deletions),
    I — кількість зайвих слів (insertions),
    N — кількість слів в еталонному тексті (reference).
"""

import re

# Слово: літери, всередині можуть бути апостроф або дефіс.
WORD_RE = re.compile(r"[^\W\d_]+(?:['’ʼ-][^\W\d_]+)*")


def tokenize(text):
    """Розбиває текст на слова в нижньому регістрі (без розділових знаків)."""
    return WORD_RE.findall(text.lower())


def wer(reference, hypothesis):
    """Обчислює WER між еталонним і розпізнаним текстами.

    Повертає словник {"WER": ..., "S": ..., "D": ..., "I": ..., "N": ...}.
    """
    ref = tokenize(reference)
    hyp = tokenize(hypothesis)
    n = len(ref)
    if n == 0:
        raise ValueError("Еталонний текст порожній: N = 0, WER не визначений.")

    # dist[i][j] — мінімальна кількість помилок між ref[:i] і hyp[:j]
    dist = [[0] * (len(hyp) + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][0] = i                      # усі слова пропущені
    for j in range(1, len(hyp) + 1):
        dist[0][j] = j                      # усі слова зайві

    for i in range(1, n + 1):
        for j in range(1, len(hyp) + 1):
            cost = 0 if ref[i - 1] == hyp[j - 1] else 1
            dist[i][j] = min(
                dist[i - 1][j - 1] + cost,  # збіг або заміна
                dist[i - 1][j] + 1,         # пропуск слова (deletion)
                dist[i][j - 1] + 1,         # зайве слово (insertion)
            )

    # Зворотний прохід: рахуємо, скільки було замін, пропусків і вставок
    s = d = ins = 0
    i, j = n, len(hyp)
    while i > 0 or j > 0:
        if i > 0 and j > 0:
            cost = 0 if ref[i - 1] == hyp[j - 1] else 1
            if dist[i][j] == dist[i - 1][j - 1] + cost:
                s += cost
                i -= 1
                j -= 1
                continue
        if i > 0 and dist[i][j] == dist[i - 1][j] + 1:
            d += 1
            i -= 1
        else:
            ins += 1
            j -= 1

    return {
        "WER": round((s + d + ins) / n, 4),
        "S": s,
        "D": d,
        "I": ins,
        "N": n,
    }