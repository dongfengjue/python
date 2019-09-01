import requests
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
f = open('/Users/chenbing/Documents/file/url.txt', 'r')
url = f.readlines()
length = len(url)
url_result_success=[]
url_result_failed=[]
for i in range(0,length):
    try:
        response = requests.get(url[i].strip(), verify=False, allow_redirects=True, timeout=5)
        if response.status_code != 200:
            raise requests.RequestException(u"Status code error: {}".format(response.status_code))
    except requests.RequestException as e:
        url_result_failed.append(url[i])
        continue
    url_result_success.append(url[i])
f.close()
result_len1 = len(url_result_failed)
result_len2= len(url_result_success)
for i in range(0,result_len1):
    print (url_result_failed[i].strip()+"打开失败")
print("   ")
for j in range(0,result_len2):
	print (url_result_success[j].strip()+"打开成功")