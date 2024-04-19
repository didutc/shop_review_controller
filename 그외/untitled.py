import pandas as pd
import pyzard
import selenium
import time
from selenium.webdriver.common.alert import Alert
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import subprocess
import doubleagent
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
import random
import string

# 영어 대소문자와 숫자를 포함한 모든 가능한 문자

# 1000에서 9999 사이의 난수 생성 (4자리)

target = 'https://healthyflow.co.kr/product/mbp-%EC%BD%98%EB%93%9C%EB%A1%9C%EC%9D%B4%EC%B9%9C-%EB%A5%98%EC%8B%A0-%EB%8B%A8%EB%B0%B1%EB%B9%8C-max-1200/11/category/42/display/1/'



df_from_excel = pd.read_csv('자사몰 계정.csv')

scout_list = df_from_excel.values.tolist()
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
service = Service("chromedriver.exe")
driver = webdriver.Chrome(service = service, options=chrome_options)
driver.switch_to.window(driver.window_handles[0])


# document = driver.find_elements(By.TAG_NAME,'iframe')

# driver.switch_to.frame(document[0])

while True:
    try:                   
        elem = driver.find_element("xpath",'/html/body/p').send_keys('백현동 532')

        break
    except:

        time.sleep(2)  