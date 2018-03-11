import numpy as np
import cv2

ref_image_name = 'pika-proportions.png'
image_name = 'drawing-proportions.png'
ref_img = cv2.imread(ref_image_name)
raw_img = cv2.imread(image_name)
# cv2.imshow(ref_image_name)
vis = np.concatenate((ref_img, raw_img), axis=1)
cv2.imwrite('porportions.jpg',vis)
