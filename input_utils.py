def get_text(prompt):
    """빈 문자열이 아닌 입력을 받을 때까지 반복한다."""

    while True:
        value = input(prompt).strip()

        if not value:
            print("⚠️ 입력값이 없습니다. 다시 입력해 주세요.")
            continue

        return value


def get_number(prompt, minimum, maximum):
    """지정된 범위의 정수를 입력받는다."""

    while True:
        value = input(prompt).strip()

        if not value:
            print("⚠️ 입력값이 없습니다. 다시 입력해 주세요.")
            continue

        try:
            number = int(value)
        except ValueError:
            print("⚠️ 숫자만 입력해 주세요.")
            continue

        if not minimum <= number <= maximum:
            print(
                f"⚠️ {minimum}부터 {maximum}까지의 숫자를 입력해 주세요."
            )
            continue

        return number
