import cv2 as cv

cap = cv.VideoCapture(0)
cascade = cv.CascadeClassifier('harcascades\haarcascades\haarcascade_frontalface_default.xml')
cascade2 = cv.CascadeClassifier('harcascades\haarcascades\haarcascade_eye.xml')
cascade3 = cv.CascadeClassifier('harcascades\haarcascades\haarcascade_hand.xml')
cascade4 = cv.CascadeClassifier('harcascades\haarcascades\haarcascade_upperbody.xml')


while True:
    ret, frame=cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #cv.imshow('Gray People', gray)
    frame = cv.cvtColor(frame, 0)
    detections=cascade.detectMultiScale(gray, 1.3, 7)
    detections2=cascade2.detectMultiScale(gray, 1.3, 7)
    detections3=cascade3.detectMultiScale(gray, 1.3, 7)
    detections4=cascade4.detectMultiScale(gray, 1.3, 7)
   
    if(len(detections2) > 0):
        (x,y,w,h) = detections2[0]
        frame = cv.rectangle(frame, (x,y),(x+w,y+h), (255,0,127), 2)

    if(len(detections) > 0):
        (x,y,w,h) = detections[0]
        frame = cv.rectangle(frame, (x,y),(x+w,y+h), (0,255,0), 2)
    
    if(len(detections3) > 0):
        (x,y,w,h) = detections3[0]
        frame = cv.rectangle(frame, (x,y),(x+w,y+h), (0,255,255), 2)
    
    if(len(detections4) > 0):
        (x,y,w,h) = detections4[0]
        frame = cv.rectangle(frame, (x,y),(x+w,y+h), (255,255,0), 4)
    

    cv.imshow('Face Recognition', frame)
    if cv.waitKey(1) & 0xFF == ord ('q'):
        break

# When everything done, release the capture
print(f'Number of faces found = {len(detections+1)}')
cap.release()
cv.destroyAllWindows()