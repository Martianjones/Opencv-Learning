import cv2
import numpy as np
from torchvision.transforms.v2.functional import grayscale_to_rgb_image

# 读取图片
img = cv2.imread('street.jpg')
# img = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

# 获取图像高度和宽度
# cv2.imshow('Gray',img)    # 判断是否已经为灰度图
height = img.shape[0]
width = img.shape[1]

# 创建一幅图像
newImage = np.zeros((height,width,3),np.uint8)

# 图像量化操作，量化等级为2
for i in range(height):
    for j in range(width):
        for k in range(3):
            if img[i,j][k] < 128:
                gray = 0
            else:
                gray = 128
            newImage[i,j][k] = np.uint8(gray)

# 显示图像
cv2.imshow('Source',img)
cv2.imshow('Quantify',newImage)

# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
以下代码实现了读入BGR图片将其转化为灰度图片
再将灰度图片实现量化的过程
需注意的是灰度图是单通道的而BGR图片是3通道的
在处理数据时需要注意通道数量是否正确'''
# # 读取图片
# src = cv2.imread('street.jpg')
# img = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

# # 获取图像高度和宽度
# # cv2.imshow('Gray',img)    # 判断是否已经为灰度图
# height = img.shape[0]
# width = img.shape[1]
#
# # 创建一幅图像
# newImage = np.zeros((height,width),np.uint8)
#
# # 图像量化操作，量化等级为2
# for i in range(height):
#     for j in range(width):
#         # for k in range(3):
#             if img[i,j] < 128:
#                 gray = 0
#             else:
#                 gray = 128
#             newImage[i,j] = np.uint8(gray)
#
# # 显示图像
# cv2.imshow('Source',src)
# cv2.imshow('Quantify',newImage)
#
# # 等待显示
# cv2.waitKey(0)
# cv2.destroyAllWindows()