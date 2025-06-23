import cv2
import numpy as np


# 图像特效之油漆特效
src = cv2.imread('shanghai.jpg')
gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
kernel = np.array([[-1,-1,-1],[-1,10,-1],[-1,-1,-1]])
dst = cv2.filter2D(gray,-1,kernel)

# 显示图像
cv2.imshow('Source',src)
cv2.imshow('Destination',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()