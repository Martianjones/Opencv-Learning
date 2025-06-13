import cv2
import numpy as np

# 图像形态学之腐蚀处理

src = cv2.imread('roughlines.jpg',cv2.IMREAD_UNCHANGED)

# 设置卷积核
kernel = np.ones((5,5),np.uint8)

# 图像腐蚀处理
erosion = cv2.erode(src,kernel)

# 显示图像
cv2.imshow('src',src)
cv2.imshow('result',erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()
