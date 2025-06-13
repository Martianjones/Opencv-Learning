import cv2
import numpy as np

# 图像闭运算
# 其本质是先膨胀，后腐蚀

src = cv2.imread('whiteblock.png',cv2.IMREAD_UNCHANGED)
kernel = np.ones((10,10),np.uint8)
result = cv2.morphologyEx(src,cv2.MORPH_CLOSE,kernel)

cv2.imshow('Source',src)
cv2.imshow('Result',result)
cv2.waitKey(0)
cv2.destroyAllWindows()