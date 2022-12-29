# Apply contrast stretching method
import cv2
import numpy as np
maxiI = 250
miniI = 3

maxoI = 255
minoI = 0


def contrast_stretching(img, img_name):

    stretched_image = img

    # get height and width of the image
    height, width, _ = img.shape

    # get the minimum and maximum pixel values
    maxiI, miniI = np.max(img), np.min(img)

    # set the output range
    maxoI, minoI = 255, 0

    for i in range(0, height - 1):
        for j in range(0, width - 1):

            # Get the pixel value
            pixel = stretched_image[i, j]

            # scale each pixel by this formula
            """
            pout = (pin - miniI) * ((maxoI-minoI) / (maxiI-miniI)) + minoI

            """

            # 1st index contains red pixel
            pixel[0] = (pixel[0] - miniI) * ((maxoI - minoI) / (maxiI - miniI)) + minoI

            # 2nd index contains green pixel
            pixel[1] = (pixel[1] - miniI) * ((maxoI - minoI) / (maxiI - miniI)) + minoI

            # 3rd index contains blue pixel
            pixel[2] = (pixel[2] - miniI) * ((maxoI - minoI) / (maxiI - miniI)) + minoI

            # Store new values in the pixel
            stretched_image[i, j] = pixel

    output_path = f'EditedImages/contrast_stretching_{img_name}'
    cv2.imwrite(output_path, stretched_image)

    return stretched_image, output_path
