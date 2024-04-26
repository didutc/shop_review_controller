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









# Chrome 드라이버를 설정할 때 옵션 전달



chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")







# Chrome 드라이버를 설정할 때 옵션 전달
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.switch_to.window(driver.window_handles[0])
print(211)
while True:
    df_from_excel = pd.read_csv(script_dir+'//댓글로그인.csv')

    df_from_txt = pyzard.readfile(script_dir+'//댓글컨텐츠.txt')
    time.sleep(2)
    elem = driver.get("https://healthyflow.co.kr/exec/front/Member/logout")
    time.sleep(2)
    elem = driver.get("https://healthyflow.co.kr/member/login.html?noMember=1&returnUrl=%2Forder%2Forderform.html%3Fbasket_type%3DA0000%26delvtype%3DA&delvtype=A")

    triger = df_from_excel.values.tolist()
    if len(triger) == 0:
        break
    login_lst = df_from_excel.values.tolist()[0]
    df_from_txt =df_from_txt.split('\n')
    comment_lst = df_from_txt[0].split('\t')
    print(login_lst)
    print(comment_lst)

    while True:
        try:                            
            elem = driver.find_element("xpath",'/html/body/div[2]/div[2]/div[3]/div[5]/form/div/div/fieldset/div/div[1]/span/input').send_keys(login_lst[0])

            break
        except:
            pyzard.errorboy()
            time.sleep(2)
    while True:
        try:                   
            elem = driver.find_element("xpath",'/html/body/div[2]/div[2]/div[3]/div[5]/form/div/div/fieldset/div/div[1]/input').send_keys(login_lst[1])

            break
        except:
            pyzard.errorboy()
            time.sleep(2)
    try:
        elem = driver.find_element("xpath",'/html/body/div[2]/div[2]/div[3]/div[5]/form/div/div/fieldset/div/div[3]/button').click()
    except:
        pass
    da = Alert(driver)
    dacounter1 = 0
    time.sleep(2)
    while True:

        try:
            da.accept()
            break
        except:
            pyzard.errorboy()            
            time.sleep(1)

            break
    time.sleep(2)
    driver.get("https://healthyflow.co.kr/board/product/write.html?board_no=4&product_no=26&cate_no=1")
    while True:
        try:                   
            elem = driver.find_element("xpath",'/html/body/div[2]/div[2]/div[3]/div[5]/div/form/div/div[2]/table/tbody[1]/tr[1]/td/p[2]/input').send_keys(comment_lst[0])

            break
        except:
            pyzard.errorboy()
            time.sleep(2)  

    document = driver.find_elements(By.TAG_NAME,'iframe')

    driver.switch_to.frame(document[0])

    while True:
        try:                   
            elem = driver.find_element("xpath",'/html/body/p').send_keys(comment_lst[1])

            break
        except:
            pyzard.errorboy()
            time.sleep(2)  

    driver.switch_to.default_content()
    time.sleep(1) 
    while True:
        try:                   
            elem = driver.find_element("xpath",'/html/body/div[2]/div[2]/div[3]/div[5]/div/form/div/div[4]/button').click()

            break
        except:
            pyzard.errorboy()
            time.sleep(2)  



    df_from_excel.drop(0,  inplace=True)
    df_from_txt=df_from_txt[1:]
    df_from_txt ='\n'.join(df_from_txt)
    df_from_excel.to_csv(script_dir+'//댓글로그인.csv', index=False)
    pyzard.report(script_dir+'//댓글컨텐츠.xlsx', df_from_txt)
