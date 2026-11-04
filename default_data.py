from quiz import Quiz


def create_default_quizzes():
    """최초 실행 시 사용할 기본 Python 퀴즈를 생성한다."""

    questions = [
        (
            "Python에서 화면에 값을 출력하는 함수는?",
            ["input()", "print()", "len()", "type()"],
            2
        ),
        (
            "input() 함수가 기본적으로 반환하는 자료형은?",
            ["int", "float", "str", "bool"],
            3
        ),
        (
            "Python에서 참과 거짓을 나타내는 자료형은?",
            ["str", "list", "bool", "dict"],
            3
        ),
        (
            "리스트를 정의하는 올바른 방법은?",
            ["{1, 2, 3}", "[1, 2, 3]", "(1: 2)", "<1, 2, 3>"],
            2
        ),
        (
            "len([10, 20, 30])의 결과는?",
            ["1", "2", "3", "30"],
            3
        ),
        (
            "조건에 따라 다른 코드를 실행할 때 사용하는 키워드는?",
            ["for", "if", "def", "class"],
            2
        ),
        (
            "반복문에서 반복할 때 사용하는 키워드는?",
            ["return", "import", "for", "break"],
            3
        ),
        (
            "함수를 정의할 때 사용하는 키워드는?",
            ["func", "function", "def", "method"],
            3
        )
    ]

    return [
        Quiz(question, choices, answer)
        for question, choices, answer in questions
    ]
