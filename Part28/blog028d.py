import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# 基于纹理背景的图像分割

img = cv2.imread('people.jpg')
grayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 设置掩码、fgbModel、bgModel
mask = np.zeros(img.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgbModel = np.zeros((1,65),np.float64)

# 矩形坐标,坐标不能全部为0
rect = (20,20,150,200)

# 图像分割
cv2.grabCut(img,mask,rect,bgdModel,fgbModel,5,cv2.GC_INIT_WITH_RECT)

# 设置新掩码：0和2做背景
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')

# 设置字体
matplotlib.rcParams['font.sans-serif']=['SimHei']

# 显示原图
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.subplot(1,2,1)
plt.imshow(img)
plt.title('(a)原始图像')
plt.xticks([]),plt.yticks([])

# 使用蒙版来获取前经区域
img = img*mask2[:,:,np.newaxis]
plt.subplot(1,2,2)
plt.imshow(img)
plt.title('(b)目标图像')

plt.colorbar()
plt.xticks([]),plt.yticks([])
plt.show()