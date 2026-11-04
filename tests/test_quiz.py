import unittest
import tempfile
import json

from pathlib import Path

from quiz import Quiz
from storage import StateStorage


class TestQuiz(unittest.TestCase):

    def setUp(self):
        self.quiz = Quiz(
            "Python에서 출력 함수는?",
            ["input", "print", "len", "type"],
            2
        )

    def test_correct_answer(self):
        self.assertTrue(self.quiz.is_correct(2))

    def test_wrong_answer(self):
        self.assertFalse(self.quiz.is_correct(1))

    def test_invalid_answer(self):
        with self.assertRaises(ValueError):
            Quiz("문제", ["A", "B", "C", "D"], 5)

    def test_invalid_choices(self):
        with self.assertRaises(ValueError):
            Quiz("문제", ["A", "B"], 1)

    def test_to_dict(self):
        data = self.quiz.to_dict()
        self.assertEqual(data["answer"], 2)

    def test_from_dict(self):
        restored = Quiz.from_dict(self.quiz.to_dict())
        self.assertEqual(restored.question, self.quiz.question)


class TestStorage(unittest.TestCase):

    def test_save_and_load(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "state.json"
            storage = StateStorage(str(path))

            quiz = Quiz(
                "Python 함수 키워드는?",
                ["if", "for", "def", "class"],
                3
            )

            self.assertTrue(storage.save([quiz], 1))

            loaded_quizzes, score = storage.load()

            self.assertEqual(len(loaded_quizzes), 1)
            self.assertEqual(score, 1)
            self.assertEqual(loaded_quizzes[0].answer, 3)

    def test_corrupt_json_recovery(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "state.json"
            path.write_text("{invalid json", encoding="utf-8")

            storage = StateStorage(str(path))
            quizzes, score = storage.load()

            self.assertGreaterEqual(len(quizzes), 5)
            self.assertEqual(score, 0)


if __name__ == "__main__":
    unittest.main()
