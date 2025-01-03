import cv2
from ultralytics import YOLO
import numpy as np

def main():
    # YOLO 모델 로드
    model = YOLO('yolov8n.pt')  # 'n'은 nano 버전을 의미합니다. 다른 버전도 사용 가능합니다.

    # 웹캠 초기화
    cap = cv2.VideoCapture(0)  # 0은 기본 웹캠을 의미합니다
    
    while True:
        # 프레임 읽기
        ret, frame = cap.read()
        if not ret:
            break

        # YOLO로 객체 감지 수행
        results = model(frame)
        
        # 결과 시각화
        annotated_frame = results[0].plot()
        
        # 결과 화면에 표시
        cv2.imshow('YOLO 실시간 감지', annotated_frame)
        
        # 'q' 키를 누르면 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # 리소스 해제
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
