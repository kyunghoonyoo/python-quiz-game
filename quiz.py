class Quiz:
    """개별 퀴즈를 표현하는 클래스."""

    def __init__(self, question, choices, answer):
        if not isinstance(question, str) or not question.strip():
            raise ValueError("문제는 비어 있을 수 없습니다.")

        if not isinstance(choices, list) or len(choices) != 4:
            raise ValueError("선택지는 정확히 4개여야 합니다.")

        if not all(
            isinstance(choice, str) and choice.strip()
            for choice in choices
        ):
            raise ValueError("선택지는 모두 비어 있지 않아야 합니다.")

        if type(answer) is not int or answer not in range(1, 5):
            raise ValueError("정답은 1부터 4까지여야 합니다.")

        self.question = question.strip()
        self.choices = [choice.strip() for choice in choices]
        self.answer = answer

    def display(self, number):
        """문제와 선택지를 출력한다."""
        print("\n" + "-" * 50)
        print(f"[문제 {number}]")
        print(self.question)

        for index, choice in enumerate(self.choices, start=1):
            print(f"{index}. {choice}")

    def is_correct(self, user_answer):
        """사용자가 입력한 정답을 확인한다."""
        return user_answer == self.answer

    def to_dict(self):
        """Quiz 객체를 JSON 저장용 딕셔너리로 변환한다."""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

    @classmethod
    def from_dict(cls, data):
        """딕셔너리를 Quiz 객체로 변환한다."""
        if not isinstance(data, dict):
            raise ValueError("퀴즈 데이터 형식이 올바르지 않습니다.")

        return cls(
            data.get("question"),
            data.get("choices"),
            data.get("answer")
        )
