# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/user1/Desktop/Yeni klasör/Yeni klasör/admin2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_admin2(object):
    def setupUi(self, admin2):
        admin2.setObjectName("admin2")
        admin2.resize(511, 661)
        self.centralwidget = QtWidgets.QWidget(admin2)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 170, 221, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 270, 221, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 370, 221, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 511, 661))
        self.label.setStyleSheet("background-image:tt.jpg);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("tt.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(410, 20, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        admin2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(admin2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 511, 21))
        self.menubar.setObjectName("menubar")
        admin2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(admin2)
        self.statusbar.setObjectName("statusbar")
        admin2.setStatusBar(self.statusbar)

        self.retranslateUi(admin2)
        QtCore.QMetaObject.connectSlotsByName(admin2)

    def retranslateUi(self, admin2):
        _translate = QtCore.QCoreApplication.translate
        admin2.setWindowTitle(_translate("admin2", "MainWindow"))
        self.pushButton.setText(_translate("admin2", "Change Admin password"))
        self.pushButton_2.setText(_translate("admin2", "Change User password"))
        self.pushButton_3.setText(_translate("admin2", "Take data"))
        self.pushButton_4.setText(_translate("admin2", "<--"))

