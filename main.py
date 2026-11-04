from quiz_game import QuizGame


def main():
    game = QuizGame()

    print("\n🎮 Python 기초 퀴즈 게임을 시작합니다!")

    try:
        game.run()

    except (KeyboardInterrupt, EOFError):
        print("\n\n⚠️ 입력이 중단되었습니다.")
        print("현재 데이터를 안전하게 저장합니다.")
        game.save_data()
        print("👋 프로그램을 안전하게 종료합니다.")


if __name__ == "__main__":
    main()
