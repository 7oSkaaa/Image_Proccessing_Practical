import cv2


def histo_eq(img, img_name, img_path):
    """Histogram equalization"""
    # convert from RGB color-space to YCrCb
    ycrcb_img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

    # equalize the histogram of the Y channel
    ycrcb_img[:, :, 0] = cv2.equalizeHist(ycrcb_img[:, :, 0])

    # convert back to RGB color-space from YCrCb
    equalized_img = cv2.cvtColor(ycrcb_img, cv2.COLOR_YCrCb2BGR)

    # the output path to save the image
    output_path = f'EditedImages/histo_equalization_{img_name}'

    # save the image to the output path
    cv2.imwrite(output_path, equalized_img)

    # return the equalized image and the output path
    return equalized_img, output_path
