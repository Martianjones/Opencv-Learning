import cv2
import numpy as np

# 图像膨胀处理
src = cv2.imread('lines.png',cv2.IMREAD_UNCHANGED)

# 设置卷积核
kernel = np.ones((5,5),np.uint8)

# 图像膨胀处理
dilation = cv2.dilate(src,kernel)

# 显示图像
cv2.imshow('Source',src)
cv2.imshow('Dilation',dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()