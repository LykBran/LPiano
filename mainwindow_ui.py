# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QListView, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(799, 600)
        self.action_import = QAction(MainWindow)
        self.action_import.setObjectName(u"action_import")
        self.action_export = QAction(MainWindow)
        self.action_export.setObjectName(u"action_export")
        self.action_sync = QAction(MainWindow)
        self.action_sync.setObjectName(u"action_sync")
        self.action_update = QAction(MainWindow)
        self.action_update.setObjectName(u"action_update")
        self.action_remame = QAction(MainWindow)
        self.action_remame.setObjectName(u"action_remame")
        self.action_delete = QAction(MainWindow)
        self.action_delete.setObjectName(u"action_delete")
        self.action_undo = QAction(MainWindow)
        self.action_undo.setObjectName(u"action_undo")
        self.action_redo = QAction(MainWindow)
        self.action_redo.setObjectName(u"action_redo")
        self.action_play = QAction(MainWindow)
        self.action_play.setObjectName(u"action_play")
        self.action_rename = QAction(MainWindow)
        self.action_rename.setObjectName(u"action_rename")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMovement(QListView.Movement.Static)

        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 799, 33))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        self.menu_Edit = QMenu(self.menubar)
        self.menu_Edit.setObjectName(u"menu_Edit")
        self.menu_Record = QMenu(self.menubar)
        self.menu_Record.setObjectName(u"menu_Record")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_Record.menuAction())
        self.menu_File.addAction(self.action_import)
        self.menu_File.addAction(self.action_export)
        self.menu_Edit.addAction(self.action_delete)
        self.menu_Record.addAction(self.action_sync)
        self.menu_Record.addSeparator()
        self.menu_Record.addAction(self.action_play)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_import.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165", None))
        self.action_export.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
        self.action_sync.setText(QCoreApplication.translate("MainWindow", u"\u540c\u6b65", None))
        self.action_update.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u65b0", None))
        self.action_remame.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u547d\u540d", None))
        self.action_delete.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.action_undo.setText(QCoreApplication.translate("MainWindow", u"\u64a4\u9500", None))
        self.action_redo.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u505a", None))
        self.action_play.setText(QCoreApplication.translate("MainWindow", u"\u64ad\u653e", None))
        self.action_rename.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u547d\u540d", None))
        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_Edit.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        self.menu_Record.setTitle(QCoreApplication.translate("MainWindow", u"\u5f55\u97f3", None))
    # retranslateUi

