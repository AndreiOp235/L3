import cv2
import numpy as np
from variabile import width, height

def nivel(inFrame):
    level = np.zeros((height, width), dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            level[i][j] = 1 if inFrame[i][j] < 90 else 255

    return level