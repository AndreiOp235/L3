import cv2
import numpy as np
from variabile import width, height, formaTrapez, contur

def finalFrame (puncte):
    output= np.zeros((height, width, 3), dtype=np.uint8)
    cv2.line(output, puncte[0], puncte[2], (255, 0, 0), 5)
    cv2.line(output, puncte[1], puncte[3], (0, 255, 0), 5)

    conturtp = np.float32(contur)
    formaTrapeztp = np.float32(formaTrapez)

    tp_bounds = cv2.getPerspectiveTransform(conturtp, formaTrapeztp)
    output = cv2.warpPerspective(output, tp_bounds, (width, height))

    return output

