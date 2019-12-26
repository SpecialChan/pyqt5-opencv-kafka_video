import base64

image = 'cat.jpg'
print(type(image))
def imageToByte(image):
    with open(image, 'rb') as f:
        ssk=f.read()
        print(type(ssk))
        image_byte = base64.b64encode(ssk)
        print(type(image_byte))
    #     print('123')
    # image_str=image_byte.decode('ascii') #byte类型转换为str
    # print(type(image_str))
    return image_byte
image1 = imageToByte(image)
print(type(image1))

data = {
  "engineeringdata": {
    "date": 12,
    "value": "59.3;98.5",
    "image": image1
  }
}


def byteToImage(str, filename):
    # image_str = str.encode('ascii')
    image_byte = base64.b64decode(str)
    image_json = open(filename, 'wb')
    image_json.write(image_byte)  # 将图片存到当前文件的fileimage文件中
    image_json.close()


file_address = "./" + r"34.jpg"
byteToImage(data['engineeringdata']['image'], file_address)


