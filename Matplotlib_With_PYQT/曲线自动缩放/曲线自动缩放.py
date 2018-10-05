# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindowFrom.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(931, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_widget = QtWidgets.QWidget(self.centralwidget)
        self.main_widget.setGeometry(QtCore.QRect(30, 10, 861, 531))
        self.main_widget.setObjectName("main_widget")
        self.stack_tabWidget = QtWidgets.QTabWidget(self.main_widget)
        self.stack_tabWidget.setGeometry(QtCore.QRect(30, 100, 821, 401))
        self.stack_tabWidget.setObjectName("stack_tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.stack_tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.stack_tabWidget.addTab(self.tab_2, "")
        self.toolbar_stackedWidget = QtWidgets.QStackedWidget(self.main_widget)
        self.toolbar_stackedWidget.setGeometry(QtCore.QRect(30, 20, 791, 71))
        self.toolbar_stackedWidget.setObjectName("toolbar_stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.toolbar_stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.toolbar_stackedWidget.addWidget(self.page_2)

        self.save_pushButton = QtWidgets.QPushButton(self.main_widget)
        self.save_pushButton.setGeometry(QtCore.QRect(690, 500, 75, 23))
        self.save_pushButton.setObjectName("save_pushButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.main_menubar = QtWidgets.QMenuBar(MainWindow)
        self.main_menubar.setGeometry(QtCore.QRect(0, 0, 931, 23))
        self.main_menubar.setObjectName("main_menubar")
        self.menu = QtWidgets.QMenu(self.main_menubar)
        self.menu.setObjectName("menu")
        self.file_menu = QtWidgets.QMenu(self.main_menubar)
        self.file_menu.setObjectName("file_menu")
        self.menu_3 = QtWidgets.QMenu(self.main_menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.main_menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.plot_save_action = QtWidgets.QAction(MainWindow)
        self.plot_save_action.setObjectName("plot_save_action")
        self.file_menu.addAction(self.plot_save_action)
        self.main_menubar.addAction(self.menu.menuAction())
        self.main_menubar.addAction(self.file_menu.menuAction())
        self.main_menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "曲线翻页"))
        self.stack_tabWidget.setTabText(self.stack_tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.stack_tabWidget.setTabText(self.stack_tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.save_pushButton.setText(_translate("MainWindow", "点击保存"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.file_menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_3.setTitle(_translate("MainWindow", "状态"))
        self.plot_save_action.setText(_translate("MainWindow", "保存图片"))

