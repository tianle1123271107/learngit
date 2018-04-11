# Pillow中最重要的类就是Image，该类存在于同名的模块中。可以通过以下几种方式实例化：从文件中读取图片，处理其他图片得到，或者直接创建一个图片。
# 使用Image模块中的open函数打开一张图片：
# from PIL import Image
# from PIL import ImageColor
# im=Image.open("2.png")
# print(im)#返回一个image的实例对象
# print(im.format,im.size,im.mode)#PPM (512, 512) RGB
# print(im.getcolors())
# im.show()#当有一个Image对象时，可以用Image类的各个方法进行处理和操作图像，例如显示图片：
# format属性定义了图像的格式，如果图像不是从文件打开的，那么该属性值为None；size属性是一个tuple，表示图像的宽和高（单位为像素）
# ；mode属性为表示图像的模式，常用的模式为：L为灰度图，RGB为真彩色，CMYK为pre-press图像。

# Pillow库支持相当多的图片格式。直接使用Image模块中的open()函数读取图片，而不必先处理图片的格式，Pillow库自动根据文件决定格式。

# 在图像处理中，经常需要对图像进行平滑、锐化、边界增强等滤波处理。在使用PIL图像处理库时，我们通过Image类中的成员函数filter()来调用滤波函数对图像进行滤波，而滤波函数则通过ImageFilter类来定义的。
# from PIL import Image
# from PIL import ImageFilter
#
# im=Image.open("timg.jpg")
# # 预定义的图像增强滤波器
# # im_BURL=im.filter(ImageFilter.BLUR)
# # im_BURL.show()
# # im_CONTOUR=im.filter(ImageFilter.CONTOUR)
# # im_CONTOUR.show()
# im_SMOOTH=im.filter(ImageFilter.EMBOSS)
# im_SMOOTH.show()
# GaussianBlur(radius=2)


# ImageFilter类中预定义了如下滤波方法：
# • BLUR：模糊滤波
#
# • CONTOUR：轮廓滤波
#
# • DETAIL：细节滤波
#
# • EDGE_ENHANCE：边界增强滤波
#
# • EDGE_ENHANCE_MORE：边界增强滤波（程度更深）
#
# • EMBOSS：浮雕滤波
#
# • FIND_EDGES：寻找边界滤波
#
# • SMOOTH：平滑滤波
#
# • SMOOTH_MORE：平滑滤波（程度更深）
#
# • SHARPEN：锐化滤波
#
# • GaussianBlur(radius=2)：高斯模糊


'''计算机通常将图像表示为RGB值，或者再加上alpha值（通透度，透明度），称为RGBA值。在Pillow中，RGBA的值表示为由4个整数组成的元组，分别是R、G、B、A。整数的范围0~255。'''
'''RGB全0就可以表示黑色，全255代表白色。可以猜测(255, 0, 0, 255)代表红色，因为R分量最大，G、B分量为0，所以呈现出来是红色。但是当alpha值为0时，无论是什么颜色，该颜色都不可见，可以理解为透明。'''

# from PIL import ImageColor
# print(ImageColor.getcolor('red','RGBA'))
# # 也可以只以RBG的方式查看
# print(ImageColor.getcolor('black','RGB'))


# 图像的坐标表示
# 图像中左上角是坐标原点(0, 0)，这和平常数学里的坐标系不太一样。这样定义的坐标系意味着，X轴是从左到右增长的，而Y轴是从上到下增长
# 新建图像
# Pillow也可以新建空白图像, 第一个参数是mode即颜色空间模式，第二个参数指定了图像的分辨率(宽x高)，第三个参数是颜色。
# 可以直接填入常用颜色的名称。如'red'
# 也可以填入十六进制表示的颜色，如#FF0000表示红色。
# 还能传入元组，比如(255, 0, 0, 255)或者(255， 0， 0)表示红色。
# from PIL import Image
# newIm= Image.new('RGB', (100, 100), 'red')
# newIm.save(r'F:\1.png')
# # 也可以用RGBA模式，还有其他模式查文档吧
# newIm1= Image.new('RGBA', (100, 100), (255,0,0,0))#在RGBA模式下，也可只传入前三个值，A值默认255
# newIm1.save(r'F:\4.png')
# # 在RGB模式下，第四个参数失效，默认255，在RGBA模式下，也可只传入前三个值，A值默认255
# blcakIm = Image.new('RGB',(200, 100), (255, 255, 0, 120))
# blcakIm.save(r'F:\5.png')
# blcakIm1 = Image.new('RGB',(200, 100), (255, 255, 0, 0))#在RGB模式下，第四个参数失效
# blcakIm1.save(r'F:\6.png')


''' 裁剪图像 '''

