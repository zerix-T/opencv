import cv2 as cv
#resizing and cropping of an image
img = cv.imread('cat.jpg')
print(img.shape)

imgResize = cv.resize(img,(200,300))
print(imgResize.shape)

imgCrop = img[0:500,100:300]

cv.imshow('img',img)
cv.imshow('cat_resized',imgResize)
cv.imshow('cropped',imgCrop)
cv.waitKey(0)