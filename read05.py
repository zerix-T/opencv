import cv2 as cv
import numpy as np
#warping perspective

img = cv.imread('card.jpg')

width, height = 250,350
pt1 = np.float32([[403,41],[563,136],[259,287],[420,382]])
pt2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
mat = cv.getPerspectiveTransform(pt1,pt2)
outimg = cv.warpPerspective(img,mat,(width,height))

cv.imshow('cards',img)
cv.imshow('warpped card',outimg)
cv.waitKey(0)
