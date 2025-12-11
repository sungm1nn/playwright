# playwright

# OS : Ubuntu 24.04 (WSL 환경)
# VS-code, MobaXterm
# playwright : 1.57.0

# 필수 패키지 업데이트
$ sudo apt update && sudo apt upgrade -y

# venv 패키지 설치
$ sudo apt install python3-venv -y

# playwright 환경 세팅
$ mkdir playwright
$ cd playwright

# 가상환경 생성, activate
$ python3 -m venv venv
$ source venv/bin/activate

# pytest, playwright 설치
$ pip install --upgrade pip
$ pip install pytest pytest-playwright
$ playwright install

# Ubuntu 24.04 에서 playwright 부족한 패키지 설치 (위에서 node-playwright 없다고 나왔을 시에 수행)
$ playwright install-deps


