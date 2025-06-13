import cv2
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# 读取图片变为灰度图
src = cv2.imread('tanjilo.jpg')
img = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

# 计算256灰度级的图像直方图
hist = cv2.calcHist([img],[0],None,[256],[0,255])

# 设置字体
matplotlib.rcParams['font.sans-serif']=['SimHei']

# 显示原始图像和绘制的直方图
plt.subplot(121)
plt.imshow(img,'gray')
plt.axis('off')
plt.title('(a)灰度图像')

plt.subplot(122)
plt.plot(hist,color = 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('(b)直方图曲线')
plt.show()