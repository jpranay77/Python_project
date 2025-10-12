import cv2
from fer import FER

detector = FER(mtcnn=True)

def analyze_face():
    cap = cv2.VideoCapture(0)  # open webcam
    ret, frame = cap.read()
    cap.release()

    if not ret:
        return 0.0  # default if no webcam

    emotions = detector.detect_emotions(frame)
    if emotions:
        # sadness probability of first detected face
        return emotions[0]["emotions"]["sad"]
    return 0.0
