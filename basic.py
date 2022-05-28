import cv2 as cv

img = cv.imread('Photos/park.jpg')
cv.imshow('Boston', img)

# COnverting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blurring the image
blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

cv.waitKey(0)
