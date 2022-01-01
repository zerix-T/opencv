import cv2 as cv
import numpy as np


cam = cv.VideoCapture(0)

def empty(a):
    pass

cv.namedWindow("Trackbars")
cv.resizeWindow("Trackbars",640,240)
cv.createTrackbar('Hue Min','Trackbars',0,179,empty)
cv.createTrackbar('Hue Max','Trackbars',179,179,empty)
cv.createTrackbar('Sat Min','Trackbars',0,255,empty)
cv.createTrackbar('Sat Max','Trackbars',255,255,empty)
cv.createTrackbar('Val Min','Trackbars',0,255,empty)
cv.createTrackbar('Val Max','Trackbars',255,255,empty)

while True:
    m , img = cam.read()
    imgHSV = cv.cvtColor(img,cv.COLOR_BGR2HSV)

    h_min = cv.getTrackbarPos('Hue Min', 'Trackbars')
    h_max = cv.getTrackbarPos('Hue Max', 'Trackbars')
    s_min = cv.getTrackbarPos('Sat Min', 'Trackbars')
    s_max = cv.getTrackbarPos('Sat Max', 'Trackbars')
    v_min = cv.getTrackbarPos('Val Min', 'Trackbars')
    v_max = cv.getTrackbarPos('Val Max', 'Trackbars')

    lower = np.array([h_min, s_min, v_min])
    uper = np.array([h_max, s_max, v_max])

    mask = cv.inRange(imgHSV, lower, uper)
    imgres = cv.bitwise_and(img, img, mask=mask)

    cv.imshow('cam',img)
    cv.imshow('hsv',mask)
    cv.imshow('result',imgres)
    if cv.waitKey(1) & 0xFF == ord('s'):
        break