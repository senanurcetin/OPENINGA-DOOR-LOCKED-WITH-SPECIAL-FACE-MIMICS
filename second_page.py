from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from admin_python import Ui_MainWindow
from admin2 import AThirdPage
import numpy as np


class SecondPage(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.ui.comboBox.addItem("0",0)
        self.ui.comboBox.addItem("1",1)
        self.ui.comboBox.addItem("2",2)
        self.ui.comboBox.addItem("3",3)
        self.ui.comboBox.addItem("4",4)
        self.ui.comboBox.addItem("5",5)
        self.ui.comboBox.addItem("6",6)
        self.ui.comboBox.addItem("7",7)
        self.ui.comboBox.addItem("8",8)
        self.ui.comboBox.addItem("9",9)

        self.ui.comboBox_2.addItem("0", 0)
        self.ui.comboBox_2.addItem("1", 1)
        self.ui.comboBox_2.addItem("2", 2)
        self.ui.comboBox_2.addItem("3", 3)
        self.ui.comboBox_2.addItem("4", 4)
        self.ui.comboBox_2.addItem("5", 5)
        self.ui.comboBox_2.addItem("6", 6)
        self.ui.comboBox_2.addItem("7", 7)
        self.ui.comboBox_2.addItem("8", 8)
        self.ui.comboBox_2.addItem("9", 9)

        self.ui.comboBox_3.addItem("0", 0)
        self.ui.comboBox_3.addItem("1", 1)
        self.ui.comboBox_3.addItem("2", 2)
        self.ui.comboBox_3.addItem("3", 3)
        self.ui.comboBox_3.addItem("4", 4)
        self.ui.comboBox_3.addItem("5", 5)
        self.ui.comboBox_3.addItem("6", 6)
        self.ui.comboBox_3.addItem("7", 7)
        self.ui.comboBox_3.addItem("8", 8)
        self.ui.comboBox_3.addItem("9", 9)

        self.ui.comboBox_4.addItem("0", 0)
        self.ui.comboBox_4.addItem("1", 1)
        self.ui.comboBox_4.addItem("2", 2)
        self.ui.comboBox_4.addItem("3", 3)
        self.ui.comboBox_4.addItem("4", 4)
        self.ui.comboBox_4.addItem("5", 5)
        self.ui.comboBox_4.addItem("6", 6)
        self.ui.comboBox_4.addItem("7", 7)
        self.ui.comboBox_4.addItem("8", 8)
        self.ui.comboBox_4.addItem("9", 9)

        self.ui.pushButton.clicked.connect(self.clk)
        self.ui.pushButton_2.clicked.connect(self.clk2)

        self.admin2 = AThirdPage()

    def clk(self):
        import numpy as np
        import pandas as pd

        df = pd.read_excel('passwords.xls')
        Id = df['Id']
        Password0 = df['Password0']
        Password1 = df['Password1']
        Password2 = df['Password2']
        Password3 = df['Password3']

        key_0 = self.ui.comboBox.currentText()
        key_1 = self.ui.comboBox_2.currentText()
        key_2 = self.ui.comboBox_3.currentText()
        key_3 = self.ui.comboBox_4.currentText()
        new_password = np.array([int(key_0), int(key_1), int(key_2), int(key_3)])
        admin_password = np.array([Password0[0], Password1[0], Password2[0], Password3[0]])
        if (admin_password == new_password).all():
            print("Login Confirmed")
            self.admin2.show()
            self.close()
        else:
            print("Entry Denied")

    def clk2(self):
          from main_page import MainPage
          self.giris = MainPage()
          self.giris.show()
          self.close()
