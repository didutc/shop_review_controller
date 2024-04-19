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

# 영어 대소문자와 숫자를 포함한 모든 가능한 문자

# 1000에서 9999 사이의 난수 생성 (4자리)

target = 'https://healthyflow.co.kr/product/%ED%97%AC%EC%94%A8%ED%94%8C%EB%A1%9C%EC%9A%B0-95-%EC%95%84%EB%88%84%EC%B9%B4%EC%82%AC%EA%B3%BC-%EC%95%A4-%EB%B9%84%EC%98%A4%ED%8B%B4-%EB%A7%A5%EC%A3%BC%ED%9A%A8%EB%AA%A8/13/category/42/display/1/'






chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
service = Service("chromedriver.exe")
driver = webdriver.Chrome(service = service, options=chrome_options)
driver.switch_to.window(driver.window_handles[0])


while True:
    df_from_excel = pd.read_csv('구입계정.csv')
    df = df_from_excel.values.tolist()[0]
    elem = driver.get("https://healthyflow.co.kr/exec/front/Member/logout")
    time.sleep(2)
    elem = driver.get("https://healthyflow.co.kr/member/login.html?noMember=1&returnUrl=%2Forder%2Forderform.html%3Fbasket_type%3DA0000%26delvtype%3DA&delvtype=A")



    while True:
        try:                            
            elem = driver.find_element("xpath",'/html/body/div[3]/div/form/div/div/fieldset/label[1]/input').send_keys(df[0])

            break
        except:
            pyzard.errorboy()
            time.sleep(2)
    while True:
        try:                   
            elem = driver.find_element("xpath",'/html/body/div[3]/div/form/div/div/fieldset/label[2]/input').send_keys(df[1])

            break
        except:
            pyzard.errorboy()
            time.sleep(2)
 
    while True:
        try:                   
            elem = driver.find_element("xpath",'/html/body/div[3]/div/form/div/div/fieldset/a').click()

            break
        except:
            pyzard.errorboy()
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
            pyzard.errorboy()          
            time.sleep(1)
            dacounter1 = dacounter1+1

    time.sleep(1)
    elem = driver.get(target)
    while True:
        try:                   
            elem = driver.find_element("xpath",'/html/body/div[3]/div/div[2]/div[2]/div[2]/table/tbody[1]/tr/td/ul/li[1]/a/span').click()

            break
        except:
            pyzard.errorboy()
            time.sleep(2)

    time.sleep(2)
    while True:
        try:                   
            elem = driver.find_element("xpath",'/html/body/div[3]/div/div[2]/div[2]/div[2]/div[8]/div[1]/a[3]/span[1]').click()

            break
        except:
            pyzard.errorboy()
            time.sleep(2)
    time.sleep(2)

                      
    select = Select(driver.find_element("xpath",'/html/body/form[1]/div/div[8]/div[2]/div[3]/div[1]/table/tbody/tr[1]/td/select'))
    select.select_by_visible_text("농협 3022665525391 박상현")
    time.sleep(1)
    while True:
        try:                                    
            elem = driver.find_element("xpath",'/html/body/form[1]/div/div[8]/div[2]/div[3]/div[1]/table/tbody/tr[2]/td/input').send_keys(df[2])

            break
        except:
            pyzard.errorboy()
            time.sleep(2) 
    time.sleep(1) 
    while True:
        try:                   
            elem = driver.find_element("xpath",'/html/body/form[1]/div/div[11]/button').click()

            break
        except:
            pyzard.errorboy()
            time.sleep(2) 
    time.sleep(3) 
    df_from_excel.drop(0,  inplace=True)
    print(df_from_excel)
    df_from_excel.to_csv('구입계정.csv', index=False)