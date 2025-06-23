import cv2
import numpy as np

# 图像毛玻璃特效处理
src = cv2.imread('shanghai.jpg')

# 新建目标图像
dst = np.zeros_like(src)

# 获取图像行和列
rows,cols = src.shape[:2]

# 定义偏移量和随机数
offsets = 5
random_num = 0

# 毛玻璃效果：像素点邻域内随机像素点的颜色替代当前像素点的颜色
for y in range(rows - offsets):
    for x in range(cols - offsets):
        random_num = np.random.randint(0,offsets)
        dst[y,x] = src[y+random_num,x+random_num]

# 显示图像
cv2.imshow('Source',src)
cv2.imshow('Destination',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
