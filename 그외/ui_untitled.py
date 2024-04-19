# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
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
        Dialog.setObjectName("Dialog")
        Dialog.resize(227, 159)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.pushButton.clicked.connect(self.runevent)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

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
        df_from_excel.to_csv('로그인계정.csv', index=False)





    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "클릭"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
