import cv2  #opencv读取格式是BGR格式
import matplotlib.pyplot as plt
import numpy

#cv2.IMREAD_COLOR:彩色   彩色通道：RGB    范围：0～255  
#cv2.IMREAD_GRAYSCALE:灰度  一个通道 
# 
#读取视频-捕获摄像头
#cv2.VideoCapture

vc = cv2.VideoCapture('/home/cat/Desktop/opencv/picture/1418490767-1-30080.mp4')
#检查
if vc.isOpened():
    open_, frame = vc.read()#open_为判断的bool;frame则为取出的那帧的数据
else:
    open_ = False

while open_:
    ret, frame = vc.read()
    if frame is None:
        break
    if ret == True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('result',gray)
        if cv2.waitKey(1) & 0xFF == 27:
#        if cv2.waitKey(1) & 0xFF == ord('q'):#   q键盘       
            break
vc.release()
cv2.destroyAllWindows()




