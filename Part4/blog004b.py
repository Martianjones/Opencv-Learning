import cv2
import numpy as np

# 读取图片
img = cv2.imread('minecraft.jpg',cv2.IMREAD_GRAYSCALE)

# 获取图像宽和高
rows,cols = img.shape[:2]
# print(rows,cols)

# 画圆形
circle = np.zeros((rows,cols),dtype='uint8')
cv2.circle(circle,(int(rows/2),int(cols/4)),50,255,-1)

# Opencv 运算
result1 = cv2.bitwise_and(img,circle)
result2 = cv2.bitwise_or(img,circle)
result3 = cv2.bitwise_not(img)
result4 = cv2.bitwise_xor(img,circle)

# 显示图像
cv2.imshow('original',img)
cv2.imshow('circle',circle)
cv2.imshow('and result',result1)
cv2.imshow('or result',result2)
cv2.imshow('not result',result3)
cv2.imshow('xor result',result4)


# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
