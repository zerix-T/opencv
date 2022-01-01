import cv2 as cv
import numpy as np
# creating shapes and text

img = np.zeros((400,400,3),np.uint8)
# print(img)
# img[:] = 255,0,0

cv.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
cv.rectangle(img,(50,50),(250,350),(0,0,255),2)
#cv.rectangle(img,(50,50),(250,350),(0,0,255),cv.FILLED)

cv.circle(img,(200,200),50,(255,255,0),3)
cv.putText(img,"OpenCV ing",(150,200),cv.FONT_HERSHEY_COMPLEX,1,(0,150,0),2)

cv.imshow('matimg',img)
cv.waitKey(0)