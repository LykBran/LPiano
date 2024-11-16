from ui_mainwindow import Ui_MainWindow
from PianoFrame import PianoFrame
from PySide6.QtWidgets import QMainWindow, QApplication
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pianoFrame = PianoFrame()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    piano = MainWindow()
    piano.show()
    sys.exit(app.exec())
