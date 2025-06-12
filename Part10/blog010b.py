import cv2
import numpy as np
import  matplotlib.pyplot as plt

img = cv2.imread('dragonboat.png')
r1 = cv2.pyrDown(img)
r2 = cv2.pyrDown(r1)

cv2.imshow('Original',img)
cv2.imshow('PyrDown1',r1)
cv2.imshow('PyrDown2',r2)

cv2.waitKey(0)
cv2.destroyAllWindows()