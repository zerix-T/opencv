import cv2 as cv
#reading images, videos and webcam

#img = cv.imread('/home/zerix/Pictures/open_cv_01/cat.jpg',1)
#h,w = img.shape[:2]
# cv.imshow('kitty',img)
#cv.waitKey(0)

cap = cv.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,50)

while True:
    success,img = cap.read()
    cv.imshow('video',img)
    if cv.waitKey(1)& 0xFF == ord('m'):
        break
