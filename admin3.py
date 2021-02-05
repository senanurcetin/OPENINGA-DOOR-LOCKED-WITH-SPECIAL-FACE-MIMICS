from PyQt5.QtWidgets import *
from admin3_python import Ui_MainWindow
from decimal import*

class AFPage(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.comboBox.addItem("0", 0)
        self.ui.comboBox.addItem("1", 1)
        self.ui.comboBox.addItem("2", 2)
        self.ui.comboBox.addItem("3", 3)
        self.ui.comboBox.addItem("4", 4)
        self.ui.comboBox.addItem("5", 5)
        self.ui.comboBox.addItem("6", 6)
        self.ui.comboBox.addItem("7", 7)
        self.ui.comboBox.addItem("8", 8)
        self.ui.comboBox.addItem("9", 9)

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

    def clk(self):
        import pandas as pd
        import xlwt

        style_string = "font: bold on; borders: bottom dashed"
        style = xlwt.easyxf(style_string)

        wb = xlwt.Workbook(encoding="utf-8")
        ws = wb.add_sheet('passwords', cell_overwrite_ok=True)

        df = pd.read_excel('passwords.xls')
        Id = df['Id']
        PasswordName = df['Password_Name']
        Password0 = df['Password0']
        Password1 = df['Password1']
        Password2 = df['Password2']
        Password3 = df['Password3']
        length = len(df)

        ws.write(0, 0, 'Id', style=style)
        ws.write(0, 1, 'Password_Name', style=style)
        ws.write(0, 2, 'Password0', style=style)
        ws.write(0, 3, 'Password1', style=style)
        ws.write(0, 4, 'Password2', style=style)
        ws.write(0, 5, 'Password3', style=style)

        for z in range(0, length):
            ws.write(z + 1, 0, int(Id[z]))
            ws.write(z + 1, 1, PasswordName[z])
            ws.write(z + 1, 2, int(Password0[z]))
            ws.write(z + 1, 3, int(Password1[z]))
            ws.write(z + 1, 4, int(Password2[z]))
            ws.write(z + 1, 5, int(Password3[z]))

        key_0 = self.ui.comboBox.currentText()
        key_1 = self.ui.comboBox_2.currentText()
        key_2 = self.ui.comboBox_3.currentText()
        key_3 = self.ui.comboBox_4.currentText()

        ws.write(1, 2, int(key_0))
        ws.write(1, 3, int(key_1))
        ws.write(1, 4, int(key_2))
        ws.write(1, 5, int(key_3))
        wb.save('passwords.xls')
        self.close()


