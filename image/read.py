from PIL import Image
import pytesseract

# brew install tesseract
# 如中文需下载chi_sim.traineddata,将下载好的语言包放到/usr/local/Cellar/tesseract/3.05.01/share/tessdata/路径下。
# https://pan.baidu.com/s/1J0HNoVhX8WexS_5r0k2jDw 密码: ywc3 语言包

picPath = '/Users/chenbing/Documents/file/word.jpg'
Image = Image.open(picPath)   # 打开图片
text = pytesseract.image_to_string(Image,lang='chi_sim')  #使用简体中文解析图片
print(text)