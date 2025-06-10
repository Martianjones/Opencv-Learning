import cv2
import numpy as np

src = cv2.imread('minecraft.jpg')
rows,cols = src.shape[:2]

result1 = cv2.resize(src,(200,100))
result2 = cv2.resize(src,(int(cols*0.6),int(rows*1.2)))
result3 = cv2.resize(src,None,fx=0.3,fy=0.3)


cv2.imshow('Original',src)
cv2.imshow('Resize',result1)
cv2.imshow('result',result2)
cv2.imshow('result3',result3)

cv2.waitKey(0)
cv2.destroyAllWindows()