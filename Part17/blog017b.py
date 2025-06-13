import cv2
import numpy as np

# 图像的底帽运算
# 用图像闭运算操作减去原始图像后的结果，从而获取图像内部的小孔或前景色中的黑点
src = cv2.imread('whiteblock.png',cv2.IMREAD_UNCHANGED)
kernel = np.ones((10,10),np.uint8)
result = cv2.morphologyEx(src,cv2.MORPH_BLACKHAT,kernel)

cv2.imshow('src',src)
cv2.imshow('result',result)
cv2.waitKey(0)
cv2.destroyAllWindows()