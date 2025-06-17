import cv2
import numpy as np
import matplotlib.pyplot as plt


# 基于边缘检测的图像分割
img = cv2.imread('forest.jpg')
forest_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
grayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 高斯滤波
gaussianBlur = cv2.GaussianBlur(grayImage,(3,3),0)

# 阈值处理
ret,binary = cv2.threshold(gaussianBlur,127,255,cv2.THRESH_BINARY)

# Reberts算子
kernelx = np.array([[-1,0],[0,1]],dtype=int)
kernely = np.array([[0,-1],[1,0]],dtype=int)
x = cv2.filter2D(binary,cv2.CV_16S,kernelx)
y = cv2.filter2D(binary,cv2.CV_16S,kernely)
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)
Roberts = cv2.addWeighted(absX,0.5,absY,0.5,0)

# Prewitt算子
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,11]],dtype=int)
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]],dtype=int)
x = cv2.filter2D(binary,cv2.CV_16S,kernelx)
y = cv2.filter2D(binary,cv2.CV_16S,kernely)
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)
Prewitt = cv2.addWeighted(absX,0.5,absY,0.5,0)

# Sobel算子
x = cv2.Sobel(binary,cv2.CV_16S,1,0)
y = cv2.Sobel(binary,cv2.CV_16S,0,1)
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)
Sobel = cv2.addWeighted(absX,0.5,absY,0.5,0)

# 拉普拉斯算法
dst = cv2.Laplacian(binary,cv2.CV_16S,ksize=3)
Laplacian = cv2.convertScaleAbs(dst)

# Scharr算子
x = cv2.Scharr(gaussianBlur,cv2.CV_32F,1,0) #X方向
y = cv2.Scharr(gaussianBlur,cv2.CV_32F,0,1) #Y方向
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)
Scharr = cv2.addWeighted(absX,0.5,absY,0.5,0)

# Canny算子
Canny = cv2.Canny(gaussianBlur,50,150)

# 先通过高斯滤波降噪
gaussian = cv2.GaussianBlur(grayImage,(3,3),0)

#在通过拉普拉斯算子做边缘检测
dst = cv2.Laplacian(gaussian,cv2.CV_16S,ksize = 3)
LOG = cv2.convertScaleAbs(dst)

# 效果图
titles = ['SourceImage','BinaryImage','RobertsImage','PrewittImage','SobelImage','LaplacianImage','ScharrImage','CannyImage','LOGImage']
images = [forest_img,binary,Roberts,Prewitt,Sobel,Laplacian,Scharr,Canny,LOG]
for i in range(9):
    plt.subplot(3,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i]),plt.xticks([]),plt.yticks([])
plt.show()