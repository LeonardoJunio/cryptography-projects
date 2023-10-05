# from PIL import Image
# import numpy as np
import cv2


class ImageHelper:

    def readImage(fileNameImage):
        return cv2.imread(fileNameImage)

    def writeImage(fileNameImage, image):
        return cv2.imwrite(fileNameImage, image)
