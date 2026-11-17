import os
import tempfile
import unittest

import text_analyzer as ta


class TestTokenizeAndCount(unittest.TestCase):
    def test_count_words(self):
        words = ta.tokenize("Мама мила раму.")
        self.assertEqual(ta.count_words(words), 3)

    def test_count_unique(self):
        words = ta.tokenize("кіт кіт пес")
        self.assertEqual(ta.count_unique(words), 2)

    def test_case_insensitive(self):
        words = ta.tokenize("Слово слово СЛОВО")
        self.assertEqual(ta.count_unique(words), 1)

    def test_punctuation_and_digits_ignored(self):
        words = ta.tokenize("Привіт, світе! 2026 рік...")
        self.assertEqual(words, ["привіт", "світе", "рік"])

    def test_apostrophe_and_hyphen_kept(self):
        words = ta.tokenize("м'яч будь-який")
        self.assertEqual(words, ["м'яч", "будь-який"])

    def test_frequencies(self):
        freq = ta.word_frequencies(ta.tokenize("а б а в а б"))
        self.assertEqual(freq["а"], 3)
        self.assertEqual(freq["б"], 2)
        self.assertEqual(freq.most_common(1), [("а", 3)])


class TestErrors(unittest.TestCase):
    def test_empty_text(self):
        with self.assertRaises(ta.EmptyTextError):
            ta.tokenize("")

    def test_only_punctuation(self):
        with self.assertRaises(ta.EmptyTextError):
            ta.tokenize("... !!! 123")

    def test_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            ta.read_text("no_such_file_12345.txt")

    def test_directory_instead_of_file(self):
        with tempfile.TemporaryDirectory() as folder:
            code = ta.main([folder])
            self.assertEqual(code, 1)


class TestFileReading(unittest.TestCase):
    def test_read_text_and_main(self):
        with tempfile.NamedTemporaryFile(
            "w", suffix=".txt", delete=False, encoding="utf-8"
        ) as tmp:
            tmp.write("Мова і слово, слово і мова.")
            path = tmp.name
        try:
            self.assertEqual(ta.read_text(path), "Мова і слово, слово і мова.")
            self.assertEqual(ta.main([path, "--top", "3"]), 0)
        finally:
            os.remove(path)


if __name__ == "__main__":
    unittest.main()
