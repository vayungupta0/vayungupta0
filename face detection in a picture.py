import cv2 as cv
import pyttsx3

img = cv.imread('resources\cat.jfif')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
haar_cascade = cv.CascadeClassifier('harcascades\haarcascades\haarcascade_frontalcatface.xml')
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
print(f'Number of faces found = {len(faces_rect)}')
pyttsx3.speak(f"No of faces detected is {len(faces_rect)}")

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img)
cv.waitKey(0)