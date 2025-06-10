import cv2
import numpy as np

src = cv2.imread('street.jpg')
rows,cols = src.shape[:2]

pos1 = np.float32([[50,50],[200,50],[50,200]])
pos2 = np.float32([[50,50],[200,50],[100,250]])
M = cv2.getAffineTransform(pos1,pos2)

result = cv2.warpAffine(src,M,(cols,rows))

cv2.imshow('original',src)
cv2.imshow('result',result)

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()