import cv2
import numpy as np
from variabile import width, height

def liniute(inFrame,tupla):
    yS=np.polynomial.polynomial.polyfit(tupla[0],tupla[1],deg=1)
    yD=np.polynomial.polynomial.polyfit(tupla[2],tupla[3],deg=1)

    left_top_y = 0
    left_top_x = (0-yS[0])/yS[1]

    left_bottom_y = height
    left_bottom_x = (height -yS[0])/yS[1]

    right_top_y = 0
    right_top_x = (0-yD[0])/yD[1]

    right_bottom_y = height
    right_bottom_x = (height -yD[0])/yD[1]

    left_top = (int (left_top_x),int (left_top_y))
    right_top = (int(right_top_x), int(right_top_y))
    left_bottom = (int(left_bottom_x), int(left_bottom_y))
    right_bottom = (int(right_bottom_x), int(right_bottom_y))

    cv2.line(inFrame,left_top,left_bottom,(100,0,0),5)
    cv2.line(inFrame, right_top, right_bottom, (200, 0, 0), 5)
    puncte = (left_top, right_top, left_bottom, right_bottom)
    return inFrame, puncte
