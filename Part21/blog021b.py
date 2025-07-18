import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('scenery.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# 彩色图像均衡化，需要分解通道，对每一个通道均衡化
(b,g,r) = cv2.split(img)
bH = cv2.equalizeHist(b)
gH = cv2.equalizeHist(g)
rH = cv2.equalizeHist(r)

# 合并每一个通道
result = cv2.merge((bH,gH,rH))
cv2.imshow('Input',img)
cv2.imshow('Result',result)

# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()

# 绘制直方图
plt.figure('Hist')
# 各色分量
plt.hist(bH.ravel(),bins=256,density = True,facecolor = 'b',edgecolor = 'b')
plt.hist(gH.ravel(),bins=256,density = True,facecolor = 'g',edgecolor = 'g')
plt.hist(rH.ravel(),bins=256,density = True,facecolor = 'r',edgecolor = 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()