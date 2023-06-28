#from selenium import webdriver
#from _MyPath import DRIVER as d
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from _MyPath import URL 
import time

# 옵션을 지정해 크롬 기동 --- (1)
options = webdriver.ChromeOptions()
options.add_argument('--headless')
# driver = webdriver.Chrome(d, options=options)
driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))

# 파이썬 페이지 열기 --- (2)
driver.get('https://python.org')

# 스크린샷 찍기 --- (3)
result = driver.save_screenshot('./ch4/output/screenshot.png')
if result : print('캡처 성공')

driver.quit()
