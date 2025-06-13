import cv2
import numpy as np

# 图像开运算
# 其本质是先进行腐蚀运算，在进行膨胀运算

src = cv2.imread('blocks.png',cv2.IMREAD_UNCHANGED)

# 设置卷积核
kernel = np.ones((5,5),np.uint8)

# 图像开运算
result_func = cv2.morphologyEx(src,cv2.MORPH_OPEN,kernel)
result = cv2.erode(src,kernel)
result = cv2.dilate(result,kernel)

# 显示图像
cv2.imshow('src',src)
cv2.imshow('result',result)
cv2.imshow('result_func',result_func)
cv2.waitKey(0)
cv2.destroyAllWindows()


