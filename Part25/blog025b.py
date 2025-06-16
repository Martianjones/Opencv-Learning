import cv2
import numpy as np
import matplotlib.pyplot as plt


# Prewitt算子
'''
1、通过numpy定义模板，在调用Opencv的filter2D函数实现对图像的卷积运算
2、通过convertScaleAbs函数计算绝对值，并将图像转为8位图进行显示
3、调用addWeighted函数实现边缘提取
'''

img = cv2.imread('papers.jpg')
papers_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# 灰度化处理
grayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Prewitt算子
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]],dtype=int)
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]],dtype=int)
x = cv2.filter2D(grayImage,cv2.CV_16S,kernelx)
y = cv2.filter2D(grayImage,cv2.CV_16S,kernely)

# 转 uint8
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)
Prewitt = cv2.addWeighted(absX,0.5,absY,0.5,0)

# 用来正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei']

# 显示图像
titles = ['原始图像','Prewitt算子']
images = [papers_img,Prewitt]
for i in range(2):
    plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i]),plt.xticks([]),plt.yticks([])
plt.show()