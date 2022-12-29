# Low Pass Spatial Domain Filtering  to observe the blurring effect
import cv2
import numpy as np


def average_filter(img, img_name):
    """Average filter"""
    """Average filter"""

    # height, width, number of channels (RGB) in image
    height, width, channels = img.shape

    # Convolve the 3X3 mask over the image
    img_new = np.zeros([height, width, channels])

    # Traverse the image. For every 3X3 area,
    for x in range(1, height - 1):
        for y in range(1, width - 1):
            for color in range(channels):
                tmp = 0
                # find the average of the pixels and
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        xx = x + dx
                        yy = y + dy
                        tmp += img[xx, yy, color]

                # replace the ceter pixel by the average
                img_new[x, y, color] = tmp / 9

    # the output path to save the image
    output_path = f"EditedImages/mostly_low_pass_{img_name}"

    # save the image to the output path
    cv2.imwrite(output_path, img_new)

    # return the image and the output path
    return img_new, output_path
