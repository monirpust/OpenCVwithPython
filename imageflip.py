import cv2

img = cv2.imread("resources/sunflower.jpg")

flipimg = cv2.flip(img, -1)

cv2.imshow("orginal", img)
cv2.imshow("flipped", flipimg)

cv2.waitKey(0)