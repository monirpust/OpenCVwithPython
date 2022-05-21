import cv2
import numpy as np

img = np.zeros((512, 512,3), np.uint8)
# print(img)
# img[200:300, 300:350] = 255, 0, 0

#putting different shape
cv2.line(img, (0,0), (200, 300), (0,255,0), 3)
cv2.rectangle(img, (100,100), (250, 350),(0,0,255), cv2.FILLED)
cv2.circle(img, (400,50), 30, (255, 255,0), 15)

#putting text on image
cv2.putText(img, "OPENCV", (300,200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 2)

cv2.imshow("Image created", img)

cv2.waitKey(0)