import  numpy as np
width = 320
height = 180

ss = (int(0.46 * width), int(0.74 * height))
sj = (0, height)
ds = (int(0.58 * width), int(0.74 * height))
dj = (width, height)

formaTrapez = np.array([ss, sj, dj, ds], dtype=np.int32)
contur = np.array([(0, 0), (0, height), (width, height), (width, 0)], dtype=np.int32)
#ordinea aici si la H/W

BF=3 #kernel blurare

sobel_vertical = np.float32([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
sobel_horizontal = np.transpose(sobel_vertical)
