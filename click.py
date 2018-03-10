import numpy as np
import cv2


ref_pnts = []

def select_point(event,x,y,flags,param):
    global mouseX,mouseY
    global ref_pnts
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print "Point selected: ", x, y
        mouseX,mouseY = x,y
        ref_pnts.append([x,y])

###################################################
ref_image_name = 'pica.png'
image_name = 'drawing1-small.jpg'
ref_img = cv2.imread(ref_image_name,cv2.IMREAD_GRAYSCALE)
raw_img = cv2.imread(image_name,cv2.IMREAD_GRAYSCALE)


# resized_img = cv2.resize(raw_img,(0,0), fx=0.1, fy=0.1)
ret,thresh1 = cv2.threshold(raw_img,170,255,cv2.THRESH_BINARY)

img = thresh1
# rows,cols = img.shape # number of rows/cols of image

denoised = cv2.GaussianBlur(thresh1,(5,5),0)
filtered = cv2.Laplacian(denoised,cv2.CV_64F)

###################################################

# img = np.zeros((512,512,3), np.uint8)
img=filtered
cv2.namedWindow('image')
cv2.setMouseCallback('image',select_point)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break
    elif k == ord('a'):
        print mouseX,mouseY
        print "Bye.."
