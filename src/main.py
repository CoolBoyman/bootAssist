from PySide2.QtWidgets import QApplication
from src.MainWindows import MainWindows
import sys

if __name__ == "__main__":
    # test
    app = QApplication(sys.argv)
    loginWin = MainWindows()
    loginWin.ui.show()
    app.exec_()
