# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# import math
#
# # 自动色彩均衡算法(Automatic Color Enhancement,ACE)
# # 原作者为zmshy2128
# # 线性拉伸处理
# # 去掉最大最小 0.5% 的像素值 线性拉伸至[0,1]
# def stretchImage(data,s = 0.005,bins = 2000):
#     ht = np.histogram(data,bins)
#     d = np.cumsum(ht[0])/float(data.size)
#     Imin = 0;Imax = bins - 1
#     while Imin < bins:
#         if d[Imin] >= s:
#             break
#         Imin+=1
#     while Imax >= 0:
#         if d[Imax]<=1-s:
#             break
#         Imax -= 1
#     return  np.clip((data-ht[1][Imin])/(ht[1][Imax]-ht[1][Imin]),0,1)
#
# # 根据半径计算权重参数矩阵
# g_para = {}
# def getPara(radius = 5):
#     global g_para
#     m = g_para.get(radius,None)
#     if m is not None:
#         return m
#     size = radius*2 + 1
#     m = np.zeros((size,size))
#     for h in range(-radius,radius+1):
#         for w in range(-radius,radius+1):
#             if h==0 and w==0:
#                 continue
#             m[radius+h,radius+w] = 1.0/math.sqrt(h**2+w**2)
#     m /= m.sum()
#     g_para[radius] = m
#     return m
#
# # 常规的ACE实现
# def zmlce(I,ratio = 4,radius = 300):
#     para = getPara(radius)
#     height,width = I.shape
#
#     zh =[]
#     zw =[]
#     n=0
#     while n<radius:
#         zh.append(0)
#         zw.append(0)
#         n+=1
#     for n in range(height):
#         zh.append(n)
#     for n in range(width):
#         zw.append(n)
#     n = 0
#     while n<radius:
#         zh.append(height - 1)
#         zw.append(width - 1)
#         n += 1
#
#     Z = I[np.ix_(zh,zw)]
#     res = np.zeros(I.shape)
#     for h in range(radius*2+1):
#         for w in range(radius*2+1):
#             if para[h][w] == 0:
#                 continue
#             res += (para[h][w] * np.clip((I-Z[h:h+height,w:w+width])*ratio,-1,1))
#     return res
#
# # 单通道ACE快速增强实现
# def zmlceFast(I,ratio,radius):
#     print(I)
#     height,width = I.shape[:2]
#     if min(height,width) <= 2:
#         return np.zeros(I.shape)+0.5
#     Rs = cv2.resize(I,(int((width+1)/2),int((height+1)/2)))
#     Rf = zmlce(Rs,ratio,radius)
#     Rf = cv2.resize(Rf,(width,height))
#     Rs = cv2.resize(Rs,(width,height))
#
#     return Rf + zmlce(I,ratio,radius) - zmlce(Rs,ratio,radius)
#
# def zmlceColor(I,ratio = 4,radius = 3):
#     res = np.zeros(I.shape)
#     for k in range(3):
#         res[:,:,k] = stretchImage(zmlceFast(I[:,:,k],ratio,radius))
#         return res
#
# # 主函数
# if __name__ == '__main__':
#     img = cv2.imread('smog.jpg')
#     res = zmlceColor(img/255.0)*255
#     cv2.imwrite('Ice.jpg',res)


# ChatGPT 实现ACE
import cv2
import numpy as np

def ace_channel(channel, radius=3):
    h, w = channel.shape
    result = np.zeros_like(channel, dtype=np.float32)

    for y in range(h):
        for x in range(w):
            acc = 0.0
            weight_sum = 0.0
            center_val = float(channel[y, x])

            for j in range(max(0, y - radius), min(h, y + radius + 1)):
                for i in range(max(0, x - radius), min(w, x + radius + 1)):
                    if i == x and j == y:
                        continue

                    neighbor_val = float(channel[j, i])
                    diff = neighbor_val - center_val
                    dist = np.sqrt((x - i) ** 2 + (y - j) ** 2)
                    if dist == 0:
                        continue
                    weight = 1.0 / dist
                    acc += weight * np.clip(diff, -1, 1)
                    weight_sum += weight

            if weight_sum != 0:
                result[y, x] = center_val + acc / weight_sum
            else:
                result[y, x] = center_val

    # Normalize to 0-255
    result = cv2.normalize(result, None, 0, 255, cv2.NORM_MINMAX)
    return result.astype(np.uint8)

def ace_color_equalization(img, radius=3):
    b, g, r = cv2.split(img)
    b_eq = ace_channel(b, radius)
    g_eq = ace_channel(g, radius)
    r_eq = ace_channel(r, radius)
    return cv2.merge([b_eq, g_eq, r_eq])

# 示例
img = cv2.imread('smog.jpg')
enhanced_img = ace_color_equalization(img, radius=3)

cv2.imshow('Original', img)
cv2.imshow('ACE Enhanced', enhanced_img)
cv2.waitKey(0)
cv2.destroyAllWindows()