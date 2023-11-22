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


for li in scout_list:
    

    elem = driver.get("https://healthyflow.co.kr/exec/front/Member/logout")
    time.sleep(2)
    elem = driver.get("https://healthyflow.co.kr/member/login.html?noMember=1&returnUrl=%2Forder%2Forderform.html%3Fbasket_type%3DA0000%26delvtype%3DA&delvtype=A")



    while True:
        try:                            
            elem = driver.find_element("xpath",'/html/body/div[3]/div/form/div/div/fieldset/label[1]/input').send_keys(li[0])

            break
        except:

            time.sleep(2)
    while True:
        try:                   
            elem = driver.find_element("xpath",'/html/body/div[3]/div/form/div/div/fieldset/label[2]/input').send_keys(li[1])

            break
        except:

            time.sleep(2)
 
    while True:
        try:                   
            elem = driver.find_element("xpath",'/html/body/div[3]/div/form/div/div/fieldset/a').click()

            break
        except:

            time.sleep(2)
    da = Alert(driver)
    dacounter1 = 0
    while True:
        if dacounter1 == 2:
            break
        try:
            da.accept()
            break
        except:
            time.sleep(1)
            dacounter1 = dacounter1+1

    time.sleep(1)
    elem = driver.get(target)
    select = Select(driver.find_element("xpath",'/html/body/div[3]/div/div[2]/div[2]/div[2]/table/tbody[1]/tr/td/select'))
    select.select_by_visible_text("1개 1달분")
    time.sleep(2)
    while True:
        try:                   
            elem = driver.find_element("xpath",'/html/body/div[3]/div/div[2]/div[2]/div[2]/div[8]/div[1]/a[3]/span[1]').click()

            break
        except:
            time.sleep(2)
    time.sleep(2)
    while True:
        try:                   
            elem = driver.find_element("xpath",'/html/body/form[1]/div/div[2]/div[3]/div[2]/div[2]/div[3]/div[2]/table/tbody/tr[2]/td/ul/li[6]/button').click()

            break
        except:
            time.sleep(2)
    document = driver.find_elements(By.TAG_NAME,'iframe')
    driver.switch_to.frame(document[6])
    document = driver.find_elements(By.TAG_NAME,'iframe')
    driver.switch_to.frame(document[0])
    document = driver.find_elements(By.TAG_NAME,'iframe')
    driver.switch_to.frame(document[0])
    


    while True:
        try:                   
            elem = driver.find_element("xpath",'/html/body/div[1]/div/div[1]/form/fieldset/div/div/input').send_keys('백현동 532')

            break
        except:

            time.sleep(2)    
    while True:
        try:                   
            elem = driver.find_element("xpath",'/html/body/div[1]/div/div[1]/form/fieldset/div/button[2]').click()

            break
        except:

            time.sleep(2)    
    while True:
        try:                   
            elem = driver.find_element("xpath",'/html/body/div[1]/div/div[2]/ul/li/dl/dd[1]/span/button/span[1]').click()

            break
        except:

            time.sleep(2)    

    driver.switch_to.default_content()
    time.sleep(1) 
    while True:
        try:                   
            elem = driver.find_element("xpath",'/html/body/form[1]/div/div[2]/div[3]/div[2]/div[2]/div[3]/div[2]/table/tbody/tr[2]/td/ul/li[8]/input').send_keys('백현동 532')

            break
        except:

            time.sleep(2)    



    while True:
        try:                   
            elem = driver.find_element("xpath",'/html/body/form[1]/div/div[2]/div[3]/div[2]/div[2]/div[3]/div[2]/table/tbody/tr[4]/td/div/input[1]').send_keys(random.randint(1000, 9999))

            break
        except:

            time.sleep(2)    
    while True:
        try:                   
            elem = driver.find_element("xpath",'/html/body/form[1]/div/div[2]/div[3]/div[2]/div[2]/div[3]/div[2]/table/tbody/tr[4]/td/div/input[2]').send_keys(random.randint(1000, 9999))

            break
        except:

            time.sleep(2)    
    select = Select(driver.find_element("xpath",'/html/body/form[1]/div/div[8]/div[2]/div[3]/div[1]/table/tbody/tr[1]/td/select'))
    select.select_by_visible_text("농협:3022665525391 박상현")
    while True:
        try:                   
            elem = driver.find_element("xpath",'/html/body/form[1]/div/div[8]/div[2]/div[3]/div[1]/table/tbody/tr[2]/td/input').send_keys(li[2])

            break
        except:

            time.sleep(2) 
    time.sleep(1) 
    while True:
        try:                   
            elem = driver.find_element("xpath",'/html/body/form[1]/div/div[11]/button').click()

            break
        except:

            time.sleep(2) 
    time.sleep(1) 
    # da = Alert(driver)
    # dacounter1 = 0
    # while True:
    #     if dacounter1 == 2:
    #         break
    #     try:
    #         da.accept()
    #         break
    #     except:
    #         time.sleep(1)
    #         dacounter1 = dacounter1+1
