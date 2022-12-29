import cv2
import numpy as np


def median_filter(img, img_name):
    """Median filter"""

    # height, width, number of channels (RGB) in image
    width, height, channels = img.shape

    # Traverse the image. For every 4x4 area, find the median of the pixels and replace the ceter pixel by the median
    new_image = np.zeros([width, height, channels])

    # size of the mask
    sz = 4
    # Traverse the image. For every 4x4 area,
    for x in range(1, width - 1):
        for y in range(1, height - 1):
            for color in range(channels):
                tmp = []
                for dx in range(-sz, sz):
                    for dy in range(-sz, sz):
                        new_x = x + dx
                        new_y = y + dy
                        if new_x < 0 or new_x >= width:
                            continue
                        if new_y < 0 or new_y >= height:
                            continue
                        tmp.append(img[new_x, new_y, color])

                # sort the list and find the median
                tmp.sort()

                # replace the ceter pixel by the median
                new_image[x, y, color] = tmp[int(len(tmp) / 2)]

    # convert the image to uint8
    new_image = new_image.astype(np.uint8)

    # the output path to save the image
    output_path = f"EditedImages/median_filtering_{img_name}"

    # save the image to the output path
    cv2.imwrite(output_path, new_image)

    # return the image and the output path
    return new_image, output_path
