import cv2
import numpy as np


img = cv2.imread("resources/sunflower.jpg")

horizontalJoinImg = np.hstack((img, img))
verticalJoinImg = np.vstack((img, img))

cv2.imshow("Horizontal Joined Images", horizontalJoinImg)

cv2.imshow("Vertical Joined", verticalJoinImg)

cv2.waitKey(0)