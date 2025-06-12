import cv2
import numpy as np
import matplotlib.pyplot as plt



# 图像灰度伽马变换
# 绘制曲线
def gamma_plot(c,v):
    x = np.arange(0,256,0.01)
    y = c*x**v
    plt.plot(x,y,'r',linewidth = 1)
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.title('伽马变换函数')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim([0,255]),plt.ylim([0,255])
    plt.show()

# 伽马变换
def gamma(img,c,v):
    lut = np.zeros(256,dtype = np.float32)
    for i in range(256):
        lut[i] = c*i**v
    output_img = cv2.LUT(img,lut)
    output_img = np.uint8(output_img + 0.5)
    return output_img

img = cv2.imread('nightstreetscene.png')

# 绘制伽马变换曲线
gamma_plot(0.00000005,4.0)
# 图像灰度伽马变换
output = gamma(img,0.00000005,4.0)

# 显示图像
cv2.imshow('Imput',img)
cv2.imshow('Output',output)
cv2.waitKey(0)
cv2.destroyAllWindows()