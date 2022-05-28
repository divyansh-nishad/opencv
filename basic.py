import cv2 as cv

img = cv.imread('Photos/park.jpg')
cv.imshow('Boston', img)

# COnverting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blurring the image
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

cv.waitKey(0)
