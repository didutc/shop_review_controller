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




df_from_excel = pd.read_csv('자사몰 계정.csv')

scout_list = df_from_excel.values.tolist()
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
service = Service("chromedriver.exe")
driver = webdriver.Chrome(service = service, options=chrome_options)
driver.switch_to.window(driver.window_handles[0])


for li in scout_list:
    

    elem = driver.get("https://healthyflow.co.kr/member/join.html")



    while True:
        try:                   
            elem = driver.find_element("xpath",'/html/body/div[3]/div/form[2]/div/div[2]/table/tbody/tr[1]/td/input').send_keys(li[0])

            break
        except:

            time.sleep(2)
    while True:
        try:                   
            elem = driver.find_element("xpath",'/html/body/div[3]/div/form[2]/div/div[2]/table/tbody/tr[2]/td/div/input').send_keys(li[1])

            break
        except:

            time.sleep(2)
    while True:
        try:                   
            elem = driver.find_element("xpath",'/html/body/div[3]/div/form[2]/div/div[2]/table/tbody/tr[3]/td/input').send_keys(li[1])

            break
        except:

            time.sleep(2)
    while True:
        try:                   
            elem = driver.find_element("xpath",'/html/body/div[3]/div/form[2]/div/div[2]/table/tbody/tr[6]/td/span[1]/input').send_keys(li[2])

            break
        except:

            time.sleep(2)
    while True:
        try:                   
            elem = driver.find_element("xpath",'/html/body/div[3]/div/form[2]/div/div[2]/table/tbody/tr[14]/td/input[1]').send_keys(random.randint(1000, 9999))

            break
        except:

            time.sleep(2)    

    while True:
        try:                   
            elem = driver.find_element("xpath",'/html/body/div[3]/div/form[2]/div/div[2]/table/tbody/tr[14]/td/input[2]').send_keys(random.randint(1000, 9999))

            break
        except:

            time.sleep(2)    

    characters = string.ascii_letters + string.digits

    # 6자리의 임의 난수 생성
    random_id = ''.join(random.choice(characters) for _ in range(8))
    random_email = random_id + '@gmail.com'
    while True:
        try:                   
            elem = driver.find_element("xpath",'/html/body/div[3]/div/form[2]/div/div[2]/table/tbody/tr[16]/td/input').send_keys(random_email)

            break
        except:

            time.sleep(2)    
    while True:
        try:                   

            elem = driver.find_element("xpath",'/html/body/div[3]/div/form[2]/div/div[4]/p/span/input').click()
            break
        except:

            time.sleep(2)    
    while True:
        try:                   

            elem = driver.find_element("xpath",'/html/body/div[3]/div/form[2]/div/div[11]/a').click()
            break
        except:

            time.sleep(2)    
    time.sleep(3)  
    elem = driver.get("https://healthyflow.co.kr/exec/front/Member/logout")
    time.sleep(2)  