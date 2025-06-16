import cv2
import numpy as np
import matplotlib.pyplot as plt

# Roberts算子步骤
'''
1、主要通过Numpy定义模板，再使用Opencv的filter2D函数实现边缘提取
2、在进行Roberts算子处理之后，还需要调用convertScaleAbs函数计算绝对值，并将图像转换为8位图进行显示
3、调用addWeighted函数计算水平方向和垂直方向的Roberts算子
'''

img = cv2.imread('papers.jpg')
papers_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# 灰度化处理图像
grayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Roberts算子
kernelx = np.array([[-1,0],[0,1]],dtype=int)
kernely = np.array([[0,-1],[1,0]],dtype=int)
x = cv2.filter2D(grayImage,cv2.CV_16S,kernelx)
y = cv2.filter2D(grayImage,cv2.CV_16S,kernely)

# 转 uint8
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)
Roberts = cv2.addWeighted(absX,0.5,absY,0.5,0)

cv2.imshow('Source',papers_img)
cv2.imshow('Roberts',Roberts)
cv2.waitKey(0)
cv2.destroyAllWindows()