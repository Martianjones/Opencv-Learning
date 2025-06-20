import cv2
import numpy as np
import matplotlib.pyplot as plt

# 灰度增强直方图对比
# 灰度减弱直方图对比
# 灰度反色直方图对比
# 读取图像

img = cv2.imread('mhw.jpg')
grayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

height,width = grayImage.shape[:2]
result = np.zeros((height,width),np.uint8)

# 图像灰度上移变换      图像减弱直方图只需要将条件改为灰度值*80       图像反色直方图只需255-灰度值
for i in range(height):
    for j in range(width):
        if(int(grayImage[i,j]+50)>255):
            gray = 255
        else:
            gray = int(grayImage[i,j]+50)
        result[i,j] = np.uint8(gray)

# 计算原图的直方图
hist = cv2.calcHist([img],[0],None,[256],[0,255])

# 计算灰度变换的直方图
hist_res = cv2.calcHist([result],[0],None,[256],[0,255])

# 原始图像
plt.figure(figsize = (8,6))
plt.subplot(221),plt.imshow(img,'gray'),plt.title('(a)'),plt.axis('off')

# 绘制掩膜
plt.subplot(222),plt.plot(hist),plt.title('(b)'),plt.xlabel('x'),plt.ylabel('y')

# 绘制掩膜设置后的图像
plt.subplot(223),plt.imshow(result,'gray'),plt.title('(c)'),plt.axis('off')

# 绘制直方图
plt.subplot(224),plt.plot(hist_res),plt.title('(d)'),plt.xlabel('(x)'),plt.ylabel('(y)')
plt.show()