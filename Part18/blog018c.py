import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
src = cv2.imread('tanjilo.jpg')
src = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

# 绘制直方图
plt.hist(src.ravel(),256)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# 显示原始图像
cv2.imshow('src',src)
cv2.waitKey(0)
cv2.destroyAllWindows()