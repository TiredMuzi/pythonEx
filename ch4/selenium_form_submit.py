# from selenium import webdriver
# import time
# from _MyPath import URL, DRIVER as d
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from _MyPath import URL 
import time

# 메소드 테스트 페이지 열기 --- (1)
# driver = webdriver.Chrome(d)
# driver.get(URL+'method')
driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
driver.get(URL+'method')
driver.add_cookie({'name':'mycookie','value':'it is my cookie'})

# 입력 박스 찾기 --- (2)
# getFir = driver.find_element_by_id('getFir')
# getSec = driver.find_element_by_id('getSec')
getFir = driver.find_element(By.ID, 'getFir')
getSec = driver.find_element(By.ID, 'getSec')

# 입력 박스 초기화 --- (3)
getFir.clear()
getSec.clear()
time.sleep(2)

# 키워드 입력 --- (4)
getFir.send_keys('First Value')
getSec.send_keys('Second Value')
time.sleep(2)

# 폼 제출하기 --- (5)
getSec.submit()
time.sleep(2)

# 호출 결과 받아오기 --- (6)
# gResult = driver.find_element_by_id('gResult')
gResult = driver.find_element(By.ID, 'gResult')
print(gResult.text)

time.sleep(5)
driver.quit()
