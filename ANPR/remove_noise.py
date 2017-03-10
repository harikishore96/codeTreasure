import cv2,sys
import numpy as np

def add_white_border(image,size=10,no_f_channel=3):
    if no_f_channel==3:
      copy_image=np.ones((image.shape[0]+size,image.shape[1]+size,3),np.uint8)*255
    else:
      copy_image=np.ones((image.shape[0]+size,image.shape[1]+size),np.uint8)*255
    copy_image[size/2:image.shape[0]+size/2,size/2:image.shape[1]+size/2]=image
    return copy_image

def remove_noise(image):
	input  = cv2.imread(image)
	input = add_white_border(input)
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3 , 1))
	dilated = cv2.dilate(~input,kernel,iterations = 3)
	gray = cv2.cvtColor(~dilated, cv2.COLOR_BGR2GRAY)
	_, contours, hierarchy = cv2.findContours(~gray,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	idx=0
	list_tl= []
	list_br=[]
	for idx in range(len(contours)):
	    x,y,w,h=cv2.boundingRect(contours[idx])
	    if 100>w>10 and 150>h>50:
	        list_tl.append((x,y))
	        list_tl.sort()
	        list_br.append((x+w,y+h))
	        list_br.sort()
	a=list_tl[0]
	b=list_br[-1]
	x,y = a[0],a[1]
	w,h = b[0],b[1]
	input = input[y-5:h+5,x-5:w+5]
	input = add_white_border(input)
	return input