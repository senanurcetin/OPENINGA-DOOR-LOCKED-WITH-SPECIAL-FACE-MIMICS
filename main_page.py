from PyQt5.QtWidgets import*
from giris_python import Ui_MainWindow
from second_page import SecondPage
from third_page import ThirdPage
import time

class MainPage(QMainWindow) :
    def __init__(self):
        super(). __init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.open_third_page)
        self.ui.pushButton_3.clicked.connect(self.open_second_page)

        self.admin = SecondPage()
        self.userbos = ThirdPage()

    def open_second_page(self):
        self.admin.show()
        self.close()

    def open_third_page(self):
        self.userbos.show()
        self.close()
        import camera



