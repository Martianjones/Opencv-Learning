import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('guineapig.jpg')
guineapig_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# 灰度化处理图像
grayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 高斯滤波
gaussianBlur = cv2.GaussianBlur(grayImage,(3,3),0)

# 阈值处理
ret,binary = cv2.threshold(gaussianBlur,127,255,cv2.THRESH_BINARY)

# Roberts 算子
kernelx = np.array([[-1,0],[0,1]],dtype=int)
kernely = np.array([[0,-1],[1,0]],dtype=int)
x = cv2.filter2D(binary,cv2.CV_16S,kernelx)
y = cv2.filter2D(binary,cv2.CV_16S,kernely)
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)
Roberts = cv2.addWeighted(absX,0.5,absY,0.5,0)

# Prewitt 算子
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]],dtype=int)
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]],dtype=int)
x = cv2.filter2D(binary,cv2.CV_16S,kernelx)
y = cv2.filter2D(binary,cv2.CV_16S,kernely)
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)
Prewitt = cv2.addWeighted(absX,0.5,absY,0.5,0)

# Sobel 算子
x = cv2.Sobel(binary,cv2.CV_16S,1,0)
y = cv2.Sobel(binary,cv2.CV_16S,0,1)
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)
Sobel = cv2.addWeighted(absX,0.5,absY,0.5,0)

# 拉普拉斯算法
dst = cv2.Laplacian(binary,cv2.CV_16S,ksize = 3)
Laplacian = cv2.convertScaleAbs(dst)

# 效果图
titles =['Source Image','BinaryImage','RobertsImage','PrewittImage','SobelImage','LaplacianImage']
images = [guineapig_img,binary,Roberts,Prewitt,Sobel,Laplacian]
for i in np.arange(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i]),plt.xticks([]),plt.yticks([])
plt.show()