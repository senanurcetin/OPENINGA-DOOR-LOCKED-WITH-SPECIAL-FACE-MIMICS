from PyQt5.QtWidgets import *
from userbasarısız_python import Ui_MainWindow

class Fail(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
