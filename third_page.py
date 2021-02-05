from PyQt5.QtWidgets import *
from userbos_python import Ui_MainWindow
from user_success import Success
from user_fail import Fail



class ThirdPage(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.clk)

        self.succes = Success()
        self.fail = Fail()

    def refresh(self, key):
        self.key = key
        self.analyze()

    def analyze(self):
        if self.key == 1:
            self.succes.show()
        else:
            self.fail.show()
    def clk(self):
        from main_page import MainPage
        self.giris = MainPage()
        self.giris.show()
        self.close()
