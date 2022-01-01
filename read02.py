import cv2
import numpy as np
#differnt effects to an image
kernal = np.ones((5,5),np.uint8)

img = cv2.imread('cat.jpg')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img,(7,7),0)
imgCanny = cv2.Canny(img,150,200)
imgDialation = cv2.dilate(imgCanny,kernal,iterations=1)
imgEroded = cv2.erode(imgDialation,kernal,iterations=1)



cv2.imshow('out',imgBlur)
cv2.imshow('Canny',imgCanny)
cv2.imshow('Dialated',imgDialation)
cv2.imshow('eroded',imgEroded)
cv2.waitKey(0)
