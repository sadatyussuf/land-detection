import random
import numpy as np
import cv2


img = cv2.imread('./img/crop.tif')
cv2.imshow('test_dta', img)
cv2.destroyAllWindows()
# cv2.imwrite('./line2_RANSAC.bmp', img)

data = []
test_data = []
for i in range(len(img)):
    for j in range(len(img[0])):
        if img[i][j][0] == 255:
            data.append((j, i))
            test_data.append((j, i))

threshold = 0.01
most_voted = 0
best_line = None

while len(test_data) > 1:
    vote = 0

    rnd = random.randint(0, len(test_data) - 1)
    p1 = test_data[rnd]
    test_data.pop(rnd)

    rnd = random.randint(0, len(test_data) - 1)
    p2 = test_data[rnd]
    test_data.pop(rnd)

    delta_p2p1 = (p2[0] - p1[0], p2[1] - p1[1])
    for i in range(len(data)):
        delta_p1p3 = (p1[0] - data[i][0], p1[1] - data[i][1])
        d = np.linalg.norm(np.cross(delta_p2p1, delta_p1p3)
                           ) / np.linalg.norm(delta_p2p1)

        if d <= threshold:
            vote += 1

    if vote > most_voted:
        most_voted = vote
        best_line = (p1, p2)


p1, p2 = best_line

cv2.line(img, (p1[0], p1[1]), (p2[0], p2[1]), (0, 255, 0), thickness=1)
cv2.imwrite('./img/line2_RANSAC.bmp', img)
