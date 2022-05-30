import cv2

img = cv2.imread("resources/sunflower.jpg")

height, width, channels = img.shape

rotation_matrix = cv2.getRotationMatrix2D(( width/2, height/2), 90, 0.5)

rotatedImage = cv2.warpAffine(img, rotation_matrix, (width, height))

cv2.imshow("image", img)

cv2.imshow("rotated", rotatedImage)

cv2.waitKey(0)