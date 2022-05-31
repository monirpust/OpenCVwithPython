import cv2
import numpy as np

img = cv2.imread("resources/mercedes.jpg")
print(img.shape)
#resized image
imgResized = cv2.resize(img, (600,200))
print(imgResized.shape)

#cropped image
imgCropped = img[0:150, 0:84]
print(imgCropped.shape)

cv2.imshow("Original Image", img)
cv2.imshow("Resized Image", imgResized)
cv2.imshow("Cropped Image", imgCropped)

cv2.waitKey(0)