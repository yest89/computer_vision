import cv2
import numpy as np


def modification_for_picture_1():
    image_filename = 'Images/hearts_1.png'
    img = cv2.imread(image_filename)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    kernel = np.ones((1, 1), np.uint8)
    dilation = cv2.dilate(img, kernel, iterations=1)

    th, im_th = cv2.threshold(dilation, 3, 255, cv2.THRESH_TOZERO)

    result = im_th.copy()

    h, w = im_th.shape

    # create zeros mask 2 pixels larger in each dimension
    mask = np.zeros([h + 2, w + 2], np.uint8)

    cv2.floodFill(result, mask, (0, 0), (255, 255, 255), (3, 151, 65), (3, 151, 65), flags=8)
    cv2.floodFill(result, mask, (38, 313), (255, 255, 255), (3, 151, 65), (3, 151, 65), flags=8)
    cv2.floodFill(result, mask, (363, 345), (255, 255, 255), (3, 151, 65), (3, 151, 65), flags=8)
    cv2.floodFill(result, mask, (619, 342), (255, 255, 255), (3, 151, 65), (3, 151, 65), flags=8)

    # write result to disk
    cv2.imwrite("picture1.jpg", result)

    # display it
    cv2.imshow("result", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# *******************************************************************************
#                           M A I N    P R O G R A M                            *
# *******************************************************************************


if __name__ == '__main__':
    modification_for_picture_1()
