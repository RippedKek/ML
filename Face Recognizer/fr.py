import os
import numpy as np
from PIL import Image
import cv2

def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
    
    coords = []
    
    for (x, y, w, h) in features:
        # Draw rectangle around the detected face
        cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
        
        # Predict the identity of the face
        id, pred = clf.predict(gray_image[y:y+h, x:x+w])  # Corrected the face slicing
        confidence = int(100 * (1 - pred / 300))  # Confidence score calculation
        
        if confidence > 65:  # If confidence is high enough
            if id == 1:
                cv2.putText(img, 'Rohan', (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 1, cv2.LINE_AA)
            elif id == 2:
                cv2.putText(img, 'Sara', (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 1, cv2.LINE_AA)
            elif id == 3:
                cv2.putText(img, 'Jesmin', (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 1, cv2.LINE_AA)
            elif id == 4:
                cv2.putText(img, 'Sarwar', (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 1, cv2.LINE_AA)
        else:
            cv2.putText(img, 'Unknown', (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 1, cv2.LINE_AA)
            
        coords = [x, y, w, h]
        
    return coords

def recognize(img, clf, faceCascade):
    # Perform face detection and recognition
    coords = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), 'Face', clf)
    return img

# Load the face detector and recognizer
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
clf = cv2.face.LBPHFaceRecognizer_create()
clf.read('C:\\Users\\HP\\Documents\\ML\\Face Recognizer\\classifier.xml')

# Start capturing video from the webcam
video_capture = cv2.VideoCapture(0)
while True:
    ret, img = video_capture.read()
    
    # Perform recognition on each frame
    img = recognize(img, clf, faceCascade)
    
    # Display the resulting frame
    cv2.imshow('Face Detection', img)
    
    # Break loop on pressing 'Enter'
    if cv2.waitKey(1) == 13:  # 13 is the Enter key
        break

# Release the webcam and close all windows
video_capture.release()
cv2.destroyAllWindows()
