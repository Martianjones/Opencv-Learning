import cv2
from cv2.typing import Scalar

# opencv 图像处理基础知识

# 读取图片
img = cv2.imread('minecraft.jpg')
# 显示图像
cv2.imshow('Demo',img)

# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()

s = Scalar(0,0,255)