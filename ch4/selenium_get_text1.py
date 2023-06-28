from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from _MyPath import URL 
import time

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time
# from _MyPath import URL, DRIVER as d

# 책 소개 사이트 열기 --- (1)
# driver = webdriver.Chrome(d)
driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
driver.get(URL)

# h1 요소의 텍스트 출력하기 --- (2)
# ele = driver.find_element_by_tag_name('h1')
ele =  driver.find_element(By.TAG_NAME, 'h1')
print('h1:', ele.text)

# id가 cnt인 요소의 텍스트 출력하기 --- (3)
#ele = driver.find_element_by_id('cnt')
ele = driver.find_element(By.ID, 'cnt')
print('#cnt:', ele.text)

time.sleep(3)
driver.quit()
