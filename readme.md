# YOLOv8 웹캠을 이용한 실시간 객체 감지 프로젝트

이 프로젝트는 YOLOv8을 사용하여 웹캠에서 실시간으로 객체를 감지하는 프로그램입니다.

## 프로젝트 다운로드

1. 작업 폴더 생성 및 이동
   ```bash
   mkdir yolo_project
   cd yolo_project
   ```

2. GitHub에서 프로젝트 클론
   ```bash
   git clone https://github.com/assistonia/yolo_base.git
   cd yolo_base
   ```

## 설치 방법

### 1. Python 3.10 설치 

https://www.python.org/downloads/release/python-3100/

각 컴퓨터에 맞는 버전을 설치해주세요

### 2. 필요한 패키지 설치
```bash
python -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

웹캠을 연결한 후 프로그램을 실행해주세요

## 실행 방법

1. 프로그램 실행하기
   ```bash
   python yolo.py
   ```

ultralytics 패키지에 대해 자세히 알고싶다면
아래 사이트에서 참고하세요
https://docs.ultralytics.com/ko/
