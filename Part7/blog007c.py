import cv2
import numpy as np

src = cv2.imread('street.jpg')
rows,cols=src.shape[:2]

pos1 = np.float32([[114,82],[287,156],[8,322],[216,333]])
pos2 = np.float32([[0,0],[188,0],[0,262],[188,262]])
M = cv2.getPerspectiveTransform(pos1,pos2)

# 图像透视变换
result = cv2.warpPerspective(src,M,(190,272))

# 显示图像
cv2.imshow('original',src)
cv2.imshow('result',result)

# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
