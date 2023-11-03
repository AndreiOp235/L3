import cv2
import numpy as np
from variabile import width, height, formaTrapez
from resize import resize
from albNegru import albNegru
from functieTrapez import functieTrapez
from topDown import topDown
from blur import blureaza
from sobel import sobel
from threshold import nivel
from strazile import strazi
from linii import liniute
from finalFrame import finalFrame

cam = cv2.VideoCapture('lane.mp4')

while True:
    ret, frame = cam.read()

    if ret is False:
        break

    # 2 resize
    resizedFrame= resize(frame)
    cv2.imshow('Small', resizedFrame)

    # 3 grayscale
    gray = albNegru(resizedFrame)
    cv2.imshow('Gray', gray)

    # 4 trapez
    trapez = functieTrapez(gray)
    cv2.imshow("Trapez contur",trapez*255)
    cv2.imshow("Trapez sosea", trapez * gray)

    # 5 Top-Down
    # tp = np.zeros((height, width), dtype=np.uint8) 
    tp=topDown(trapez*gray)
    cv2.imshow("Top-Down", tp)

    # 6 Blur
    blurF=blureaza(tp)
    cv2.imshow("Blur", blurF)

    # 7 sobel filter
    sobelat= sobel(blurF)
    cv2.imshow("Sobel", sobelat)

    # 8 threshold
    nivelat= nivel(sobelat)
    cv2.imshow("Binarized",nivelat)

    # 9 strazi
    (coordonate, puncte)=strazi(nivelat)
    cv2.imshow("coordonate",coordonate)

    # 10 linii
    (lines, puncteLinii)=liniute(coordonate, puncte)
    cv2.imshow("Lines", lines)

    # 11 final
    finalf = finalFrame(puncteLinii)
    merged=cv2.addWeighted(resizedFrame, 1, finalf, 1, 0)
    cv2.imshow("Final", merged)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()


