import cv2
import numpy as np
from variabile import width, height

def strazi(inFrame):
    copie=inFrame.copy()
    copie[0:(int(height*0.05)),0:width]=0
    copie[(int(height * 0.95)):height, 0:width] = 0
    copie[0:height,0:(int(width*0.05))]=0
    copie[0:height, (int(width * 0.65)):width] = 0

    stg =copie[0:height,0:(int (width/3))]
    dr  =copie[0:height, (int(width / 3)):width]

    coordS=np.argwhere(stg>1)
    coordD=np.argwhere(dr>1)
    coordD[:,1]=coordD[:,1]+width/3

    left_xs=coordS[:,1]
    left_ys = coordS[:, 0]

    right_xs = coordD[:, 1]
    right_ys = coordD[:, 0]

    puncte= (left_xs, left_ys, right_xs, right_ys)

    return copie, puncte