# Image有个crop()方法接收一个矩形区域元组(上面有提到)。返回一个新的Image对象，是裁剪后的图像，对原图没有影响。
# from PIL import Image
# im=Image.open("timg.jpg")
# caijian=im.crop((700, 400, 1200, 1000))#左，上 ，右，底
# caijian.save(r'F:\8.png')
# 图像的坐标表示
# 图像中左上角是坐标原点(0, 0)，这和平常数学里的坐标系不太一样。这样定义的坐标系意味着，X轴是从左到右增长的，而Y轴是从上到下增长。
# 在Pillow中如何使用上述定义的坐标系表示一块矩形区域？许多函数或方法要求提供一个矩形元组参数。元组参数包含四个值，分别代表矩形四条边的距离X轴或者Y轴的距离。
# 顺序是(左，顶，右，底)。右和底坐标稍微特殊，表示直到但不包括。可以理解为[左, 右)和[顶， 底)这样左闭右开的区间。比如(3, 2, 8, 9)就表示了横坐标范围[3, 9]；纵坐标范围[2, 8]的矩形区域。

#
''' 复制与粘贴图像到另一个图像'''

# Image的copy函数如其名会产生一个原图像的副本，在这个副本上的任何操作不会影响到原图像。paste()方法用于将一个图像粘贴（覆盖）在另一个图像上面。谁调用它，他就在该Image对象上直接作修改。
from PIL import Image
# im = Image.open("timg1.jpg")
# cropedIm = im.crop((500, 500,800,800))
# im.paste(cropedIm, (155, 155))#(im)谁调用它，他就在该Image对象上直接作修改。
# im.show()
# im.save(r'C:\Users\Administrator\Desktop\paste.png')


# 这如果之后还会用到原图的信息，由于信息被改变就很麻烦。所以paste前最好使用copy()复制一个副本，在此副本操作，
# 不会影响到原图信息。虽然在程序里原图信息已改变，但由于保存文件时用的其他文件名，相当于改变没有生效，所以查看的时候原图还是没有改变的。
# im = Image.open("timg2.jpg")#获得一个图对象
# cropedIm = im.crop((700,500,1000,1000))#按照比例剪切 得到一个新的图片对象
# copyIm = im.copy()#复制原图像  得到一个新的复制的图片对象
# copyIm.save(r'F:\100.jpg')#保存复制的图片对象
# copyIm.paste(cropedIm, (50,50))#将剪切的图片对象黏贴到复制的对象
# im.show()#展示结果


'''证件照'''
# from PIL import Image
# im = Image.open("2012081210372.jpg")
# cropedIm = im.crop((400, 400, 500, 500))
# # cropedIm.show()
# crop_width, crop_height = cropedIm.size
# print(cropedIm.size)
# width,height=im.size
# print(im.size)
# copyim=im.copy()
# for left in range(0,width,crop_width):
#     for top in range(0,height,crop_height):
#         cropedIm.paste(cropedIm, (left, top))
# copyim.save(r'F:\99.png')


'''调整图像的大小'''
# # resize方法返回指定宽高度的新Image对象，接受一个含有宽高的元组作为参数。宽高的值得是整数
# from PIL import Image
# im = Image.open("2012081210372.jpg")
# width, height = im.size
# print(im.size)
# resizeim=im.resize((600,300))
# resizeim.show()


'''旋转和翻转图像'''
# rotate()返回旋转后的新Image对象, 保持原图像不变。逆时针旋转
from PIL import Image
# im = Image.open("2012081210372.jpg")
# im.rotate(90).save(r'F:\90.jpg')
# im.rotate(180).save(r'F:\180.jpg')
# im.rotate(270).save(r'F:\270.jpg')
# im.rotate(20).save(r'F:\20.jpg')
# im.rotate(20,expand=True).save(r'F:\21.jpg')
# 由上到下，分别是旋转了90°，180°， 270°、普通的20°，加了参数expand=True旋转的20°。expand放大了图像尺寸（变成了2174x1672），
# 使得边角的图像不被裁剪（四个角刚好贴着图像边缘）。再看旋转90°、270°时候图像被裁剪了，但是如下查看图像的宽高，确是和原图一样，搞不懂。
im90=Image.open(r'F:\90.jpg')
im270=Image.open(r'F:\270.jpg')
print(im90.size,im270.size)#和原图的大小一样  所以说裁剪没用

'''图像的镜面翻转。transpose()函数可以实现，必须传入Image.FLIP_LEFT_RIGHT或者Image.FLIP_TOP_BOTTOM，第一个是水平翻转，第二个是垂直翻转。'''
# im = Image.open(r'F:\21.jpg')
# im.transpose(Image.FLIP_LEFT_RIGHT).save(r'F:\540.jpg')
# im.transpose(Image.FLIP_TOP_BOTTOM).save(r'F:\550.jpg')

im = Image.open("timg5.jpg")
print(im.size)#(1920, 1080)
cropim=im.crop((800,300,1500,1500))
cropim.show()