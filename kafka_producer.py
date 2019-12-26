#!/usr/bin/env python
# coding: utf-8
import base64
import numpy as np
import cv2
import json
from PIL import Image
from io import BytesIO
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='192.168.1.103:9092')
# producer = KafkaProducer(bootstrap_servers='10.108.4.119:9092')
def frame2base64(frame):
    img = Image.fromarray(frame) #将每一帧转为Image
    output_buffer = BytesIO() #创建一个BytesIO
    img.save(output_buffer, format='JPEG') #写入output_buffer
    byte_data = output_buffer.getvalue() #在内存中读取
    base64_data = base64.b64encode(byte_data) #转为BASE64
    return base64_data

cap=cv2.VideoCapture(0)

while True:
 sucess, frame = cap.read()
 frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
 ##############################################################################
 img_b64encode = frame2base64(frame)
 img_b64encode_string = img_b64encode.decode('utf-8')
 post_dict = {"image": img_b64encode_string, "type": 0}
 # send_str = str(post_dict, encoding='utf-8')
 msg = json.dumps(post_dict).encode()

 producer.send('test_frame01', msg)

producer.close()
cap.release()
