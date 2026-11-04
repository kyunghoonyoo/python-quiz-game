# Python 기초 퀴즈 게임

## 1. 프로젝트 소개

Python 기초 문법을 학습하고 확인할 수 있는 콘솔 기반 객관식 퀴즈 게임입니다.

사용자는 기본 퀴즈를 풀거나 새로운 문제를 직접 추가할 수 있습니다. 퀴즈와 최고 점수는 JSON 파일에 저장되어 프로그램을 종료한 후에도 유지됩니다.

## 2. 주제 선정 이유

Python을 처음 배우는 학습자가 기본 문법을 반복해서 학습하고 확인할 수 있도록 이 프로젝트를 제작했습니다.

변수, 자료형, 리스트, 조건문, 반복문, 함수 등 프로그래밍 입문에 필요한 개념을 문제로 구성했습니다.

## 3. 개발 환경

- 운영체제: Windows 11 / WSL2 Ubuntu
- 프로그래밍 언어: Python 3.10 이상
- 개발 도구: Visual Studio Code
- 버전 관리: Git, GitHub
- 외부 라이브러리: 사용하지 않음 (Python 표준 라이브러리 사용)

## 4. 실행 방법

프로젝트 폴더에서 다음 명령어를 실행합니다.

```bash
cd ~/projects/python-quiz-game
source .venv/bin/activate
python main.py
```

## 5. 주요 기능

1. **퀴즈 풀기:** 등록된 문제를 풀고 정답 수와 점수를 확인합니다.
2. **퀴즈 추가:** 문제, 선택지 4개, 정답 번호를 직접 입력합니다.
3. **퀴즈 목록:** 등록된 전체 문제를 확인합니다.
4. **최고 점수 확인:** 저장된 최고 점수를 확인합니다.
5. **프로그램 종료:** 데이터를 저장하고 안전하게 종료합니다.

추가 기능:

- 퀴즈 무작위 출제
- 잘못된 입력값 검증 및 재입력
- 최고 점수 자동 갱신
- JSON 데이터 저장 및 불러오기
- Ctrl+C 및 EOFError 발생 시 안전 종료

## 6. 클래스 및 모듈 구성

### Quiz

개별 퀴즈의 문제, 선택지, 정답을 관리합니다. 정답 여부를 확인하고 퀴즈 데이터를 사전 형태로 변환하는 기능을 담당합니다.

### QuizGame

게임의 전체 흐름을 관리합니다. 메뉴 출력, 퀴즈 진행, 새로운 문제 추가, 퀴즈 목록 및 점수 확인 기능을 담당합니다.

### StateStorage

JSON 파일을 이용한 데이터 저장과 불러오기를 담당합니다. 저장 파일이 없거나 손상된 경우 기본 퀴즈 데이터로 실행할 수 있도록 처리합니다.

### 기타 모듈

- `main.py`: 프로그램 실행 및 안전 종료 처리
- `default_data.py`: 기본 퀴즈 데이터 제공
- `input_utils.py`: 문자열 및 숫자 입력 검증
- `tests/test_quiz.py`: 퀴즈 및 데이터 저장 기능 테스트

## 7. 프로젝트 파일 구조

```text
python-quiz-game/
├── main.py
├── quiz.py
├── quiz_game.py
├── storage.py
├── default_data.py
├── input_utils.py
├── state.json
├── README.md
├── .gitignore
├── tests/
│   ├── __init__.py
│   └── test_quiz.py
└── docs/
    └── screenshots/
        ├── 01_environment.png
        ├── 02_project_structure.png
        ├── 03_menu.png
        ├── 04_quiz_add.png
        ├── 05_quiz_list.png
        ├── 06_quiz_play.png
        ├── 07_score.png
        ├── 08_data_persistence.png
        ├── 09_invalid_input.png
        ├── 10_git_branch_merge.png
        ├── 11_clone_pull.png
        └── 12_tests.png
```

## 8. 데이터 저장 방식

퀴즈와 최고 점수는 프로젝트 루트의 `state.json` 파일에 JSON 형식으로 저장됩니다.

- **저장 형식:** JSON
- **문자 인코딩:** UTF-8
- **퀴즈 정보:** 문제, 선택지 4개, 정답 번호
- **점수 정보:** 최고 정답 개수

프로그램을 다시 실행하면 저장된 데이터를 불러옵니다. 저장 파일이 없거나 손상된 경우 기본 퀴즈 데이터로 실행합니다.

## 9. 테스트 및 Git 실습

### 자동 테스트

Python 표준 라이브러리 `unittest`를 사용하여 퀴즈 및 JSON 데이터 저장 기능을 검증합니다.

다음 명령어로 테스트를 실행할 수 있습니다.

```bash
python -m unittest discover -s tests -v
```

총 8개의 테스트를 통해 정답 확인, 잘못된 입력에 대한 예외 처리, 데이터 변환, JSON 저장 및 복구 기능을 검사합니다.

### Git 브랜치 실습

- `main` 브랜치에서 기본 프로그램을 개발했습니다.
- `feature/quiz-play` 브랜치를 생성했습니다.
- 퀴즈 결과에 정답률을 표시하는 기능을 추가했습니다.
- 작업 브랜치를 `main` 브랜치에 병합했습니다.

### Git Clone 및 Pull 실습

별도 디렉터리에 GitHub 저장소를 복제했습니다. 복제한 폴더에서 README를 수정하고 commit 및 push를 수행했습니다. 이후 원래 프로젝트 폴더에서 pull을 실행하여 원격 변경사항이 반영되는 것을 확인했습니다.

## 10. 실행 화면

스크린샷은 `docs/screenshots/` 폴더에 저장합니다.

### 01. 개발 환경

![개발 환경](docs/screenshots/01_environment.png)

### 02. 프로젝트 파일 구조

![프로젝트 구조](docs/screenshots/02_project_structure.png)

### 03. 메인 메뉴

![메인 메뉴](docs/screenshots/03_menu.png)

### 04. 퀴즈 추가

![퀴즈 추가](docs/screenshots/04_quiz_add.png)

### 05. 퀴즈 목록

![퀴즈 목록](docs/screenshots/05_quiz_list.png)

### 06. 퀴즈 풀이

![퀴즈 풀이](docs/screenshots/06_quiz_play.png)

### 07. 최고 점수

![최고 점수](docs/screenshots/07_score.png)

### 08. 데이터 저장 및 불러오기

![데이터 저장 및 불러오기](docs/screenshots/08_data_persistence.png)

### 09. 잘못된 입력 처리

![잘못된 입력](docs/screenshots/09_invalid_input.png)

### 10. Git 브랜치 병합

![브랜치 병합](docs/screenshots/10_git_branch_merge.png)

### 11. Git Clone 및 Pull

![Clone 및 Pull](docs/screenshots/11_clone_pull.png)

### 12. 자동 테스트

![자동 테스트](docs/screenshots/12_tests.png)