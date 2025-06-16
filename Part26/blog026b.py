import cv2
import numpy as np
import matplotlib.pyplot as plt
from sympy.vector import Laplacian

# Laplacian算子
'''
1、判断图像中心像素灰度值与它周围其他像素值的灰度值
2、如果中心像素的灰度更高，则提升中心像素的灰度
3、反之降低中心像素的灰度，从而实现图像锐化操作
'''

img = cv2.imread('cat.jpg')
cat_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# 灰度化处理图像
grayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Laplacian算子
dst = cv2.Laplacian(grayImage,cv2.CV_16S,ksize = 3)
Laplacian = cv2.convertScaleAbs(dst)

# 用来正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei']

# 显示图形
titles = ['原始图像','Laplacian算子']
images = [cat_img,dst]
for i in range(2):
    plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i]),plt.xticks([]),plt.yticks([])
plt.show()