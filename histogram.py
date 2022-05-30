import cv2
import numpy as np
from matplotlib import pyplot as plot

# img = np.zeros((200, 200), np.uint8)

img = cv2.imread("resources/sunflower.jpg")

# cv2.rectangle(img, (0,100), (200,200), (255), -1)
# cv2.rectangle(img, (0,50), (100,100), (127), -1)
# plot.hist((img))

b,g,r = cv2.split(img)

cv2.imshow("Image",img)

plot.hist(b.ravel(), 256, [0, 256])
plot.hist(g.ravel(), 256, [0, 256])
plot.hist(r.ravel(), 256, [0, 256])
plot.show()


cv2.waitKey(0)
cv2.destroyAllWindows()