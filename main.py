import cv2 as cv
from PIL import Image


def crop_image():
    print('start crop_img func...')
    img = Image.open('tet1.tif')
    width, height = img.size
    x = 830  # 800 360
    y = 400  # 370 140
    x1 = x + 30  # 60
    y1 = y + 30
    # crop image with the given width and height
    im1 = img.crop((x, y, width-x1, height - y1))  # y+height
    im1.save("./crop.tif", "TIFF")
    # print(cc)
    print('finished crop_img func...')


def detectPolygon():
    print('start detectPolygon func...')
    img = cv.imread('.imgs/crop.tif', cv.IMREAD_ANYCOLOR | cv.IMREAD_ANYDEPTH)

    # Convert to grayscale image
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Determine edges of objects in an image
    img_edged = cv.Canny(img_gray, 170, 255)

    # applies fixed-level thresholding to a multiple-channel array. gets binary image out of a grayscale image.
    ret, threshold = cv.threshold(img_gray, 240, 255, cv.THRESH_BINARY)

    # Finds contours in a binary image.
    contours, _ = cv.findContours(
        img_edged, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    def detectShape(c):
        # Calculates a contour perimeter or a curve length.
        perimeter = cv.arcLength(contour, True)
        #  Approximates a polygonal curve(s)
        shape = cv.approxPolyDP(contour, 0.01*perimeter, True)
        sides = len(shape)
        X_COR = shape.ravel()[0]
        Y_COR = shape.ravel()[1]

        if sides == 4:
            x, y, w, h = cv.boundingRect(contour)
            aspectratio = float(w)/h
            cv.drawContours(img, [contour], 0, (0, 0, 255), 4)
            if (aspectratio >= 0.9 or aspectratio <= 1.1):
                cv.putText(img, 'square', (X_COR, Y_COR),
                           cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            else:
                cv.putText(img, 'rectangle', (X_COR, Y_COR),
                           cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    count = 0
    for contour in contours:
        count += 1
        print(f'calling detectShape func {count} times')
        shape = detectShape(contour)
        filename = 'result19.tif'
        cv.imwrite(filename, img)
    # cv.imshow('polygons_detected',img)
    # cv.waitKey(0)
    cv.destroyAllWindows()
    print('finished')
    print('finished detectPolygon func...')


def image_converter():
    print('start img_converter func...')
    img = Image.open('./result19.tif')
    img = img.convert("RGBA")
    data = img.getdata()

    imgData = []
    for item in data:
        # check if the pixel is red
        if item[0] == 255 and item[1] == 0 and item[2] == 0:
            imgData.append((255, 0, 0, 255))
        # else make it transparent
        else:
            imgData.append((255, 255, 255, 0))

    img.putdata(imgData)
    img.save("./result1.tif", "TIFF")
    print('finished img_converter func...')


if __name__ == '__main__':
    crop_image()
    detectPolygon()
    image_converter()
