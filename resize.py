import cv2
import numpy as np
from variabile import width, height

def resize(inFrame):
    resized = cv2.resize(inFrame, (width, height))
    return resized
