import cv2
import numpy as np

# Opencv绘制直线

# 创建黑色图像
img1 = np.zeros((256,256,3),np.uint8)
img2 = np.zeros((256,256,3),np.uint8)
# 绘制直线
cv2.line(img1,(0,0),(255,255),(55,255,155),5)

# 绘制矩形
cv2.rectangle(img2,(20,20),(150,250),(255,0,0),2)

# 显示图像
cv2.imshow('Demo1',img1)
cv2.imshow('Demo2',img2)

# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()


