import cv2 as cv
import numpy as np
# Color Detection

def empty(a):
    pass

cv.namedWindow("Trackbars")
cv.resizeWindow("Trackbars",640,240)
cv.createTrackbar('Hue Min','Trackbars',0,179,empty)
cv.createTrackbar('Hue Max','Trackbars',179,179,empty)
cv.createTrackbar('Sat Min','Trackbars',122,255,empty)
cv.createTrackbar('Sat Max','Trackbars',255,255,empty)
cv.createTrackbar('Val Min','Trackbars',235,255,empty)
cv.createTrackbar('Val Max','Trackbars',255,255,empty)


while True:
    img = cv.imread('car.jpg')
    imghsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    h_min = cv.getTrackbarPos('Hue Min','Trackbars')
    h_max = cv.getTrackbarPos('Hue Max', 'Trackbars')
    s_min = cv.getTrackbarPos('Sat Min', 'Trackbars')
    s_max = cv.getTrackbarPos('Sat Max', 'Trackbars')
    v_min = cv.getTrackbarPos('Val Min', 'Trackbars')
    v_max = cv.getTrackbarPos('Val Max', 'Trackbars')
    print(h_min,h_max,s_min,s_max,v_min,v_max)

    lower = np.array([h_min,s_min,v_min])
    uper = np.array([h_max,s_max,v_max])

    mask = cv.inRange(imghsv,lower,uper)
    imgres = cv.bitwise_and(img,img,mask=mask)

    cv.imshow('Kitty',img)
    cv.imshow('hsv',imghsv)
    cv.imshow('Masked',mask)
    cv.imshow('result',imgres)

    cv.waitKey(1)