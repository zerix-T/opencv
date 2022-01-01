import cv2 as cv
import numpy as np
#images stacking

img = cv.imread('cat.jpg')
hmg = np.hstack((img,img))
#hmg = np.vstack((img,img))

cv.imshow('CAT',img)
cv.imshow('joined',hmg)
cv.waitKey(0)