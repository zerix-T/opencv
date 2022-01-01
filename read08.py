import cv2 as cv
import numpy as np
#Contours and shape detection

def getContours(img):
    contours,hierarchy = cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    for c in contours:
        area = cv.contourArea(c)
        print(area)
        if area > 200:
            cv.drawContours(imgc,c,-1,(255,0,0),5)
            peri = cv.arcLength(c,True)
            approx = cv.approxPolyDP(c,0.02*peri,True)
            print(len(approx))
            objcor = len(approx)
            x,y,w,h = cv.boundingRect(approx)

            if objcor == 3 : objectType = 'Triangle'
            elif objcor ==4:
                aspRatio = w/float(h)
                if aspRatio > 0.95 and aspRatio < 1.05: objectType = 'Square'
                else: objectType = 'Rectangle'
            elif objcor>4:objectType='Circle'
            else:objectType='None'

            cv.rectangle(imgc, (x, y), (x + w, y + h), (255, 255, 0), 2)
            cv.putText(imgc,objectType,(x+(w//2)-25,y+(h//2)+5),cv.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)


img0 = cv.imread('shapes.jpg')
img = cv.resize(img0,(800,700))
imgc = img.copy()
imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv.Canny(imgBlur,20,20)

getContours(imgCanny)

cv.imshow('shapes',img)
#cv.imshow('blurred',imgBlur)
cv.imshow('canny',imgCanny)
cv.imshow('contoured',imgc)
cv.waitKey(0)
