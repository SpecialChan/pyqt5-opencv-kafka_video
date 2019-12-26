#!/usr/bin/env python
# coding: utf-8
import base64
import numpy as np
import cv2
import json
from PIL import Image
from io import BytesIO
from kafka import KafkaConsumer


consumer = KafkaConsumer('test_frame01', bootstrap_servers=['192.168.1.103:9092'])
# consumer = KafkaConsumer('test_frame01', bootstrap_servers=['10.108.4.119:9092'])
faceCascade = cv2.CascadeClassifier(r'D:\Programs\Python\Python38\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
# eyeCascade = cv2.CascadeClassifier(r'D:\Programs\Python\Python38\Lib\site-packages\cv2\data\haarcascade_eye.xml')

kk = 0

for msg in consumer:
 kfk_text = json.loads(msg.value)
 # print(kfk_text['type'])
 pic_str = kfk_text['image']
 img_b64decode = base64.b64decode(pic_str)
 nparr = np.frombuffer(img_b64decode, np.uint8)
 img_o = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
 # print (pic_str)
 # # ##############################################################################
 #

 gray = cv2.cvtColor(img_o, cv2.COLOR_BGR2GRAY)
 faces = faceCascade.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5, minSize = (32, 32) )

 for (x, y, w, h) in faces:
  fac_gray = gray[y: (y + h), x: (x + w)]
  result = []
  # eyes = eyeCascade.detectMultiScale(fac_gray, 1.3, 2)
  # for (ex, ey, ew, eh) in eyes:
  #  result.append((x + ex, y + ey, ew, eh))
 # 画矩形

 for (x, y, w, h) in faces:
  cv2.rectangle(img_o, (x, y), (x + w, y + h), (0, 255, 0), 2)
 # for (ex, ey, ew, eh) in result:
 #   cv2.rectangle(img_o, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

 cv2.imshow("小猪快跑--实时计算平台", img_o)
 #保持画面的持续。
 k=cv2.waitKey(1)
 if k == 27:
  #通过esc键退出摄像
  cv2.destroyAllWindows()
  break

consumer.close()
