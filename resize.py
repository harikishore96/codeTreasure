import cv2
img = cv2.imread('blank_form.jpg')
resized = cv2.resize(img,(1500,1000))
cv2.imwrite('resized.jpg',resized)