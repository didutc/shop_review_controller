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

# 1000에서 9999 사이의 난수 생성 (4자리)

target = 'https://healthyflow.co.kr/product/%EB%A7%88%EC%B9%B4%EC%A0%A0-%EB%B8%94%EB%9E%99%EB%A7%88%EC%B9%B4/26/category/1/display/15/'

limit = input('몇명 작업할까요?')

limit = int(limit)


chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")







# Chrome 드라이버를 설정할 때 옵션 전달
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.switch_to.window(driver.window_handles[0])
triger = 0
while True:
    if triger == limit:
        break
    df_from_excel = pd.read_csv(script_dir+'//구입계정.csv')
    print(df_from_excel)

    df = df_from_excel.values.tolist()[0]
    elem = driver.get("https://healthyflow.co.kr/exec/front/Member/logout")
    time.sleep(2)
    elem = driver.get("https://healthyflow.co.kr/member/login.html?noMember=1&returnUrl=%2Forder%2Forderform.html%3Fbasket_type%3DA0000%26delvtype%3DA&delvtype=A")



    while True:
        try:                            
            elem = driver.find_element("xpath",'/html/body/div[2]/div[2]/div[3]/div[5]/form/div/div/fieldset/div/div[1]/span/input').send_keys(df[0])

            break
        except:
            pyzard.errorboy()
            time.sleep(2)
    while True:
        try:                   
            elem = driver.find_element("xpath",'/html/body/div[2]/div[2]/div[3]/div[5]/form/div/div/fieldset/div/div[1]/input').send_keys(df[1])

            break
        except:
            pyzard.errorboy()
            time.sleep(2)
 
    # while True:
    #     try:                   
    #         elem = driver.find_element("xpath",'/html/body/div[2]/div[2]/div[3]/div[5]/form/div/div/fieldset/div/div[3]/button').click()

    #         break
    #     except:

    #         pyzard.errorboy()
    #         time.sleep(2)
    elem = driver.find_element("xpath",'/html/body/div[2]/div[2]/div[3]/div[5]/form/div/div/fieldset/div/div[3]/button').click()

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

    time.sleep(3)
    elem = driver.get(target)
    while True:
        try:                   
            elem = driver.find_element("xpath",'/html/body/div[2]/div[2]/div[3]/div[5]/div[1]/div[2]/div[2]/div[4]/div[2]/div/div[1]/table/tbody[2]/tr/td/ul/li[5]/a/span').click()

            break
        except:
            driver.execute_script("window.scrollTo(0, {})".format(700))
            pyzard.errorboy()
            time.sleep(2)

    time.sleep(2)
    while True:
        try:                   
            elem = driver.find_element("xpath",'/html/body/div[2]/div[2]/div[3]/div[5]/div[1]/div[2]/div[2]/div[4]/div[2]/div/div[5]/div[2]/a/span[1]').click()

            break
        except:
            driver.execute_script("window.scrollTo(0, {})".format(700))
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
    df_from_excel.to_csv(script_dir+'//구입계정.csv', index=False)
    triger = triger+1