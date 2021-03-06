# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindowFrom.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(788, 516)

        # 主界面 toolabr 和 图像都放在上面
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_widget = QtWidgets.QWidget(self.centralwidget)



        self.main_widget.setGeometry(QtCore.QRect(20, 10, 701, 471))
        self.main_widget.setObjectName("main_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # toolbar区域
        self.toolbar_stackedWidget = QtWidgets.QStackedWidget(self.main_widget)
        self.toolbar_stackedWidget.setObjectName("toolbar_stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # 在toolbar区域存放的按钮
        self.reset_Button = QtWidgets.QPushButton(self.page)
        self.reset_Button.setObjectName("reset_Button")
        self.horizontalLayout.addWidget(self.reset_Button)
        self.reset_Button.setIcon(QIcon("images/button_icon/home.png"))

        self.forward_Button = QtWidgets.QPushButton(self.page)
        self.forward_Button.setObjectName("forward_Button")
        self.horizontalLayout.addWidget(self.forward_Button)
        self.forward_Button.setIcon(QIcon("images/button_icon/forward.png"))


        self.back_Button = QtWidgets.QPushButton(self.page)
        self.back_Button.setObjectName("back_Button")
        self.horizontalLayout.addWidget(self.back_Button)
        self.back_Button.setIcon(QIcon("images/button_icon/back.png"))

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.pan_pushButton = QtWidgets.QPushButton(self.page)
        self.pan_pushButton.setObjectName("pan_pushButton")
        self.horizontalLayout.addWidget(self.pan_pushButton)
        self.pan_pushButton.setIcon(QIcon("images/button_icon/pan.png"))

        self.zoom_pushButton = QtWidgets.QPushButton(self.page)
        self.zoom_pushButton.setObjectName("zoom_pushButton")
        self.horizontalLayout.addWidget(self.zoom_pushButton)
        self.zoom_pushButton.setIcon(QIcon("images/button_icon/zoom.png"))

        self.save_pushButton = QtWidgets.QPushButton(self.page)
        self.save_pushButton.setObjectName("save_pushButton")
        self.save_pushButton.setIcon(QIcon("images/button_icon/save.png"))
        self.horizontalLayout.addWidget(self.save_pushButton)

        self.toolbar_stackedWidget.addWidget(self.page)
        self.verticalLayout.addWidget(self.toolbar_stackedWidget)

        # 图像放置区域
        self.stack_tabWidget = QtWidgets.QTabWidget(self.main_widget)
        self.stack_tabWidget.setObjectName("stack_tabWidget")
        self.verticalLayout.addWidget(self.stack_tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        # 菜单栏
        self.main_menubar = QtWidgets.QMenuBar(MainWindow)
        self.main_menubar.setGeometry(QtCore.QRect(0, 0, 788, 23))
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
        # self.plot_save_action = QtWidgets.QAction(MainWindow)
        # self.plot_save_action.setObjectName("plot_save_action")
        # # self.plot_save_action.setShortcuts("")
        #
        # self.file_menu.addAction(self.plot_save_action)
        self.main_menubar.addAction(self.menu.menuAction())
        self.main_menubar.addAction(self.file_menu.menuAction())
        self.main_menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        self.stack_tabWidget.setCurrentIndex(0)

        # 主界面布局
        wlayout = QtWidgets.QVBoxLayout()

        wlayout.addWidget(self.toolbar_stackedWidget)
        wlayout.addWidget(self.stack_tabWidget)
        # wlayout.addWidget(self.toolbar_stackedWidget)

        self.centralwidget.setLayout(wlayout)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "曲线翻页"))
        self.reset_Button.setText(_translate("MainWindow", "图像"))
        self.forward_Button.setText(_translate("MainWindow", "前一步"))
        self.back_Button.setText(_translate("MainWindow", "后一步"))
        self.pan_pushButton.setText(_translate("MainWindow", "选中"))
        self.zoom_pushButton.setText(_translate("MainWindow", "放大"))
        self.save_pushButton.setText(_translate("MainWindow", "保存"))

        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.file_menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_3.setTitle(_translate("MainWindow", "状态"))
        # self.plot_save_action.setText(_translate("MainWindow", "保存图片"))

