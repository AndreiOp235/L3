import cv2
import numpy as np
from variabile import width, height, formaTrapez, contur

def topDown(inFrame):
    conturtp = np.float32(contur)
    formaTrapeztp = np.float32(formaTrapez)

    tp_bounds = cv2.getPerspectiveTransform(formaTrapeztp, conturtp)
    tp = cv2.warpPerspective(inFrame, tp_bounds, (width, height))
    return tp