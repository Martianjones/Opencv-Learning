import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
src = cv2.imread('TomJerry.jpg')

# 获取BGR三个通道
b,g,r = cv2.split(src)

# 绘制直方图
plt.figure('炭治郎')
# 蓝色分量
plt.hist(b.ravel(),bins = 256,density = 1,facecolor = 'b',edgecolor = 'b',alpha = 0.75)
# 绿色分量
plt.hist(g.ravel(),bins = 256,density = 1,facecolor = 'g',edgecolor = 'g',alpha = 0.75)
# 红色分量
plt.hist(r.ravel(),bins = 256,density = 1,facecolor = 'r',edgecolor = 'r',alpha = 0.75)
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# 显示原始图像
cv2.imshow('src',src)
cv2.waitKey(0)
cv2.destroyAllWindows()