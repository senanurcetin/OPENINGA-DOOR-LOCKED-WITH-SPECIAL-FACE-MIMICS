from PyQt5.QtWidgets import *
from admin2_python import Ui_admin2
from admin3 import AFPage
from admin4 import AGPage


class AThirdPage(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_admin2()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.page1)
        self.ui.pushButton_2.clicked.connect(self.page2)
        self.ui.pushButton_3.clicked.connect(self.page3)
        self.ui.pushButton_4.clicked.connect(self.mainpage)

        self.admin3 = AFPage()
        self.admin4 = AGPage()

    def page1(self):
        self.admin3.show()

    def page2(self):
        self.admin4.show()

    def page3(self):
        import read_data
        read_data.transfer()

    def mainpage(self):
        from main_page import MainPage
        self.giris=MainPage()
        self.giris.show()
        self.close()
