import cv2 as cv
import numpy as np

Cam = cv.VideoCapture(0)

MyColors = [[158, 73, 255, 179, 255, 255], [40, 31, 0, 94, 255, 225]]  # 0, 179, 176, 255, 114, 255
colorValues = [[0, 0, 255], [0, 255, 0]]
myPoints = []


def findColor(img, MyColors, colorValues):
    imghsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in MyColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv.inRange(imghsv, lower, upper)
        x, y = getContours(mask)
        cv.circle(imgResult, (x, y), 10, colorValues[count], cv.FILLED)
        if x != 0 and y != 0:
            newPoints.append([x, y, count])
        count += 1
        cv.imshow(str(color[0]), mask)
    return newPoints


def getContours(frame):
    contours, hierarchy = cv.findContours(frame, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for c in contours:
        area = cv.contourArea(c)

        if area > 500:
            # cv.drawContours(imgResult, c, -1, (255, 0, 0), 5)
            peri = cv.arcLength(c, True)
            approx = cv.approxPolyDP(c, 0.02 * peri, True)
            x, y, w, h = cv.boundingRect(approx)
    return x + w // 2, y


def drawC(myPoints, colorValues):
    for p in myPoints:
        cv.circle(imgResult, (p[0], p[1]), 10, colorValues[p[2]], cv.FILLED)


while True:
    success, frame = Cam.read()
    imgResult = frame.copy()
    newPoints = findColor(frame, MyColors, colorValues)
    if len(newPoints) != 0:
        for newp in newPoints:
            myPoints.append(newp)
    if len(myPoints) != 0:
        drawC(myPoints, colorValues)
    cv.imshow('Cam', imgResult)

    if cv.waitKey(1) & 0xFF == ord('s'):
        break
