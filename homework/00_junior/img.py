# ^_^ coding: utf-8
# 1、导入Image类
from PIL import Image

# 2、使用Image的对象读取图片
image_name = 'logo.png'
img = Image.open(image_name)
print(img.size)
print(img.mode)
# 3、将图片转换为灰度图像
bak = img.convert('L')
