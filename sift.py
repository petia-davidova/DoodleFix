
import numpy as np
import cv2
from matplotlib import pyplot as plt

# img = cv2.imread('pica.png',0)
#
# # Initiate STAR detector
# orb = cv2.ORB_create()
# # find the keypoints with ORB
# kp = orb.detect(img,None)
#
# # compute the descriptors with ORB
# kp, des = orb.compute(img, kp)
#
# # draw only keypoints location,not size and orientation
# img2 = cv2.drawKeypoints(img,kp,None, color=(0,255,0), flags=0)
# plt.imshow(img2),plt.show()





img1 = cv2.imread('pika.png',0)          # queryImage
img2 = cv2.imread('pika copy.png',cv2.IMREAD_GRAYSCALE) # trainImage

blur = cv2.GaussianBlur(img2,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
img2 = th3
# Initiate SIFT detector
orb = cv2.ORB_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)
# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

# Match descriptors.
matches = bf.match(des1,des2)

# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)

# Draw first 10 matches.
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:200], None, flags=2)

plt.imshow(img3),plt.show()
