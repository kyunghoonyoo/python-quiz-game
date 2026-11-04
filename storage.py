import json
from pathlib import Path

from quiz import Quiz
from default_data import create_default_quizzes


class StateStorage:
    """게임 데이터를 JSON 파일로 저장하고 불러오는 클래스."""

    def __init__(self, filename="state.json"):
        self.path = Path(__file__).resolve().parent / filename

    def load(self):
        """저장된 데이터를 불러온다."""

        if not self.path.exists():
            print("📂 저장 파일이 없습니다. 기본 데이터를 사용합니다.")
            return create_default_quizzes(), 0

        try:
            with self.path.open("r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, dict):
                raise ValueError("데이터 구조가 올바르지 않습니다.")

            raw_quizzes = data.get("quizzes")
            best_score = data.get("best_score", 0)

            if not isinstance(raw_quizzes, list):
                raise ValueError("퀴즈 목록이 올바르지 않습니다.")

            if type(best_score) is not int or best_score < 0:
                raise ValueError("최고 점수가 올바르지 않습니다.")

            quizzes = [
                Quiz.from_dict(item)
                for item in raw_quizzes
            ]

            return quizzes, best_score

        except (json.JSONDecodeError, ValueError, TypeError, OSError) as error:
            print(f"⚠️ 저장 파일을 읽을 수 없습니다: {error}")
            print("기본 퀴즈 데이터로 초기화합니다.")
            return create_default_quizzes(), 0

    def save(self, quizzes, best_score):
        """게임 데이터를 JSON 파일에 저장한다."""

        data = {
            "quizzes": [quiz.to_dict() for quiz in quizzes],
            "best_score": best_score
        }

        temporary_path = self.path.with_suffix(".tmp")

        try:
            with temporary_path.open("w", encoding="utf-8") as file:
                json.dump(
                    data,
                    file,
                    ensure_ascii=False,
                    indent=4
                )

            temporary_path.replace(self.path)
            print("💾 데이터 저장 완료!")
            return True

        except OSError as error:
            print(f"⚠️ 데이터 저장에 실패했습니다: {error}")

            try:
                temporary_path.unlink(missing_ok=True)
            except OSError:
                pass

            return False
