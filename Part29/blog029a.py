import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib

# 傅里叶变换与逆变换

img = cv2.imread('twilight.jpg',0)

# 傅里叶变换
dft = cv2.dft(np.float32(img),flags=cv2.DFT_COMPLEX_OUTPUT)

# 将频谱低频从左上角移动至中心位置
dft_shift = np.fft.fftshift(dft)

# 频谱图像双通道复数转换为0-255区间
result = 20 * np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

# 傅里叶逆变换
ishift = np.fft.ifftshift(dft_shift)
iimg = cv2.idft(ishift)
reverse = cv2.magnitude(iimg[:,:,0],iimg[:,:,1])


# 设置字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']

# 显示图像
plt.subplot(131),plt.imshow(img,cmap='gray')
plt.title('(a)原始图像'),plt.xticks([]),plt.yticks([]),plt.axis('off')
plt.subplot(132),plt.imshow(result,cmap='gray')
plt.title('(b)傅里叶变换处理'),plt.xticks([]),plt.yticks([]),plt.axis('off')
plt.subplot(133),plt.imshow(reverse,cmap='gray')
plt.title('(c)傅里叶逆变换处理'),plt.xticks([]),plt.yticks([]),plt.axis('off')
plt.show()