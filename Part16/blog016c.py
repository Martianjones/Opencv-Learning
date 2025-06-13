import cv2
import numpy as np

# 图像梯度运算
# 其本质是膨胀运算后的图像减去腐蚀运算后的图像
# 梯度运算可用于获得图像的轮廓

src = cv2.imread('whiteblock.png',cv2.IMREAD_UNCHANGED)
kernel = np.ones((10,10),np.uint8)
result = cv2.morphologyEx(src,cv2.MORPH_GRADIENT,kernel)

cv2.imshow('Source',src)
cv2.imshow('Result',result)
cv2.waitKey(0)
cv2.destroyAllWindows()

