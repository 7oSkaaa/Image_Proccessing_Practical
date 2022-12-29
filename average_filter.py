# Low Pass SPatial Domain Filtering  to observe the blurring effect
import cv2
import numpy as np


def average_filter(img, img_name):
    """Average filter"""
    '''Average filter'''
    # Obtain number of rows and columns
    # of the image
    m, n, rgb = img.shape

    # Convolve the 3X3 mask over the image
    img_new = np.zeros([m, n, rgb])

    for i in range(1, m - 1):
        for j in range(1, n - 1):
            for color in range(rgb):
                tmp = 0
                for ii in range(-1, 2):
                    for jj in range(-1, 2):
                        xx = i + ii
                        yy = j + jj
                        if xx < 0 or xx >= m:
                            continue
                        if yy < 0 or yy >= n:
                            continue
                        tmp += img[xx, yy, color]

                img_new[i, j, color] = tmp / 9

    output_path = f'EditedImages/mostly_low_pass_{img_name}'
    cv2.imwrite(output_path, img_new)
    return img_new, output_path
