import pstats
from turtle import width
import cv2
import numpy as np

width, height = 250, 350

img = cv2.imread("resources/card.jpg")

pts1 = np.float32([[240, 260], [435, 225],[285, 545],[505, 500]])
pts2 = np.float32([[0,0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Card Image Original", img)
cv2.imshow("Output image", imgOutput)

cv2.waitKey(0)
