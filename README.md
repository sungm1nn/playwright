# Playwright 기반 웹 테스트 자동화 프로젝트

카카오 OAuth 로그인을 사용하는 웹 서비스에 대해 Playwright + pytest 기반으로 자동화 테스트와 CI(GitHub Actions)를 구성한 프로젝트

OAuth 로그인 특성상 완전 자동화(로그인 혹은 세션 유지)가 어려운 영역과 자동화 가능한 영역을 분리하여 현실적인 테스트 전략 적용

OAuth 로그인 자동화는 세션 유지가 힘들어 수동으로 로그인 후 버튼 테스트 진행

---

## 실행 환경

- OS: Ubuntu 24.04 (WSL)
- IDE : VS Code
- Terminal : MobaXterm
- Python: 3.12
- Playwright: 1.57.0
- Test Framework: pytest
- CI: GitHub Actions

---

## 사전 준비

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-venv -y

$ mkdir playwright
$ cd playwright

#가상환경 생성, activate

$ python3 -m venv venv
$ source venv/bin/activate

#pytest, playwright 설치

$ pip install --upgrade pip
$ pip install pytest pytest-playwright
$ playwright install


# Ubuntu 24.04 에서 playwright 부족한 패키지 설치 (위에서 node-playwright 없다고 나왔을 시에 수행)
$ playwright install-deps
```

---

## 테스트 파일 구조
```bash
tests/
├── main_page.py
├── test_h_button.py
├── main_page_headless_false.py
└── test_h_button_headless_false.py
```

test_h_button.py 는 수동으로 카카오톡 로그인을 통해 햄버거 버튼을 통해 이동할 수 있는 메뉴들에 대해 정상적으로 클릭 가능한지 테스트
main_page.py는 로그인 페이지 접근 가능 여부에 대한 테스트

test_h_button.py 와 main_page.py는 CI 환경(git actions)에서 수행하기 위함
test_h_button.py는 무조건 실패 (로그인을 수동으로 해야하기 때문)
main_page.py는 정상적인 상태에서 수행한다면 성공
위 두 파일 모두, Git Actions 을 통해 Html report 생성됨을 확인

main_page_headless_false.py, test_h_button_headless_false.py는 수동으로 테스트하기 위한 python 파일 (UI 제공, 로그인 후 timeout 5분)

---

## CI 대상 테스트 실행 명령어(UI 제공 안함)
```bash
$ python -m pytest tests/main_page.py --html=report.html --self-contained-html
$ python -m pytest tests/test_h_button.py --html=report.html --self-contained-html
```

## 수동 테스트 실행 명령어 (UI 제공, 로그인 timeout 5분 - 수동)
```bash
python -m pytest tests/main_page_headless_false.py --html=report.html --self-contained-html
python -m pytest tests/test_h_button_headless_false.py --html=report.html --self-contained-html
```

## Git Acitons 설명
```bash
.github/workflows/
├── pass.yml
└── playwright_test.yml
```

pass.yml 은 main_page.py, playwright_test.yml 은 test_h_button.py 에 대한 CI 설정을 포함

Actions에서 go to log-in page로 가면 pass.yml, button test로 가면 test_h_button.py 의 이력을 확인 가능
각 workflow에서 수동 실행 가능하며, Artifacts에서 html을 확인할 수 있음

---

## Slack 알람
테스트 성공/실패 여부만 전송, 테스트 실패 여부에 대한 자세한 사항은 값을 전달받을 수 있는 쿼리 혹은 input 정보가 있으면 더 자세하게 전송 가능할 수도...

