from PIL import Image
import pytesseract

picPath = '/Users/chenbing/Documents/file/word.jpg'
Image = Image.open(picPath)   # 打开图片
text = pytesseract.image_to_string(Image,lang='chi_sim')  #使用简体中文解析图片
print(text)