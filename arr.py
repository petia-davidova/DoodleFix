
from Tkinter import *
from PIL import Image
from PIL import ImageTk
import tkFileDialog
import numpy as np
import cv2

ref_pnts_sample = []
ref_pnts_drawing = []

sample_path = "/Users/nikolarankov/Desktop/HACK/pica.png"
# def select_point(event,x,y,flags,param):
#     global mouseX,mouseY
#     global ref_pnts
#     if event == cv2.EVENT_LBUTTONDBLCLK:
#         print "Point selected: ", x, y
#         mouseX,mouseY = x,y
#         ref_pnts.append([x,y])

def filter_img(image):
    ret,thresh1 = cv2.threshold(image,170,255,cv2.THRESH_BINARY)

    img = thresh1
    # rows,cols = img.shape # number of rows/cols of image

    denoised = cv2.GaussianBlur(thresh1,(5,5),0)
    edged = cv2.Laplacian(denoised,cv2.CV_64F)
    return edged

def select_image():
	# grab a reference to the image panels
	global panelA, panelB

	# open a file chooser dialog and allow the user to select an input
	# image
	path = tkFileDialog.askopenfilename()
    # ensure a file path was selected
	if len(path) > 0:
		# load the image from disk, convert it to grayscale, and detect
		# edges in it
		image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        print "path: ", path

        ret,thresh1 = cv2.threshold(image,170,255,cv2.THRESH_BINARY)

        img = thresh1
        # rows,cols = img.shape # number of rows/cols of image

        denoised = cv2.GaussianBlur(thresh1,(5,5),0)
        edged = cv2.Laplacian(denoised,cv2.CV_64F)

        sample_image = cv2.imread(sample_path)
        # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # OpenCV represents images in BGR order; however PIL represents
        # images in RGB order, so we need to swap the channels
        # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # convert the images to PIL format...
        sample_image = Image.fromarray(sample_image)
        edged = Image.fromarray(edged.astype('uint8'))

        # ...and then to ImageTk format
        sample_image = ImageTk.PhotoImage(sample_image)
        edged = ImageTk.PhotoImage(edged)

        # if the panels are None, initialize them
        if panelA is None or panelB is None:
            # the first panel will store our original image
            panelA = Label(image=sample_image, name='panel_a')
            panelA.image = sample_image
            panelA.pack(side="left", padx=10, pady=10)

            # while the second panel will store the edge map
            panelB = Label(image=edged, name='panel_b')
            panelB.image = edged
            panelB.pack(side="right", padx=10, pady=10)

        # otherwise, update the image panels
        else:
        	# update the pannels
        	panelA.configure(image=sample_image)
        	panelB.configure(image=edged)
        	panelA.image = sample_image
        	panelB.image = edged


# initialize the window toolkit along with the two image panels
root = Tk()
panelA = None
panelB = None


def motion(event):
    x, y = event.x, event.y
    print('hh {}, {}'.format(x, y))
    caller = event.widget
    c_id = str(caller)
    if c_id ==  ".panel_a":
        ref_pnts_sample.append([x,y])
    elif c_id == ".panel_b":
        ref_pnts_drawing.append([x,y])

root.bind("<Button-1>", motion)
root.bind("<Motion>", motion)


# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI
btn = Button(root, text="Select an image", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")

# kick off the GUI
root.mainloop()
