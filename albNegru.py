import cv2
import numpy as np
from variabile import width, height

def albNegru(resized):
    gray = np.zeros((height, width), dtype=np.uint8)

    return cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    #
    # for i in range(height):
    #      for j in range(width):
    #         gray[i][j] = sum(resized[i][j]) / 3
    #
    # return gray