import cv2
import numpy as np

# 读取图片
img = cv2.imread('minecraft.jpg')

# 创建空图像
emptyImage = np.zeros(img.shape,np.uint8)

# 复制图像
copyImage = img.copy()

# 显示图像
cv2.imshow('image',img)
cv2.imshow('emptyImage',emptyImage)
cv2.imshow('copyImage',copyImage)
# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()