import cv2
import numpy as np
from matplotlib import pyplot as plt

def get_point():
    return 1


ref_image_name = 'pica.png'
image_name = 'drawing1.jpg'
ref_img = cv2.imread(ref_image_name,cv2.IMREAD_GRAYSCALE)
raw_img = cv2.imread(image_name,cv2.IMREAD_GRAYSCALE)
ref_width, ref_height = ref_img.shape
# resized_img = cv2.resize(raw_img,(ref_width,ref_height))
resized_img = cv2.resize(raw_img,(0,0), fx=0.1, fy=0.1)
ret,thresh1 = cv2.threshold(resized_img,170,255,cv2.THRESH_BINARYINV)

img = thresh1
rows,cols = img.shape # number of rows/cols of image

denoised = cv2.GaussianBlur(thresh1,(5,5),0)
filter = cv2.Laplacian(denoised,cv2.CV_64F)

# cv2.imshow('Original',raw_img)

cv2.imshow('Reference', ref_img)
cv2.imshow('Laplacian Filter',filter)

# plt.subplot(121),plt.imshow(ref_img)
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(filter)
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

# cv2.namedWindow('image',cv2.WINDOW_NORMAL)  # Can be resized
# cv2.resizeWindow('image', self.w, self.h)   #Reasonable size window
# cv2.setMouseCallback('image',self.mouse_callback) #Mouse callback
# while(not self.finished):
#   cv2.imshow('image',self.img)
#   k = cv2.waitKey(4) & 0xFF
#   if k == 27:
#      breakim
# cv2.destroyAllWindows()
#
#
# # mouse callback function
# def mouse_callback(self,event,x,y,flags,param):
#   if event == cv2.EVENT_LBUTTONDOWN:
#      print x, y


plt.show()
cv2.namedWindow("image")

cv2.waitKey(0)
