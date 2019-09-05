from selenium import webdriver
import time


f = open('D:/file/config.txt','r')

lines = f.readlines()

print(lines[0])

url = lines[0]
username = lines[1]
password = lines[2]
childurl = lines[3]

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
browser = webdriver.Chrome(executable_path="D:/file/chromedriver.exe",chrome_options=options)
browser.maximize_window()
browser.get(url)
time.sleep(3)
login_name = browser.find_element_by_id('username')

# login_name.click()
# login_name.clear()
login_name.send_keys(username)

time.sleep(0.5)
login_password = browser.find_element_by_id('password')
# login_password.click()
# login_password.clear()
login_password.send_keys(password) 

time.sleep(0.5)
captcha = browser.find_element_by_id('captcha')
# captcha.click()
# captcha.clear()
captcha.send_keys("1234") 

time.sleep(0.5)
login_button = browser.find_element_by_tag_name ('button')
login_button.click()

time.sleep(5)
myIframe = browser.find_element_by_id('myIframe')

myjs = "document.getElementById('myIframe').src='"+childurl+"'"
browser.execute_script(myjs)


