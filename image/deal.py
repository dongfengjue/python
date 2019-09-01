from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
import os

path = "/Users/chenbing/Documents/file/"
img = Image.open("/Users/chenbing/Documents/file/1.jpg")
print(img.format)		 # 输出图片基本信息
print(img.mode)
print(img.size)
img_resize = img.resize((256,256)) # 调整尺寸
img_resize.save(path+"dogresize.jpg")
img_rotate = img.rotate(45)         # 旋转
img_rotate.save(path+"dogrotate.jpg")
om=img.convert('L')				# 灰度处理
om.save(path+'doggray.jpg')
om = img.filter(ImageFilter.CONTOUR)		# 图片的轮廓
om.save(path+'dogcontour.jpg')
om = ImageEnhance.Contrast(img).enhance(20)		# 对比度为初始的10倍
om.save(path+'dogencontrast.jpg')
#更改图片格式：
 
filelist =["1.jpg",
           "dogcontour.jpg",
           "dogencontrast.jpg",
           "doggray.jpg",
           "dogresize.jpg",
           "dogrotate.jpg",
           ]
for infile in filelist:
  outfile = path + os.path.splitext(infile)[0] + ".png"
  print(outfile)
  if infile != outfile:
    try:
      Image.open(path+infile).save(outfile)
    except IOError:
      print ("cannot convert", infile)