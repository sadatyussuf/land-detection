import cv2
import numpy as np


# Line Segment Detector
img = cv2.imread("./imgs/crop.tif",cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

lsd = cv2.createLineSegmentDetector(0)
# print(lsd)
lines = lsd.detect(gray)[0]
# print(lines)

for l in lines:
    print(l)
    (x1, y1, x2, y2) = l[0]
    # (x1, y1, x2, y2) = [4.5861,9.3117,11.8799,3.7544]
    print(x1, y1, x2, y2)
    cv2.line(img, (int(x1), int(y1)), (int(x2),int(y2)), (0, 255, 0), thickness=2)

cv2.imwrite("./imgs/results_LSD.jpg", img)