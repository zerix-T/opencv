import  cv2 as cv
#testing addWeighted function
img1 = cv.imread('cat.jpg')
img2 = cv.imread('cat.jpg')

imgo = cv.addWeighted(img1,0.5,img2,1,0.0)

cv.imshow('imgo',imgo)
cv.imshow('original',img1)
cv.waitKey(0)