# PIL：Python Imaging Library，已经是Python平台事实上的图像处理标准库了。PIL功能非常强大，但API却非常简单易用。
# 由于PIL仅支持到Python 2.7，加上年久失修，于是一群志愿者在PIL的基础上创建了兼容的版本，名字叫Pillow，支持最新Python 3.x，又加入了许多新特性，因此，我们可以直接安装使用Pillow。


# 操作图像
# 来看看最常见的图像缩放操作，只需三四行代码
# from PIL import Image
# im=Image.open('2.png')#打开一个图片文件
# w,h=im.size
# print('图片的大小格式是     %sx%s' %(w,h))
# # im.thumbnail(w//2,h//2)
# # print('Resize image to: %sx%s' % (w//2, h//2))
# # 把缩放后的图像用jpg格式保存:

#
# 其他功能如切片、旋转、滤镜、输出文字、调色板等一应俱全。
#
# 比如，模糊效果也只需几行代码：
# from PIL import Image,ImageFilter
# im=Image.open('2.png')
# # 应用模糊滤镜:
# im2=im.filter(ImageFilter.BLUR)
# im2.save('blur1.png')


# PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。比如要生成字母验证码图片：

from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
# 随机字母:
def suijishu():
    return chr(random.randint(65,90))#随机去到65到90之间的整数，然后转换成字符串
# 生成随机颜色，用来填充背景
def suijicolor1():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
# 生成随机颜色2，用来填充文本
def suijicolor2():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
#自定义新建图片的宽和高
width=60*4
heght=60
image=Image.new('RGB',(width,heght),(255,255,255))## 新建RGB类的图片，默认为白色
# 新建字体对象
#ImageFont.truetype(file,size) 这个函数从指定的文件加载了一个字体对象，并且为指定大小的字体创建了字体对象。
font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)
#ImageDraw模块提供了图像对象的简单2D绘制。用户可以使用这个模块创建新的图像，注释或润饰已存在图像，为web应用实时产生各种图形。
# 新建draw对象
draw=ImageDraw.Draw(image)#在这个图片上写东西
# 填充每个像素:   循环内嵌套循环  xy一起跟着循环
for x in range(width):
    for y in range(heght):
        draw.point((x,y),fill=suijicolor1())#在这个图片上填充颜色  调用上面的函数
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), suijishu(), font=font, fill=suijicolor2())
# 模糊:
#在图像处理中，经常需要对图像进行平滑、锐化、边界增强等滤波处理。在使用PIL图像处理库时，我们通过Image类中的成员函数filter()来调用滤波函数对图像进行滤波，而滤波函数则通过ImageFilter类来定义的。
image1=image.filter(ImageFilter.BLUR)
image1.save('code.jpg','jpeg')
image.show('code.jpg')
