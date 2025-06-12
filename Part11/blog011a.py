import cv2
import numpy as np

# 最大值灰度处理方法
# 该方法的灰度值等于彩色图像R、G、B三个分量的最大值
img = cv2.imread('mountain.png')

# 获取图像高度和宽度
height,width = img.shape[:2]

# 创建一幅图像
grayimg = np.zeros((height,width,3),np.uint8)

# 图像最大值灰度处理
for i in range(height):
    for j in range(width):
        # 获取图像R G B最大值
        gray = max(img[i,j][0],img[i,j][1],img[i,j][2])
        # 灰度图像像素赋值
        grayimg[i,j] = np.uint8(gray)

# 显示图像
cv2.imshow('Source',img)
cv2.imshow('Gray',grayimg)

# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
