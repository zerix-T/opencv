import cv2 as cv

#Face Detection

faceCas = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv.imread('faces.jpg')
imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

faces = faceCas.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv.imshow('face',img)
cv.waitKey(0)