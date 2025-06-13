import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('dragonboat.png')

# 获取图像高度
height = img.shape[0]
width = img.shape[1]

# 采样转换成 16 * 16 区域
numHeight = int(height/32)
numWidth = int(width/32)

# 创建一幅图像
newImage = np.zeros((height,width,3),np.uint8)

# 图像循环采样 16*16 区域
for i in range(32):
    # 获取Y坐标
    y = i * numHeight
    for j in range(32):
        # 获取X坐标
        x = j * numWidth
        # 获取填充颜色 左上角像素点
        b = img[y + 16,x + 16][0]
        g = img[y + 16,x + 16][1]
        r = img[y + 16,x + 16][2]

        #循环设置小区域采样
        for n in range(numHeight):
            for m in range(numWidth):
                newImage[y + n, x + m][0] = np.uint8(b)
                newImage[y + n, x + m][1] = np.uint8(g)
                newImage[y + n, x + m][2] = np.uint8(r)

# 显示图像
cv2.imshow('src',img)
cv2.imshow('Sampling',newImage)

# 等待显示
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()