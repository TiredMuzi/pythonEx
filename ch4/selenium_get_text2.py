#from selenium import webdriver
#import time
#from _MyPath import URL, DRIVER as d
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from _MyPath import URL 
import time

# 책 소개 사이트 열기 --- (1)
#driver = webdriver.Chrome(d)
#driver.get(URL)
driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
driver.get(URL)


# title 및 div.title 요소 가져오기 --- (2)
# title = driver.find_element_by_tag_name('title')
# div = driver.find_element_by_class_name('title')

title = driver.find_element(By.TAG_NAME, 'title')
div = driver.find_element(By.CLASS_NAME, 'title')

# text 속성 출력 --- (3)
print('---------text---------')
print('<title>:', title.text) #빈 문자열
print('<div>:', div.text) #빈 문자열

#display 여부 출력 --- (4)
print('---------is_displayed()---------')
print('<title>:', title.is_displayed())
print('<div>:',div.is_displayed())

# innerText 속성 가져오기 --- (5)
print('---------innerText---------')
print('<title>:', title.get_attribute('innerText'))
print('<div>:',div.get_attribute('innerText'))

time.sleep(3)
driver.quit()
