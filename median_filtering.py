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
    for x in range(1, m - 1):
        for y in range(1, n - 1):
            for color in range(rgb):
                tmp = []
                for dx in range(-sz, sz):
                    for dy in range(-sz, sz):
                        new_x = x + dx
                        new_y = y + dy
                        if new_x < 0 or new_x >= m:
                            continue
                        if new_y < 0 or new_y >= n:
                            continue
                        tmp.append(img[new_x, new_y, color])
                tmp.sort()
                img_new1[x, y, color] = tmp[int(len(tmp) / 2)]

    img_new1 = img_new1.astype(np.uint8)
    output_path = f'EditedImages/median_filtering_{img_name}'
    cv2.imwrite(output_path, img_new1)
    return img_new1, output_path
