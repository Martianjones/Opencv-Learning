import cv2
import numpy as np

img = cv2.imread('minecraft.jpg')
r1 = cv2.pyrUp(img)
r2 = cv2.pyrUp(r1)

cv2.imshow('Original',img)
cv2.imshow('PyrUp1',r1)
cv2.imshow('PyrUp2',r2)
cv2.waitKey(0)
cv2.destroyAllWindows()
