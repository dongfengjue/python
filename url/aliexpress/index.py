import urllib
def down1(url):
    return  urllib.urlopen(url).read()#读取全部网页
url = "https://www.baidu.com"
print (down1(url))