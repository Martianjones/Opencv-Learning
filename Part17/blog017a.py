import cv2
import numpy as np

# 图像的顶帽处理
# 用原始图像减去图像开运算后的结果，常用于解决由于光照不均匀图像分割出错的问题
src = cv2.imread('blocks.png',cv2.IMREAD_UNCHANGED)
kernel = np.ones((10,10),np.uint8)
result = cv2.morphologyEx(src,cv2.MORPH_TOPHAT,kernel)

cv2.imshow('Source',src)
cv2.imshow('Result',result)
cv2.waitKey(0)
cv2.destroyAllWindows()
