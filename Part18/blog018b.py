import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


# 读取图片变为灰度图
src = cv2.imread('tanjilo.jpg')
src = cv2.cvtColor(src,cv2.COLOR_BGR2RGB)
# 计算256灰度级的图像直方图
histb = cv2.calcHist([src],[0],None,[256],[0,255])
histg = cv2.calcHist([src],[1],None,[256],[0,255])
histr = cv2.calcHist([src],[2],None,[256],[0,255])

# 设置字体
matplotlib.rcParams['font.sans-serif']=['SimHei']

# 显示原始图像和绘制的直方图
plt.subplot(121)
plt.imshow(src,'gray')
plt.axis('off')
plt.title('(a)炭治郎彩色图像')
plt.subplot(122)
plt.plot(histb,color = 'b')
plt.plot(histg,color = 'g')
plt.plot(histr,color = 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('(b)直方图曲线')
plt.show()