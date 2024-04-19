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

class Ui_Dialog(object):
    def __init__(self):
        super(Ui_Dialog,self).__init__()

        
        self.Dialog = QWidget(self)   
        if not self.Dialog.objectName():
            self.Dialog.setObjectName(u"Dialog")
        self.Dialog.resize(227, 159)
        self.verticalLayout_2 = QVBoxLayout(self.Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(self.Dialog)

        QMetaObject.connectSlotsByName(self.Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        self.Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\ud074\ub9ad", None))
    # retranslateUi

def main():



    app = QApplication(sys.argv)
    mainwindow = Ui_Dialog()
    mainwindow.show()
    app.exec()


if __name__ == '__main__':
    main()
