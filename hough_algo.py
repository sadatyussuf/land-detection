import cv2
import numpy as np


# Hough Algorithm
img = cv2.imread("./imgs/crop.tif",cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 100, 200, apertureSize=3)
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 15, minLineLength=10, maxLineGap=10)

for i in range(0, len(lines)):
    for x1, y1, x2, y2 in lines[i]:
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), thickness=2)

cv2.imwrite("./imgs/results_Hough.jpg", img)
