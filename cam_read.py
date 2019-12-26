# coding: utf-8
import base64
import numpy as np
import cv2
import json
from PIL import Image
from io import BytesIO


def frame2base64(frame):
    img = Image.fromarray(frame) #将每一帧转为Image
    output_buffer = BytesIO() #创建一个BytesIO
    img.save(output_buffer, format='JPEG') #写入output_buffer
    byte_data = output_buffer.getvalue() #在内存中读取
    base64_data = base64.b64encode(byte_data) #转为BASE64
    return base64_data #转码成功 返回base64编码

#调用笔记本内置摄像头，所以参数为0，如果有其他的摄像头可以调整参数为1，2
cap=cv2.VideoCapture(0)
while True:
 sucess, frame = cap.read()
 frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
 ##############################################################################
 img_b64encode = frame2base64(frame)
 post_dict = {"image": img_b64encode, "type": 0}

 pic_str = post_dict['image']
 img_b64decode = base64.b64decode(pic_str)
 nparr = np.frombuffer(img_b64decode, np.uint8)
 img_o = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

 ##############################################################################

 cv2.imshow("img", img_o)
 #保持画面的持续。
 k=cv2.waitKey(1)
 if k == 27:
  #通过esc键退出摄像
  cv2.destroyAllWindows()
  break
#  elif k==ord("s"):
#   #通过s键保存图片，并退出。
#   cv2.imwrite("image2.jpg", img_o)
#   cv2.destroyAllWindows()
#   break

cap.release()