import cv2
import numpy as np


def median_filter(img, img_name):
    """Median filter"""
    # Obtain the number of rows and columns
    # of the image
    m, n, rgb = img.shape

    # Traverse the image. For every 3X3 area,
    # find the median of the pixels and
    # replace the ceter pixel by the median
    img_new1 = np.zeros([m, n, rgb])

    sz = 4
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            for color in range(rgb):
                tmp = []
                for ii in range(-sz, sz):
                    for jj in range(-sz, sz):
                        xx = i + ii
                        yy = j + jj
                        if xx < 0 or xx >= m:
                            continue
                        if yy < 0 or yy >= n:
                            continue
                        tmp.append(img[xx, yy, color])
                tmp.sort()
                img_new1[i, j, color] = tmp[int(len(tmp) / 2)]

    img_new1 = img_new1.astype(np.uint8)
    output_path = f'EditedImages/median_filtering_{img_name}'
    cv2.imwrite(output_path, img_new1)
    return img_new1, output_path
