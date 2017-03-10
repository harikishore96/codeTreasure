import os,sys,glob,dlib,cv2
from skimage import io
cord_pts=[]
detector = dlib.fhog_object_detector("anpr_detector.svm")
img = io.imread(sys.argv[1])
dets = detector(img)
for k, d in enumerate(dets):
    cord_pts.append(d.left())
    cord_pts.append(d.top())
    cord_pts.append(d.right())
    cord_pts.append(d.bottom())
print cord_pts
anpr_part = img[cord_pts[1]:cord_pts[3],max(0,cord_pts[0]):min(cord_pts[2],cord_pts[2])]
cv2.imwrite("anpr3.jpg",anpr_part)