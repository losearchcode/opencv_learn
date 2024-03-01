import cv2  #opencv读取格式是BGR格式
import matplotlib.pyplot as plt
import numpy

#cv2.IMREAD_COLOR:彩色   彩色通道：RGB    范围：0～255  
#cv2.IMREAD_GRAYSCALE:灰度  一个通道 
# 
#边界填充
#
img_rgb=cv2.imread('/home/cat/Desktop/opencv/picture/car.jpg',cv2.IMREAD_COLOR)

top_size,bottom_size,left_size,right_size = (50,50,50,50)

#原始图像
replicate = cv2.copyMakeBorder(img_rgb,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_REPLICATE)
#
reflect = cv2.copyMakeBorder(img_rgb,top_size,bottom_size,left_size,right_size,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img_rgb,top_size,bottom_size,left_size,right_size,cv2.BORDER_REFLECT_101)
warp = cv2.copyMakeBorder(img_rgb,top_size,bottom_size,left_size,right_size,cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img_rgb,top_size,bottom_size,left_size,right_size,cv2.BORDER_CONSTANT,value=0)


#BORDER REPLICATE:复制法，也就是复制最边缘像素。
#BORDER REFLECT:反射法，对感兴趣的图像中的像素在两边进行复制例如：  fedcba|abcdefgh|hgfedcb
#BORDER_REFLECT_101:反射法，也就是以最边缘像素为轴，对称，  gfedcb|abcdefgh|gfedcba
#BORDER WRAP:外包装法   abcdefgh|abcdefgh|abcdefg
#BORDER CONSTANT:常量法，常数值填充。

plt.subplot(231),plt.imshow(img_rgb,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(warp,'gray'),plt.title('WARP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()


