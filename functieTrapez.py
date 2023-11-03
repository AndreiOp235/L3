import cv2
import numpy as np
from variabile import width, height, formaTrapez

def functieTrapez(inFrame):
    trapez = np.zeros((height, width), dtype=np.uint8)
    trapez = cv2.fillConvexPoly(trapez, formaTrapez, 1)
    return trapez