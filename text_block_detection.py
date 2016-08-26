import cv2
import numpy as np
import sys

rgb=cv2.imread(sys.argv[1])
large=rgb.copy()
small = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
morphKernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
grad = cv2.morphologyEx(small, cv2.MORPH_GRADIENT, morphKernel)
bw=cv2.adaptiveThreshold(grad,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,5,7)
morphKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (int(sys.argv[2]), 1))
connected=cv2.morphologyEx(bw,cv2.MORPH_CLOSE, morphKernel)
mask=np.zeros(bw.shape,dtype=np.uint8)
contours, hierarchy = cv2.findContours(connected,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE,(0,0))
idx=0
print len(contours)
#idx=0
for idx in range(len(contours)):
	x,y,w,h=cv2.boundingRect(contours[idx])
	#maskROI=mask[y:y+h,x:x+w]
	#maskROI[:]=0
	cv2.drawContours(mask,contours,idx,(255,255,255),-1)
	r=np.count_nonzero(mask[y:y+h,x:x+w])/(w*h*1.0)
	if r>0.45 and w>10 and h>10:
		if h<w:
			cv2.rectangle(large,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imwrite('aa.jpg',large)