import cv2  #opencv读取格式是BGR格式
import matplotlib.pyplot as plt
import numpy

#cv2.IMREAD_COLOR:彩色   彩色通道：RGB    范围：0～255  
#cv2.IMREAD_GRAYSCALE:灰度  一个通道 
# 
#数值计算
#
img_cat=cv2.imread('/home/cat/Desktop/opencv/picture/cat.jpg',cv2.IMREAD_COLOR)
img_dog=cv2.imread('/home/cat/Desktop/opencv/picture/dog.jpg',cv2.IMREAD_COLOR)

img_cat2 = img_cat + 10
print('cat2->\n',img_cat2[:5,:,0])
print('cat->\n',img_cat[:5,:,0])
#numpy相加   相当于相加之后 %256
print('numpt add->\n',(img_cat2+img_cat)[:5,:,0])
#cv2.add 超界之后默认最大值
print('cv2 add->\n',(cv2.add(img_cat,img_cat2))[:5,:,0])




#图像融合  ,  plt显示出现色差处理



print('cat.shape->',img_cat.shape,'\t','dog shape->',img_dog.shape)
#数据shape不匹配，需要resize调整大小

img_dog_armsize = cv2.resize(img_dog,(300,168))#参数(h,w)，制定大小
#参数(0,0)，fx= ,fy=    放缩比例
img_dog_scalesize =  cv2.resize(img_dog,(0,0),fx= 1.5 ,fy= 3)

print('\ndog_armsize shape->',img_dog_armsize.shape,'\t','dog_scalesize ->',img_dog_scalesize.shape)
def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)#任意键跳出
    cv2.destroyAllWindows()#销毁窗口


#2.1 彩色图像出现色差原因
#使用cv2.imread()读取图像时，默认彩色图像的三通道顺序为B、G、R，这与我们所熟知的RGB中的R通道和B通道正好互换位置了。
#而使用plt.imshow()函数却默认显示图像的通道顺序为R、G、B，导致图像出现色差发蓝。
    
""" img = cv2.imread('dog.jpg')		#读取通道顺序为B、G、R
b,g,r = cv2.split(img)			#分别提取B、G、R通道
img_new1 = cv2.merge([r,g,b])	#重新组合为R、G、B
plt.xticks([]), plt.yticks([]) # 隐藏x和y轴
plt.imshow(img_new1) """

""" img = cv2.imread('dog.jpg')		#读取通道顺序为B、G、R
#img[:,:,0]表示图片的蓝色通道，对一个字符串s进行翻转用的是s[::-1]，同样img[:,:,::-1]就表示BGR通道翻转，变成RGB
img_new2 = img[:, :, ::-1]
plt.xticks([]), plt.yticks([]) # 隐藏x和y轴
plt.imshow(img_new2) """



#2.2 灰度图像出现色差原因
#那么为什么plt.imshow()显示灰度图（只有一个通道）还会出现色差呢？
#上一段讲过，这是因为plt.imshow()函数默认显示三通道图像，把灰度图当作彩色图显示出来了，所以出现了发蓝的现象。

#plt.imshow(img_gray,cmap='gray')


def plt_img(img):
    return img[:, :, ::-1]

#图像融合权重相加  R = 权重1*图1 + 权重2*图2 + b
res = cv2.addWeighted(img_cat,0.4,img_dog_armsize,0.6,0)  #b=0

img_cat_plt = plt_img(img_cat)
img_dog_plt = plt_img(img_dog)
img_res_plt = plt_img(res)


plt.subplot(131),plt.imshow(img_dog_plt),plt.title('DOG')
plt.subplot(132),plt.imshow(img_cat_plt),plt.title('CAT')
plt.subplot(133),plt.imshow(img_res_plt),plt.title('RES')

plt.show()
