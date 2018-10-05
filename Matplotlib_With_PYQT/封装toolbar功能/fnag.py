import sys
import matplotlib
import PyQt5.sip

# matplotlib的键盘按压事件引入到pyqt5中
# from matplotlib.backend_bases import key_press_handler

matplotlib.use("Qt5Agg")

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QSizePolicy, QAction, QLabel,
                             QWidget,QStackedWidget, QPushButton,QTabWidget, QAction, QMessageBox, QFileDialog, QHBoxLayout)
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

import  matplotlib.pyplot as plt
from MatploWidget import PlotCanvas  # qt绘制matplotlib图像的类
from mainFrom import Ui_MainWindow  # 弹出为屏幕中心主窗口
from loadlines import load_all_lines  # 加载数据
# 添加曲线到画布上
from PyQt5.QtWidgets import QDesktopWidget, QApplication, QMainWindow, QPushButton

from utils import log
# from MatploWidget import PlotCanvas



fig = plt.figure()
ax = fig.add_subplot(111)

lines = load_all_lines()

tab1 = PlotCanvas(width=9, height=6, dpi=100)

tab1.draw_one_line(lines[0])
# fig.add_subplot(tab1)

tab1.draw()
# plt.show()