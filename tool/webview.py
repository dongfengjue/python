from selenium import webdriver
import os

# https://npm.taobao.org/mirrors/chromedriver/  阿里镜像
chromedriver = "/Users/chenbing/Documents/file/chromedriver" 
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver) #模拟打开浏览器
browser.get("https://tieba.baidu.com/index.html")

# new_list = browser.find_element_by_id('new_list')
# user_name = browser.find_element_by_name ('user_name')
active = browser.find_element_by_class_name  ('f-d-item')
# p = browser.find_element_by_tag_name ('p')

print(type(active))
print(active.text)

active1 = browser.find_element_by_class_name  ('rcmd_f_name')
active1.find_element_by_tag_name("a").click()


# find_element_by_name 通过name查找单个元素
# find_element_by_xpath 通过xpath查找单个元素
# find_element_by_link_text 通过链接查找单个元素
# find_element_by_partial_link_text 通过部分链接查找单个元素
# find_element_by_tag_name 通过标签名称查找单个元素
# find_element_by_class_name 通过类名查找单个元素
# find_element_by_css_selector 通过css选择武器查找单个元素
# find_elements_by_name 通过name查找多个元素
# find_elements_by_xpath 通过xpath查找多个元素
# find_elements_by_link_text 通过链接查找多个元素
# find_elements_by_partial_link_text 通过部分链接查找多个元素
# find_elements_by_tag_name 通过标签名称查找多个元素
# find_elements_by_class_name 通过类名查找多个元素
# find_elements_by_css_selector 通过css选择武器查找多个元素