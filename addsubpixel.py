import cv2
import numpy as np

img = cv2.imread("resources/sunflower.jpg")

#addition of value to image(incraese brightness)
value = np.ones_like(img, dtype='uint8')*50

img_add = cv2.add(img, value)

img_sub = cv2.subtract(img, value)

cv2.imshow("Original", img)
cv2.imshow("Addition", img_add)
cv2.imshow("subtruction", img_sub)

cv2.waitKey(0)