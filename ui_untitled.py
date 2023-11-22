# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledxzgJfA.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
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



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(227, 159)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.runevent)

        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi
    def runevent(self):
        df_from_excel = pd.read_csv('로그인계정.csv')


        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        service = Service("chromedriver.exe")
        driver = webdriver.Chrome(service = service, options=chrome_options)
        driver.switch_to.window(driver.window_handles[0])
        elem = driver.get("https://healthyflow.co.kr/exec/front/Member/logout")
        time.sleep(2)
        elem = driver.get("https://healthyflow.co.kr/member/login.html?noMember=1&returnUrl=%2Forder%2Forderform.html%3Fbasket_type%3DA0000%26delvtype%3DA&delvtype=A")


        df = df_from_excel.values.tolist()[1]
        print(df_from_excel)

        while True:
            try:                            
                elem = driver.find_element("xpath",'/html/body/div[3]/div/form/div/div/fieldset/label[1]/input').send_keys(df[0])

                break
            except:

                time.sleep(2)
        while True:
            try:                   
                elem = driver.find_element("xpath",'/html/body/div[3]/div/form/div/div/fieldset/label[2]/input').send_keys(df[1])

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
        driver.get("https://healthyflow.co.kr/board/review/write.html?board_no=4&product_no=11&cate_no=42&display_group=1#none")

        df_from_excel.drop(0,  inplace=True)
        print(df_from_excel)
        df_from_excel.to_csv('example.csv', index=False)
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\ud074\ub9ad", None))
    # retranslateUi

def main():


    app = QApplication(sys.argv)

    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    app.exec()


if __name__ == '__main__':
    main()
