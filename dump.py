

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
            image_sample = cv2.imread(sample_path)
            image = cv2.imread(path)

            ret,thresh1 = cv2.threshold(image,170,255,cv2.THRESH_BINARY)
            img = thresh1
            # rows,cols = img.shape # number of rows/cols of image

            denoised = cv2.GaussianBlur(thresh1,(5,5),0)
            edged = cv2.Laplacian(denoised,cv2.CV_64F)

            # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # OpenCV represents images in BGR order; however PIL represents
            # images in RGB order, so we need to swap the channels
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # convert the images to PIL format...
            image = Image.fromarray(image)
            edged = Image.fromarray(edged.astype('uint8'), 'RGB')

            # ...and then to ImageTk format
            image_sample = ImageTk.PhotoImage(image_sample)
            edged = ImageTk.PhotoImage(edged)

            # if the panels are None, initialize them
            if panelA is None or panelB is None:
                # the first panel will store our original image
                panelA = Label(image=image_sample, name='panel_a')
                panelA.image = image_sample
                panelA.pack(side="left", padx=10, pady=10)

                # while the second panel will store the edge map
                panelB = Label(image=edged, name='panel_b')
                panelB.image = edged
                panelB.pack(side="right", padx=10, pady=10)

            # otherwise, update the image panels
            else:
            	# update the pannels
            	panelA.configure(image=image_sample)
            	panelB.configure(image=edged)
            	panelA.image = image_sample
            	panelB.image = edged
