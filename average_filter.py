# Low Pass Spatial Domain Filtering  to observe the blurring effect
import cv2
import numpy as np


def average_filter(img, img_name):
    """Average filter"""
    '''Average filter'''

    # height, width, number of channels (RGB) in image
    height, width, channels = img.shape

    # Convolve the 3X3 mask over the image
    img_new = np.zeros([height, width, channels])

    for i in range(1, height - 1):
        for j in range(1, width - 1): 
            for color in range(channels): 
                tmp = 0

                for ii in range(-1, 2):
                    for jj in range(-1, 2):
                        xx = i + ii
                        yy = j + jj
                        
                        tmp += img[xx, yy, color]

                img_new[i, j, color] = tmp / 9

    output_path = f'EditedImages/mostly_low_pass_{img_name}'
    cv2.imwrite(output_path, img_new)
    return img_new, output_path
