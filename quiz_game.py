import random

from quiz import Quiz
from storage import StateStorage
from input_utils import get_text, get_number


class QuizGame:
    """퀴즈 게임 전체를 관리하는 클래스."""

    def __init__(self):
        self.storage = StateStorage()
        self.quizzes, self.best_score = self.storage.load()

    def show_menu(self):
        """메인 메뉴를 출력한다."""

        print("\n" + "=" * 50)
        print("          🎯 PYTHON 기초 퀴즈 게임")
        print("=" * 50)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 최고 점수 확인")
        print("5. 종료")
        print("=" * 50)

    def run(self):
        """메뉴 선택에 따라 기능을 실행한다."""

        while True:
            self.show_menu()
            choice = get_number("메뉴를 선택하세요: ", 1, 5)

            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.show_quizzes()
            elif choice == 4:
                self.show_score()
            elif choice == 5:
                self.save_data()
                print("👋 퀴즈 게임을 종료합니다.")
                break

    def play_quiz(self):
        """퀴즈를 출제하고 점수를 계산한다."""

        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다.")
            return

        questions = self.quizzes.copy()
        random.shuffle(questions)

        total = len(questions)
        correct = 0

        print(f"\n📝 퀴즈를 시작합니다! 총 {total}문제입니다.")

        for index, quiz in enumerate(questions, start=1):
            quiz.display(index)

            answer = get_number("정답 입력 (1-4): ", 1, 4)

            if quiz.is_correct(answer):
                print("✅ 정답입니다!")
                correct += 1
            else:
                print(f"❌ 오답입니다. 정답은 {quiz.answer}번입니다.")

        score = round(correct / total * 100)

        print("\n" + "=" * 50)
        print("🏆 퀴즈 결과")
        print(f"총 {total}문제 중 {correct}문제 정답!")
        print(f"점수: {score}점")
        print(f"정답률: {correct}/{total}")

        if correct > self.best_score:
            self.best_score = correct
            print("🎉 새로운 최고 정답 수입니다!")

        print("=" * 50)
        self.save_data()

    def add_quiz(self):
        """새로운 퀴즈를 등록한다."""

        print("\n📌 새로운 퀴즈를 추가합니다.")

        question = get_text("문제를 입력하세요: ")

        choices = []

        for index in range(1, 5):
            choices.append(
                get_text(f"선택지 {index}: ")
            )

        answer = get_number("정답 번호 (1-4): ", 1, 4)

        quiz = Quiz(question, choices, answer)
        self.quizzes.append(quiz)

        if self.save_data():
            print("✅ 퀴즈가 추가되었습니다!")
        else:
            self.quizzes.pop()
            print("⚠️ 저장에 실패하여 퀴즈 등록을 취소했습니다.")

    def show_quizzes(self):
        """등록된 퀴즈 목록을 출력한다."""

        print("\n📋 등록된 Python 퀴즈 목록")
        print(f"총 {len(self.quizzes)}개의 퀴즈가 있습니다.")

        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[{index}] {quiz.question}")

    def show_score(self):
        """최고 점수를 출력한다."""

        print("\n🏆 최고 점수 확인")

        if self.best_score == 0:
            print("아직 퀴즈를 푼 기록이 없습니다.")
        else:
            print(f"최고 정답 수: {self.best_score}개")

            if self.quizzes:
                print(
                    f"현재 퀴즈 기준 점수: "
                    f"{round(self.best_score / len(self.quizzes) * 100)}점"
                )

    def save_data(self):
        """현재 게임 상태를 저장한다."""

        return self.storage.save(self.quizzes, self.best_score)
