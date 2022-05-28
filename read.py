import cv2 as cv

# for reading images
# img = cv.imread('Photos/cat_large.jpg')
# cv.imshow('Cat', img)

# for reading video
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows

cv.waitKey(0)
