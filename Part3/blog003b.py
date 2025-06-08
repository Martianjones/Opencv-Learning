import cv2
import numpy as np

# 创建黑色图像
img1 = np.zeros((256,256,3),np.uint8)
img2 = np.zeros((256,256,3),np.uint8)

# 绘制圆形
cv2.circle(img1,(100,100),50,(255,255,0),4) # 若将粗细设置为-1，则绘制的圆形为实心圆
cv2.ellipse(img2,(120,100),(100,50),20,0,360,(255,0,255),2)

# 显示图像
cv2.imshow('circle',img1)
cv2.imshow('ellipse',img2)

# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()