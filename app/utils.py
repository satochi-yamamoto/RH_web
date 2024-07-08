import cv2
import numpy as np
import face_recognition

def capture_image():
    video_capture = cv2.VideoCapture(0)
    ret, frame = video_capture.read()
    video_capture.release()
    cv2.destroyAllWindows()
    return frame

def recognize_face(known_face_encodings, face_encoding_to_check):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding_to_check)
    return matches
