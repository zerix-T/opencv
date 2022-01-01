import cv2 as cv
#detecting faces in webcam

faceCas = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

Cam = cv.VideoCapture(0)

while True:
    success, frame = Cam.read()
    #frame = cv.cvtColor(frame01,cv.COLOR_BGR2GRAY)
    faces = faceCas.detectMultiScale(frame,1.1,5)

    for (x,y,w,h) in faces:
        frame = cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),4)

    cv.imshow("Face detector",frame)
    if cv.waitKey(1)& 0xFF == ord('m'):
        break

Cam.release()
cv.destroyAllWindows()