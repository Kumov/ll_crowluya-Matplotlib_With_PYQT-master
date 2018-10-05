from __future__ import print_function

import sys

import numpy as np
from PyQt5 import *
from matplotlib.figure import Figure
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
# from matplotlib.backends import qt5_compat
from matplotlib.backends import qt_compat




import sys
import matplotlib
import PyQt5.sip
from matplotlib.backend_bases import key_press_handler

matplotlib.use("Qt5Agg")

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QSizePolicy, QAction, QLabel,
                             QWidget,QStackedWidget, QPushButton,QTabWidget, QAction, QMessageBox, QFileDialog, QHBoxLayout)
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
#
# from MatploWidget import PlotCanvas  # qt绘制matplotlib图像的类
# from mainWindowFrom import Ui_MainWindow  # 弹出为屏幕中心主窗口
# from loadlines import load_all_lines  # 加载数据
# 添加曲线到画布上
from PyQt5.QtWidgets import QDesktopWidget, QApplication, QMainWindow, QPushButton
from utils import log


use_pyside = qt_compat.QT_API == qt_compat.QT_API_PYSIDE

# if use_pyside:
#     from PySide.QtCore import *
#     from PySide.QtGui import *
# else:
#     from PyQt5.QtCore import *
#     from PyQt5.QtGui import *


class AppForm(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        #self.x, self.y = self.get_data()
        self.data = self.get_data2()
        self.create_main_frame()
        self.on_draw()

    def create_main_frame(self):
        self.main_frame = QWidget()

        self.fig = Figure((5.0, 4.0), dpi=100)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.main_frame)
        self.canvas.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.canvas.setFocus()

        self.mpl_toolbar = NavigationToolbar(self.canvas, self.main_frame)

        self.canvas.mpl_connect('key_press_event', self.on_key_press)

        vbox = QVBoxLayout()
        vbox.addWidget(self.canvas)  # the matplotlib canvas
        vbox.addWidget(self.mpl_toolbar)
        self.main_frame.setLayout(vbox)
        self.setCentralWidget(self.main_frame)

    def get_data2(self):
        return np.arange(20).reshape([4, 5]).copy()

    def on_draw(self):
        self.fig.clear()
        self.axes = self.fig.add_subplot(111)
        #self.axes.plot(self.x, self.y, 'ro')
        self.axes.imshow(self.data, interpolation='nearest')
        #self.axes.plot([1,2,3])
        self.canvas.draw()

    def on_key_press(self, event):
        print('you pressed', event.key)
        # implement the default mpl key press events described at
        # http://matplotlib.org/users/navigation_toolbar.html#navigation-keyboard-shortcuts
        key_press_handler(event, self.canvas, self.mpl_toolbar)


def main():
    app = QApplication(sys.argv)
    form = AppForm()
    form.show()
    app.exec_()

if __name__ == "__main__":
    main()