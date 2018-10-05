import sys
import os
import random
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("Qt5Agg")

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QSizePolicy, QAction, QLabel,
                             QWidget,QStackedWidget, QPushButton,QTabWidget, QAction, QMessageBox, QFileDialog, QHBoxLayout)
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from MatploWidget import MatplotlibWidget

# qt绘制matplotlib图像的类
from MatploWidget import PlotCanvas
# 弹出为屏幕中心主窗口
from MainForm import Ui_MainWindow
from mainWindowFrom import Ui_MainWindow
from utils import log

# 加载数据
from loadlines import load_all_lines

# 添加曲线到画布上
from ZoomCurve import chose_color
from ZoomCurve import find_inflection_point
from ZoomCurve import get_zoomed_x_axes_limts
from PyQt5.QtWidgets import QDesktopWidget, QApplication, QMainWindow, QPushButton


'''
1.绘制matplotlib图像的类是PlotCanvas   --> 所有图像放到QtabWigdet里面
2.
pyqt主窗体的主窗体 QtabWigdet 区有2个分页，每个分页中都绘制一个matplotlib图形，第一个绘制正弦，第二绘制余弦；
点击菜单栏  QstackWigdet  某个菜单后，能够保存当前分页中的matplotlib图形；
点击工具栏某个命令按钮后，，能够保存当前分页中的matplotlib图形；--> 保存用的matplotlib toolbar自带的保存函数
菜单栏和工具栏都支持快捷键操作；

'''
# class MyMatpolowidget(MatplotlibWidget):
#   按钮绑定事件
#
#
#     def center(self):
#         # 设置matplotlib窗口在屏幕中间 


class MinWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MinWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.setupUi(self)
        self.center()
        self.on_draw()
        self.load_event()

    def on_draw(self):
        self.draw_all_stack_tab()
        self.set_all_stack_tab_toolbar()
        pass

    def load_event(self):
        self.event_with_buttons()
        pass

    def draw_all_stack_tab(self):
        # 绘制所有图像
        # 添加到stack_tabWidget上

        # 创建matplot画布
        self.tab1 = PlotCanvas(self, width=9, height=6, dpi=100)
        self.tab2 = PlotCanvas(self, width=9, height=6, dpi=100)
        self.tab3 = PlotCanvas(self, width=9, height=6, dpi=100)
        # mpl.draw_one_line()

        # 加载数据
        # 在不同的画布上画出来
        # 将所有f分页加入到tabWidget上
        lines = load_all_lines()

        self.tab1.draw_one_line(lines[0])
        self.tab2.draw_one_line(lines[1])
        self.tab3.draw_one_line(lines[2])

        # 将所有的tab添加到stack_tabWidget上
        self.ui.stack_tabWidget.addTab(self.tab1, 'td=0.12')
        self.ui.stack_tabWidget.addTab(self.tab2, 'td=0.144')
        self.ui.stack_tabWidget.addTab(self.tab3, 'td=0.176')
        pass

    def set_all_stack_tab_toolbar(self):
        # 添加图像的工具栏 所有的工具栏用容器toolbar_stackedWidget保存
        self.tab1_ntb = NavigationToolbar(self.tab1, self.ui.page)  # 添加完整的 toolbar
        self.tab2_ntb = NavigationToolbar(self.tab2, self.ui.page)  # 添加完整的 toolbar
        self.tab3_ntb = NavigationToolbar(self.tab3, self.ui.page)  # 添加完整的 toolbar

        self.tab1.mpl_nav_toolbar = self.tab1_ntb
        self.tab2.mpl_nav_toolbar = self.tab2_ntb
        self.tab3.mpl_nav_toolbar = self.tab3_ntb
        # log('设置了的')
        # 隐藏当前的toolbar
        self.tab1_ntb.hide()
        self.tab2_ntb.hide()
        self.tab3_ntb.hide()

    def set_button_tip(self, button, tip=None):
        # 设置左下角显示button 的提示
        if tip is not None:
            button.setToolTip(tip)
            button.setStatusTip(tip)
        pass

    def event_with_buttons(self):
        # button绑定事件
        # self.ui.reset_Button.clocked()
        # 点击按钮 保存当前图像
        self.ui.save_pushButton.clicked.connect(self.toolbar_save_plot)

        self.ui.reset_Button.clicked.connect(self.toolbar_home)

        self.ui.forward_Button.clicked.connect(self.toolbar_forward)

        self.ui.back_Button.clicked.connect(self.toolbar_back)
        self.ui.zoom_pushButton.clicked.connect(self.toolbar_zoom)
        self.ui.pan_pushButton.clicked.connect(self.toolbar_pan)

        self.set_button_tip(self.ui.save_pushButton, '点击保存 快捷键Ctrl + S')
        self.set_button_tip(self.ui.reset_Button, '显示图像最初的样子')

        self.set_button_tip(self.ui.forward_Button, '返回上一步图像')
        self.set_button_tip(self.ui.back_Button, '返回下一步图像')
        self.set_button_tip(self.ui.zoom_pushButton, '选中放大图像')
        self.set_button_tip(self.ui.pan_pushButton, '选中图像 可拖动查看细节')



        # 给菜单按钮添加绑定事件
        # QtCore.QMetaObject.connectSlotsByName(self)
        save_file_action = self.create_action("&保存图像",
                                              shortcut="Ctrl+S", slot=self.toolbar_save_plot,
                                              tip="Save the plot")
        quit_action = self.create_action("&Quit", slot=self.close,
                                         shortcut="Ctrl+Q", tip="Close the application")

        self.add_actions(self.ui.file_menu,
                         (save_file_action, None, quit_action))
        pass

    def toolbar_set_curt(self):
        # self.ui.stack_tabWidget.currentWidget().mpl_nav_toolbar

        pass

    def create_action(self, text, slot=None, shortcut=None,
                      icon=None, tip=None, checkable=False,
                      signal="triggered()"):
        # 创建事件
        action = QAction(text, self)
        if icon is not None:
            # action.setIcon(QIcon(":/%s.png" % button_icon))
            pass
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            # bottons = QPushButton(text, self)
            # bottons.setti
            action.setStatusTip(tip)
        if slot is not None:
            action.triggered.connect(slot)
        if checkable:
            action.setCheckable(True)
        return action

    def add_actions(self, target, actions):
        # 添加事件
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)

    def center(self):
        # 设置主窗口在屏幕中间
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        # from utils import log
        # log('screen.width ({})  size.width({})'.format(screen.width(), size.width()))
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def toolbar_save_plot(self):
        # 保存当前图像
        log('点击了保存')
        # 给button设置tips

        self.ui.stack_tabWidget.currentWidget().mpl_nav_toolbar.save_figure()
        # log('点击了保存啊')
        pass

    def toolbar_zoom(self):
        # 放大当前图像
        log('点击了放大')
        self.ui.stack_tabWidget.currentWidget().mpl_nav_toolbar.zoom()

    def toolbar_back(self):
        # 显示前一步操作的图像
        log("点击了前进")
        self.ui.stack_tabWidget.currentWidget().mpl_nav_toolbar.back()

    def toolbar_forward(self):
        # 显示前一步操作的图像
        log("点击了上一步")
        self.ui.stack_tabWidget.currentWidget().mpl_nav_toolbar.forward()

    def toolbar_edit_parameters(self):
        # 编辑图像的参数

        self.ui.stack_tabWidget.currentWidget().mpl_nav_toolbar.edit_parameters()

    def toolbar_pan(self):
        #
        self.ui.stack_tabWidget.currentWidget().mpl_nav_toolbar.pan()

    def toolbar_edit_parameters(self):
        self.ui.stack_tabWidget.currentWidget().mpl_nav_toolbar.edit_parameters()

    def toolbar_home(self):
        log('点击了重置')
        self.ui.stack_tabWidget.currentWidget().mpl_nav_toolbar.home()


'''
1.mtplotlib完全显示
2.保存图像的函数
'''
if __name__ == "__main__":
    # app = QApplication(sys.argv)
    # win = MinWindow()
    # win.show()
    # sys.exit(app.exec_())
    app = QApplication(sys.argv)
    win = MinWindow()
    win.show()
    sys.exit(app.exec_())



