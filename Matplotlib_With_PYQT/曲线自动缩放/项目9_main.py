import sys
import random
import matplotlib

matplotlib.use("Qt5Agg")
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QSizePolicy, QAction,
                             QWidget,QStackedWidget, QPushButton,QTabWidget, QAction, QMessageBox,QFileDialog)
# from PyQt5.Con import QFarme
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from Winform import Winform
from MatploWidget import MatplotlibWidget
from MatploWidget import MyMplCanvas
from utils import log

# 加载数据
from loadlines import load_all_lines

# 添加曲线到画布上
from ZoomCurve import chose_color
from ZoomCurve import find_inflection_point
from ZoomCurve import get_zoomed_x_axes_limts


'''

pyqt主窗体有
菜单栏、-->
    1.添加保存图像  功能失败
    2.matplotlib与菜单栏重合
    
工具栏、--> matplotlib自带的的toolbar重合
主窗体区，--> 未做到 
状态栏 --> 未做到
pyqt主窗体的主窗体区有2个分页，每个分页中都绘制一个matplotlib图形，第一个绘制正弦，第二绘制余弦；
点击菜单栏某个菜单后，能够保存当前分页中的matplotlib图形；
点击工具栏某个命令按钮后，，能够保存当前分页中的matplotlib图形；
菜单栏和工具栏都支持快捷键操作；
基础：matplotlib+pyqt
思路：网上/书上找代码，并实验和总结

'''
# class MyMatpolowidget(MatplotlibWidget):
#
#
#
#     def center(self):
#         # 设置matplotlib窗口在屏幕中间


