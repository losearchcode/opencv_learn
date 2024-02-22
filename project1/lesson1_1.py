import cv2  #opencv读取格式是BGR格式
import matplotlib.pyplot as plt
import numpy

#cv2.IMREAD_COLOR:彩色   彩色通道：RGB    范围：0～255  
#cv2.IMREAD_GRAYSCALE:灰度  一个通道  

img_rgb=cv2.imread('/home/cat/Desktop/opencv/opencv/picture/car.jpg',cv2.IMREAD_COLOR)
#img_rgb=cv2.imread('/home/cat/Desktop/opencv/picture/car.jpg')
#[[[h,w,c]通道]] BGR格式

img_gray=cv2.imread('/home/cat/Desktop/opencv/opencv/picture/car.jpg',cv2.IMREAD_GRAYSCALE)


#print(img_rgb)
#print(img_rgb.shape)
print(img_gray)
print(img_gray.shape)

def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)#任意键跳出
    cv2.destroyAllWindows()#销毁窗口

cv_show("image",img_rgb)
cv_show("image1",img_gray)

#保存
cv2.imwrite('/home/cat/Desktop/opencv/opencv/picture/mycar.png',img_rgb)

print(type(img_gray))#底层格式

print(img_gray.size)#像素点

print(img_gray.dtype)#数据类型


