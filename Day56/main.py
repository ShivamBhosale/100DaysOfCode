import cv2 as cv
import numpy as np

""" Reading the image """
img = cv.imread("me.jpg")

""" Edges """

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray,5)
edges = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,9,9)

""" Cartoonification """

color = cv.bilateralFilter(img,9,250,250)
cartoon = cv.bitwise_and(color,color,mask=edges)
cartoon = cv.resize(cartoon, (960, 540)) 


cv.imshow("cartoon",cartoon)
cv.waitKey(0)
cv.destroyAllWindows()