# 创建主窗口
class MinWindow(Winform):
    def __init__(self, parent=None):
        super(MinWindow, self).__init__(parent)

        self.setWindowTitle('主窗口')
        self.resize(900, 600)
        self.center()
        self.create_main_frame()
        self.create_menu()
        # self.create_status_bar()
        self.set_all_tab()
        self.retranslateUi()
        # self.btn1 = QPushButton("Button1")
        # self.btn1.setCheckable(True)
        # self.btn1.toggle()
        # self.btn1.clicked.connect(lambda: self.whichbtn(self.btn1))
        # self.btn1.clicked.connect(self.btnstate)
        # self.addWidget(self.btn1)

    def save_plot(self):
        # 保存当前matplotlib图像
        file_choices = "PNG (*.png)|*.png"

        path = QFileDialog.getSaveFileName(self,
                                           'Save file', '',
                                           file_choices)
        if path:
            self.canvas.print_figure(path, dpi=self.dpi)
            self.statusBar().showMessage('Saved to %s' % path, 2000)

        pass

    def create_menu(self):
        # 添加菜单栏
        # print('运行到这里了')
        self.file_menu = self.menuBar().addMenu("&File")

        plot_file_action = self.create_action("&Save plot",
                                              shortcut="Ctrl+S", slot=self.save_plot,
                                              tip="Save the plot")
        quit_action = self.create_action("&Quit", slot=self.close,
                                         shortcut="Ctrl+Q", tip="Close the application")

        self.add_actions(self.file_menu,
                         (plot_file_action, None, quit_action))

        self.help_menu = self.menuBar().addMenu("&Help")
        about_action = self.create_action("&About",
                                          shortcut='F1', slot=self.on_about,
                                          tip='About the demo')

        self.add_actions(self.help_menu, (about_action,))


        # self.tab = QtWidgets.QWidget()
        # self.tab.setObjectName("tab")
        # self.stack_tabWidget.addTab(self.tab, "")
        #
        # self.tab_2 = QtWidgets.QWidget()
        # self.tab_2.setObjectName("tab_2")
        # self.stack_tabWidget.addTab(self.tab_2, "")

        self.main_menubar = QtWidgets.QMenuBar()
        self.main_menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.main_menubar.setObjectName("main_menubar")

        self.menu = QtWidgets.QMenu(self.main_menubar)
        self.menu.setObjectName("menu")
        self.file_menu = QtWidgets.QMenu(self.main_menubar)
        self.file_menu.setObjectName("file_menu")

        self.menu_3 = QtWidgets.QMenu(self.main_menubar)
        self.menu_3.setObjectName("menu_3")

        self.setMenuBar(self.main_menubar)

        # 状态栏
        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setObjectName("statusbar")

        self.setStatusBar(self.statusbar)

        # self.plot_save_action = QtWidgets.QAction("&Save plot",
        #                                       shortcut="Ctrl+S", slot=self.save_plot)
        # self.plot_save_action.setObjectName("plot_save_action")



        save_file_action = self.create_action("&Save plot",
                                              shortcut="Ctrl+S", slot=self.save_plot,
                                              tip="Save the plot")
        quit_action = self.create_action("&Quit", slot=self.close,
                                         shortcut="Ctrl+Q", tip="Close the application")

        self.add_actions(self.file_menu,
                         (save_file_action, None, quit_action))


        # self.file_menu.addAction(self.plot_save_action)
        # self.main_menubar.addAction(self.menu.menuAction())
        # self.main_menubar.addAction(self.file_menu.menuAction())
        # self.main_menubar.addAction(self.menu_3.menuAction())
        # print('运行到这里了')
        pass

    def create_main_frame(self):
        self.setObjectName("MainWindow")

        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)

        self.main_widget = QtWidgets.QWidget(self.centralwidget)
        self.main_widget.setGeometry(QtCore.QRect(10, 20, 761, 481))
        self.main_widget.setObjectName("main_widget")

        self.stack_tabWidget = QtWidgets.QTabWidget(self.main_widget)
        self.stack_tabWidget.setGeometry(QtCore.QRect(30, 60, 721, 401))
        self.stack_tabWidget.setObjectName("stack_tabWidget")

    def main_frame_center(self):
        screen = self.ui.parent.screenGeometry()
        size = self.geometry()
        # print("wid ({}) heih({})".format(screen.width(),  size.width()))
        # self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
        pass

    def create_status_bar(self):

        pass

    def add_actions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)

    def create_action(self, text, slot=None, shortcut=None,
                      icon=None, tip=None, checkable=False,
                      signal="triggered()"):
        action = QAction(text, self)
        if icon is not None:
            # action.setIcon(QIcon(":/%s.png" % button_icon))
            pass
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            action.triggered.connect(slot)
        if checkable:
            action.setCheckable(True)
        return action

    def on_about(self):
        msg = """ A demo of using PyQt with matplotlib:

         * Use the matplotlib navigation bar
         * Add values to the text box and press Enter (or click "Draw")
         * Show or hide the grid
         * Drag the slider to modify the width of the bars
         * Save the plot to a file using the File menu
         * Click on a bar to receive an informative message
        """
        QMessageBox.about(self, "About the demo", msg.strip())

    def on_draw(self):
        # self.retranslateUi(Winform)
        # QtCore.QMetaObject.connectSlotsByName(Winform)
        pass
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        self.setWindowTitle(_translate("MainWindow", "曲线翻页"))

        # self.stack_tabWidget.setTabText(self.stack_tabWidget.indexOf(self.tab1), _translate("MainWindow", "Tab 1"))
        # self.stack_tabWidget.setTabText(self.stack_tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 2"))

        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.file_menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_3.setTitle(_translate("MainWindow", "状态"))
        self.plot_save_action.setText(_translate("MainWindow", "保存图片"))

    def set_all_tab(self):

        # self.layout = QVBoxLayout(self)

        # 创建matplot画布
        self.tab1 = MyMplCanvas(self, width=9, height=6, dpi=100)
        self.tab2 = MyMplCanvas(self, width=9, height=6, dpi=100)
        self.tab3 = MyMplCanvas(self, width=9, height=6, dpi=100)
        # mpl.draw_one_line()

        # 加载数据
        # 在不同的画布上画出来
        # 将所有f分页加入到tabWidget上
        lines = load_all_lines()

        self.tab1.draw_one_line(lines[0])
        self.tab2.draw_one_line(lines[1])
        self.tab3.draw_one_line(lines[2])

        self.stack_tabWidget.addTab(self.tab1, 'td=0.12')
        self.stack_tabWidget.addTab(self.tab2, 'td=0.144')
        self.stack_tabWidget.addTab(self.tab3, 'td=0.176')

        self.tab1_ntb = NavigationToolbar(self.tab1, self)  # 添加完整的 toolbar
        self.tab1_UI()
        self.tab2_UI()

        pass

    def tab1_UI(self):
        pass

    def tab2_UI(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MinWindow()
    win.show()
    sys.exit(app.exec_())




