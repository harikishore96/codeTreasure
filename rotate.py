import cv2,glob,os
from scipy import ndimage
path = "/home/kishore/Documents/OfficeStuff/magic_pin_bills/"
for img in glob.glob(path+'*.jpg'):
	imageName = os.path.basename(img)
	#print imageName
	img = cv2.imread(img)
	height, width, channel = img.shape
	#print height, width, channel
	if width > height:
		rotated = ndimage.rotate(img, -90)
		cv2.imshow('Image',rotated)
		#cv2.waitKey(0)
		cv2.imwrite(path+'rotated/'+imageName,rotated)
	#break