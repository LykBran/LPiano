from mainwindow_ui import Ui_MainWindow
from PianoFrame import PianoFrame, notesList, notesListM, soundList, soundListM
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog
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
        self.action_export.triggered.connect(self.export)
        self.action_import.triggered.connect(self.imp)

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

    def export(self):
        if not self.listWidget.selectedIndexes():
            return
        name = self.listWidget.selectedItems()[0].text()
        filename = QFileDialog.getSaveFileName(
            self, self.tr("导出录音"), "", self.tr("LPiano 录音文件 (*.lpr)")
        )[0]
        if not filename:
            return
        with open(filename, "w") as f:
            for r in self.records:
                if r[0] == name:
                    for n in r[3]:
                        f.write(n + " ")
                    f.write("\n")
                    for t in r[2]:
                        f.write(str(t) + " ")
                    f.write("\n")
                    break

    def imp(self):
        filename = QFileDialog.getOpenFileName(
            self, self.tr("导入录音"), "", self.tr("LPiano 录音文件 (*.lpr)")
        )[0]
        if not filename:
            return
        with open(filename, "r") as f:
            lines = f.readlines()
            notes = [n for n in lines[0].strip().split()]
            times = [float(t) for t in lines[1].strip().split()]
            sounds = []
            for n in notes:
                try:
                    i = notesList.index(n)
                    sounds.append(soundList[i])
                except ValueError:
                    i = notesListM.index(n)
                    sounds.append(soundListM[i])
            self.records.append((filename.split("/")[-1], sounds, times, notes))
        self.sync()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    piano = MainWindow()
    piano.show()
    sys.exit(app.exec())
