import cv2

img = cv2.imread('lena.jpg')
cv2.imshow('demo',img)

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
