import cv2
import numpy as np
from variabile import width, height, sobel_vertical, sobel_horizontal

def sobel(inFrame):
    vertical=cv2.filter2D(np.float32(inFrame),-1,sobel_vertical)
    horizontal=cv2.filter2D(np.float32(inFrame),-1,sobel_horizontal)

    #cv2.imshow("vertical",cv2.convertScaleAbs(vertical))
    #cv2.imshow("horizontal", cv2.convertScaleAbs(horizontal))

    combinatul=np.sqrt((vertical**2)+(horizontal**2))

    return cv2.convertScaleAbs(combinatul)

