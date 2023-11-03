import cv2
import numpy as np
from variabile import width, height, BF

def blureaza(inFrame):
    blurF=cv2.blur(inFrame, ksize=(BF,BF))
    return blurF