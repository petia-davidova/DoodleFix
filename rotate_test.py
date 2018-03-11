import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img_orig = cv.imread('pika1.jpg',0)
img=cv.resize(img_orig,(0,0),fx=0.1,fy=0.1)

#constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)
(h,w)=img.shape
# Rotation
M=cv.getRotationMatrix2D((100,200),45,1.5)
rotated=cv.warpAffine(img,M,(w,h))
# Blurring
blur = cv.GaussianBlur(rotated,(5,5),0)
ret3,th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

cv.imshow('rotated',rotated)
cv.waitKey(0)
