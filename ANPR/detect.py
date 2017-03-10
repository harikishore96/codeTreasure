import os,sys,glob,dlib,cv2
from skimage import io
import numpy as np
from remove_noise import remove_noise

def detect(filepath):
	cord_pts=[]
	detector = dlib.fhog_object_detector("anpr_detector.svm")
	img = cv2.imread(filepath)
	dets = detector(img)
	for k, d in enumerate(dets):
		cord_pts.append(d.left())
		cord_pts.append(d.top())
		cord_pts.append(d.right())
		cord_pts.append(d.bottom())
	anpr_part = img[cord_pts[1]:cord_pts[3],max(0,cord_pts[0]):min(cord_pts[2],cord_pts[2])]
	cv2.imwrite("static/localized.jpg",anpr_part)
	os.system('ocropus-nlbin -n static/localized.jpg')
	denoised = remove_noise('static/localized.bin.png')
	cv2.imwrite("static/denoised.jpg",denoised)
	os.system('ocropus-rpred -m anpr_model.pyrnn.gz -n static/denoised.jpg')
	with open('static/denoised.txt') as file:
		data = file.read()
	font = cv2.FONT_HERSHEY_SIMPLEX
	data = data.strip('\n')
	cv2.putText(img,str(data),(10,50), font, 2,(0,0,255),4,cv2.LINE_AA)
	cv2.imwrite("static/output.jpg",img)