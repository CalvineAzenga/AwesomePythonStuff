import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
address="https://192.168.43.1:8080/video"
video=cv2.VideoCapture(address)


while True:
    check,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
    for x,y,w,h in face:
        img=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow("gottcha",frame)
    key=cv2.waitKey(1)

    