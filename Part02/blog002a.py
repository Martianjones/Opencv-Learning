import cv2
import matplotlib.pyplot as plt

# 读入图片并将图片转换到RGB颜色空间
img1 = cv2.imread('lena.jpg')
img1[20:50,50:80] = [255,255,255]   # 改变图像中的一块区域
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)


img2 = cv2.imread('minecraft.jpg')
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

img3 = cv2.imread('puppet.jpg')
img3 = cv2.cvtColor(img3,cv2.COLOR_BGR2RGB)

img4 = cv2.imread('terraria.jpg')
img4 = cv2.cvtColor(img4,cv2.COLOR_BGR2RGB)

# 显示四张图像
titles = ['lena','minecraft','puppet','terraria']
images = [img1,img2,img3,img4]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

# 显示图像，遇到ESC退出窗口
# k = cv2.waitKey(0)
# if k == 27:
#     cv2.destroyAllWindows()
