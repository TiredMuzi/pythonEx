# Selenium 불러오기 --- (1)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
driver.get('https://python.org')
time.sleep(3)
driver.quit()

# 책 예제 
# from selenium import webdriver
# import time
# from _MyPath import DRIVER as d
# 크롬 열기 --- (2)
# driver = webdriver.Chrome(d)
# 파이썬 페이지 열기 --- (3)
# driver.get('https://python.org')
# 3초 후에 크롬 닫기 --- (4)
#time.sleep(3)
# driver.quit()
