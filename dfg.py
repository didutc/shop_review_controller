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
import pyzard
from selenium.webdriver.common.by import By
import random
import string
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
# 현재 스크립트 파일의 절대 경로
script_path = os.path.abspath(__file__)

# 현재 스크립트 파일의 디렉토리 경로
script_dir = os.path.dirname(script_path)
# 영어 대소문자와 숫자를 포함한 모든 가능한 문자

# Chrome 드라이버를 설정할 때 옵션 전달



chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
document = driver.find_elements(By.TAG_NAME,'iframe')

driver.switch_to.frame(document[0])

while True:
    try:                   
        elem = driver.find_element("xpath",'/html/body').click()

        break
    except:
        pyzard.errorboy()
        time.sleep(2)  

driver.switch_to.default_content()

while True:
    try:                   
        elem = driver.find_element("xpath",'/html/body/div[2]/div[2]/div[3]/div[5]/div/form/div/div[2]/table/tbody[1]/tr[1]/td/input').click()

        break
    except:
        pyzard.errorboy()
        time.sleep(2)  