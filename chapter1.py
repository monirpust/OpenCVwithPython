import cv2
print("Package imported")

img = cv2.imread("resources/monk.jpg")

cv2.imshow("output", img)
cv2.waitKey(0) # 0 for infinite wait

# cap = cv2.VideoCapture("resources/minionpaper.mp4")

# while True:
#     success, img = cap.read()
#     cv2.imshow("video", img)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break