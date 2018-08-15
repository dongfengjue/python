import urllib
import http.client 

test_data = {'ServiceCode':'aaaa','b':'bbbbb'}
test_data_urlencode = urllib.parse.urlencode(test_data)

requrl = "http://127.0.0.1:8765/api/common/sendSms/logRecord"
headerdata = {"Host":"127.0.0.1"}

conn = http.client.HTTPConnection("127.0.0.1:8765")

conn.request(method="POST",url=requrl,body=test_data_urlencode,headers = headerdata) 

response = conn.getresponse()

res= response.read()

print (res)