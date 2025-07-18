import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import  LinearLocator,FormatStrFormatter

img = cv.imread('dog.jpg')
img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
imgd = np.array(img)    # image类转numpy

# 准备数据
sp = img.shape
h = int(sp[0])  # 图像高度（rows）
w = int(sp[1])  # 图像宽度（colums） of image

# 绘图初始处理
fig = plt.figure(figsize = (16,12))
ax = fig.add_subplot(projection = "3d") #gca不可用

x = np.arange(0,w,1)
y = np.arange(0,h,1)
x,y = np.meshgrid(x,y)
z = imgd
surf = ax.plot_surface(x,y,z,cmap = cm.coolwarm)

# 自定义Z轴
ax.set_zlim(-10,255)
ax.zaxis.set_major_locator(LinearLocator(10))   # 设置Z轴网格线的疏密

# 将Z的value字符串转为float 并保留2位小数
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# 设置坐标轴的label 和 标题
ax.set_xlabel('x',size=15)
ax.set_ylabel('y',size=15)
ax.set_zlabel('z',size=15)
ax.set_title('surface plot',weight = 'bold',size = 20)

# 添加右侧的色卡条
fig.colorbar(surf,shrink=0.6,aspect=8)
plt.show()