import cv2

import cv2
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
PerritoClassif = cv2.CascadeClassifier('cascade.xml')
while True:
    
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    perro = PerritoClassif.detectMultiScale(gray,
    scaleFactor = 5,
    minNeighbors = 91,
    minSize=(100,78))
    for (x,y,w,h) in perro:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(200,0,200),2)
        cv2.putText(frame,'Perro Bombero',(x,y-10),2,0.7,(200,0,200),2,cv2.LINE_AA)
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()