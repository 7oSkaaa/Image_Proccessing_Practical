import cv2
from matplotlib import pyplot as plt


def histo_eq(img, img_name, img_path):
    """Histogram equalization"""

    # show the histogram of the image before equalization
    plt.figure("Histogram Before Equalization")
    plt.hist(img.flatten(), 256, [0, 256], color="r", label='Histogram Before Equalization')
    plt.xlim([0, 256])
    plt.title("Histogram Before Equalization")
    plt.show()

    # convert from RGB color-space to YCrCb
    ycrcb_img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

    # equalize the histogram of the Y channel
    ycrcb_img[:, :, 0] = cv2.equalizeHist(ycrcb_img[:, :, 0])

    # convert back to RGB color-space from YCrCb
    equalized_img = cv2.cvtColor(ycrcb_img, cv2.COLOR_YCrCb2BGR)

    # show the histogram of the image after equalization
    plt.figure("Histogram After Equalization")
    plt.hist(equalized_img.flatten(), 256, [0, 256], color="r", label='Histogram After Equalization')
    plt.xlim([0, 256])
    plt.title("Histogram After Equalization")
    plt.show()

    # the output path to save the image
    output_path = f"EditedImages/histo_equalization_{img_name}"

    # save the image to the output path
    cv2.imwrite(output_path, equalized_img)

    # return the image and the output path
    return equalized_img, output_path
