import cv2
import numpy as np
import matplotlib.pyplot as plt

# 图像模糊特效
img = cv2.imread('shanghai.jpg')
source = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 高斯滤波
result = cv2.GaussianBlur(source,(11,11),0)

# 显示图形
plt.rcParams['font.sans-serif']=['SimHei']
titles = ['原始图像','高斯滤波']
images = [source,result]
for i in range(2):
    plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i]),plt.xticks([]),plt.yticks([])
plt.show()