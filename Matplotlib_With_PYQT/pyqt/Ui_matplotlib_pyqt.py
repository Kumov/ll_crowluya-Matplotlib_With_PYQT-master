# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'matplotlib_pyqt.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QStackedWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        # window = QMainWindow()
        # window.resize(800, 600)

        # self.centralwidget = QtWidgets.QWidget(MainWindow)
        # self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.stack = QStackedWidget(parent=MainWindow)
        self.centralwidget = QStackedWidget(parent=MainWindow)

        self.centralwidget.setObjectName("centralwidget")

        # self.matplotlibwidget_static = MatplotlibWidget(self.centralwidget)
        matplotlibwidget_static = MatplotlibWidget()
        matplotlibwidget_static.setGeometry(QtCore.QRect(10, 0, 611, 271))
        matplotlibwidget_static.setObjectName("matplotlibwidget_static")

        self.stack.addWidget(matplotlibwidget_static)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(670, 80, 75, 23))
        self.pushButton.setObjectName("pushButton")

        # self.matplotlibwidget_dynamic = MatplotlibWidget()
        # self.matplotlibwidget_dynamic.setEnabled(True)
        # self.matplotlibwidget_dynamic.setGeometry(QtCore.QRect(10, 270, 611, 291))
        # self.matplotlibwidget_dynamic.setObjectName("matplotlibwidget_dynamic")
        matplotlibwidget_dynamic = MatplotlibWidget()
        matplotlibwidget_dynamic.setEnabled(True)
        matplotlibwidget_dynamic.setGeometry(QtCore.QRect(10, 0, 611, 271))
        matplotlibwidget_dynamic.setObjectName("matplotlibwidget_dynamic")

        self.stack.addWidget(matplotlibwidget_dynamic)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(670, 370, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.stack.show()
        # window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "显示静态图"))
        self.pushButton_2.setText(_translate("MainWindow", "显示动态图"))

    def next(self):
        self.stack.setCurrentIndex(self.stack.currentIndex() + 1)
        print('current', self.stack.currentIndex())

from MatplotlibWidget import MatplotlibWidget
