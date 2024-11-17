from mainwindow_ui import Ui_MainWindow
from PianoFrame import PianoFrame
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PySide6.QtGui import QIcon
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.icon = QIcon("./resources/note.bmp")
        self.setWindowIcon(self.icon)
        self.pianoFrame = PianoFrame()
        self.records = self.pianoFrame.records
        self.action_sync.triggered.connect(self.sync)
        self.action_play.triggered.connect(self.play)
        self.action_delete.triggered.connect(self.delete)

    def sync(self):
        self.listWidget.clear()
        for r in self.records:
            self.listWidget.addItem(r[0])

    def play(self):
        if self.listWidget.selectedIndexes():
            for r in self.records:
                if r[0] == self.listWidget.selectedItems()[0].text():
                    self.pianoFrame.play(r[1], r[2])
                    break

    def delete(self):
        if self.listWidget.selectedIndexes():
            warn = QMessageBox.warning(
                self,
                self.tr("警告"),
                self.tr("确定要删除吗？"),
                QMessageBox.Yes | QMessageBox.No,
            )
            if warn == QMessageBox.No:
                return
            for r in self.records:
                if r[0] == self.listWidget.selectedItems()[0].text():
                    self.records.remove(r)
                    # print(self.pianoFrame.records)
                    break
            self.sync()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    piano = MainWindow()
    piano.show()
    sys.exit(app.exec())
