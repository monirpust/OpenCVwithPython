import cv2
import numpy as np
from matplotlib import pyplot as plot

originalImg = cv2.imread("resources/sunflower.jpg",0)
equalized = cv2.equalizeHist(originalImg)

cv2.imshow("original", originalImg)
cv2.imshow("equalized", equalized)


plot.hist(originalImg.ravel(), 256, [0, 256])
plot.hist(equalized.ravel(), 256, [0, 256])
plot.show()


cv2.waitKey(0)