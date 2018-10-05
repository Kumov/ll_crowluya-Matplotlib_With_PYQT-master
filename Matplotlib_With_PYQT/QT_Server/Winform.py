# -*- coding: utf-8 -*-

'''
    【简介】
	PyQT5将窗口放在屏幕中间例子
    
'''

from PyQt5.QtWidgets import QDesktopWidget, QApplication, QMainWindow, QPushButton
import sys


class Winform(QMainWindow):

    def __init__(self, parent=None):
        super(Winform, self).__init__(parent)

        self.setWindowTitle('主窗口')
        self.resize(900, 600)
        self.center()
        # self.btn1 = QPushButton("Button1")
        # self.btn1.setCheckable(True)
        # self.btn1.toggle()
        # self.btn1.clicked.connect(lambda: self.whichbtn(self.btn1))
        # self.btn1.clicked.connect(self.btnstate)
        # self.addWidget(self.btn1)

    def center(self):
        # 设置主窗口在屏幕中间
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    # 创建菜单

# 创建窗口


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Winform()
    win.show()
    sys.exit(app.exec_())
