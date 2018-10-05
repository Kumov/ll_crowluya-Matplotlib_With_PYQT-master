import sys
import random
import matplotlib

from PyQt5.QtWidgets import QDesktopWidget, QApplication, QMainWindow
import sys
matplotlib.use("Qt5Agg")
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QSizePolicy, QWidget,QStackedWidget
# from PyQt5.Con import QFarme
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

# 1.创建主窗口

# 2.在主窗口上添加QStackedWidget
# 3.在QStackedWidget上分别添加widget
from Winform import Winform

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Winform()
    win.show()
    sys.exit(app.exec_())