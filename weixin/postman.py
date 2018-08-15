# coding=utf-8
import urllib
import urllib.request

#url地址
url="http://127.0.0.1:8765/api/common/sendSms/logRecord"
#参数
values={
        'ie':'UTF-8',
        'wd':'test'   
        }
#进行参数封装
data=urllib.parse.urlencode(values)
#组装完整url
#req=urllib2.Request(url,data)
url=url+'?'+data

#访问完整url
#response = urllib2.urlopen(req)
response = urllib.request.urlopen(url)
html=response.read()

print (html)