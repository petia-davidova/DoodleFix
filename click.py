import numpy as np
import cv2


ref_pnts_sample = []
ref_pnts_drawing = []

def select_point(event,x,y,flags,param):
    global mouseX,mouseY
    global ref_pnts
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print "Point selected: ", x, y
        mouseX,mouseY = x,y
        cv2.circle(img2,(x,y),5,(100,100,100),-1)
        ref_pnts_sample.append([x,y])
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        print "Point selected: ", x, y
        mouseX,mouseY = x,y
        cv2.circle(img,(x,y),5,(100,100,100),-1)
        ref_pnts_drawing.append([x,y])
###################################################
ref_image_name = 'pika.png'
image_name = 'drawing-2.jpg'
ref_img = cv2.imread(ref_image_name,cv2.IMREAD_GRAYSCALE)
raw_img = cv2.imread(image_name,cv2.IMREAD_GRAYSCALE)


# resized_img = cv2.resize(raw_img,(0,0), fx=0.1, fy=0.1)
ret,thresh1 = cv2.threshold(raw_img,170,255,cv2.THRESH_BINARY)

img = thresh1
# rows,cols = img.shape # number of rows/cols of image

denoised = cv2.GaussianBlur(thresh1,(5,5),0)
filtered = cv2.Laplacian(denoised,cv2.CV_64F)
cv2.imwrite('edged.jpg', filtered)
###################################################

# img = np.zeros((512,512,3), np.uint8)
img=filtered
cv2.namedWindow('image')
cv2.setMouseCallback('image',select_point)
# cv2.resizeWindow('image', 600,600)

img2=ref_img
cv2.namedWindow('ref_image')
cv2.setMouseCallback('ref_image',select_point)

vis = np.concatenate((img2, img), axis=1)
cv2.imwrite('vis.jpg',vis)
while(1):
    cv2.imshow('image', img)
    cv2.imshow('ref_image',ref_img)

    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break
    elif k == ord('a'):
        print mouseX,mouseY
        print ref_pnts_sample
        print ref_pnts_drawing
        print "Bye.."
