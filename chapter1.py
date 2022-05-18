import cv2
print("Package imported")

cap = cv2.VideoCapture("resources/minionpaper.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break