import cv2  #opencv读取格式是BGR格式
import matplotlib.pyplot as plt
import numpy

#cv2.IMREAD_COLOR:彩色   彩色通道：RGB    范围：0～255  
#cv2.IMREAD_GRAYSCALE:灰度  一个通道 
# 
#截取部分图像数据
#

img_rgb=cv2.imread('/home/cat/Desktop/opencv/picture/car.jpg',cv2.IMREAD_COLOR)

car = img_rgb[100:400,100:400]

def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)#任意键跳出
    cv2.destroyAllWindows()#销毁窗口

cv_show('car',car)

#颜色通道
b,g,r = cv2.split(img_rgb)#分离通道
print('r.shape->\n',r.shape)

img_merge = cv2.merge((b,g,r))
print("img_merge.shape->\n",img_merge.shape)

#只保留R
r_img = img_rgb.copy()
r_img[:,:,0] = 0 #B
r_img[:,:,1] = 0 #G
cv_show('r_img',r_img)
#只保留G
g_img = img_rgb.copy()
g_img[:,:,0] = 0 #B
g_img[:,:,2] = 0 #R
cv_show('g_img',g_img)
#只保留B
b_img = img_rgb.copy()
b_img[:,:,1] = 0 #G
b_img[:,:,2] = 0 #R
cv_show('b_img',b_img)


