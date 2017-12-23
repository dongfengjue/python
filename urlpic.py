import re
import urllib.request
import sys
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

#从url里找到png的url
def getImg(html):
    reg = r'src="(.+?\.png)"'
    imgre = re.compile(reg)
    html = html.decode('utf-8')
    imglist = re.findall(imgre,html)
    return imglist      
   
html = getHtml("https://p.baidu.com/daily/view?id=106845")


for index , item in enumerate(getImg(html)) :
        print(item)
        urllib.request.urlretrieve(item,__file__+"\\..\\temp\\"+str(index)+".png")
    
       



