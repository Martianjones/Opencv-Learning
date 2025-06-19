import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# 高通滤波器

img = cv.imread('lena.jpg',0)

# 傅里叶变换
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

# 设置高通滤波器
rows,cols = img.shape
crow,ccol = int(rows/2),int(cols/2)
fshift[crow-30:crow+30,crow-30:ccol+30] = 0

# 傅里叶变换
ishift = np.fft.ifftshift(fshift)
iimg = np.fft.ifft2(ishift)
iimg = np.abs(iimg)

# 设置字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']

# 显示原始图像和高通滤波处理图像
plt.subplot(121),plt.imshow(img,'gray'),plt.title('(a)原始图像'),plt.axis('off')
plt.subplot(122),plt.imshow(iimg,'gray'),plt.title('(b)结果图像'),plt.axis('off')
plt.show()