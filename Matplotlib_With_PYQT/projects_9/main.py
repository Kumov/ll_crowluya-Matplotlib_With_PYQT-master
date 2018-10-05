import sys
import os
import random
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("Qt5Agg")

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QSizePolicy, QAction, QLabel,
                             QWidget,QStackedWidget, QPushButton,QTabWidget, QAction, QMessageBox, QFileDialog)
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from MatploWidget import MatplotlibWidget

# qt绘制matplotlib图像的类
from MatploWidget import PlotCanvas
# 弹出为屏幕中心主窗口
from Winform import Winform

from utils import log

# 加载数据
from loadlines import load_all_lines

# 添加曲线到画布上
from ZoomCurve import chose_color
from ZoomCurve import find_inflection_point
from ZoomCurve import get_zoomed_x_axes_limts


'''
1.绘制matplotlib图像的类是PlotCanvas   --> 所有图像放到QtabWigdet里面
2.
pyqt主窗体的主窗体 QtabWigdet 区有2个分页，每个分页中都绘制一个matplotlib图形，第一个绘制正弦，第二绘制余弦；
点击菜单栏  QstackWigdet  某个菜单后，能够保存当前分页中的matplotlib图形；
点击工具栏某个命令按钮后，，能够保存当前分页中的matplotlib图形；--> 保存用的matplotlib toolbar自带的保存函数
菜单栏和工具栏都支持快捷键操作；

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

        # 创建主窗口
        self.create_main_frame()
        self.add_button()
        # 创建菜单
        self.create_menu()
        # 画出图像
        self.on_draw()

        # 绑定所有事件
        self.events_all_siganl_connect()

    def save_plot(self):
        # 保存当前matplotlib图像
        file_choices = "PNG (*.png)|*.png"

        # path = QFileDialog.getSaveFileName(self,
        #                                    'Save file', '',
        #                                    file_choices)
        # path = self.get_current_path()
        self.stack_tabWidget.currentWidget().mpl_nav_toolbar.save_figure()

        # if path:
        #     print('保存啊')
        #     # self.stack_tabWidget.currentWidget()
        #     self.stack_tabWidget.currentWidget().mpl_nav_toolbar.save_figure()
        #     print('保存了啊')
        #     self.statusBar().showMessage('Saved to %s' % path, 2000)

        pass

    def create_menu(self):
        # 添加菜单栏

        self.setCentralWidget(self.centralwidget)

        # 添加菜单栏
        self.main_menubar = QtWidgets.QMenuBar()
        self.main_menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.main_menubar.setObjectName("main_menubar")

        self.menu = QtWidgets.QMenu(self.main_menubar)
        self.menu.setObjectName("menu")
        self.file_menu = QtWidgets.QMenu(self.main_menubar)
        self.file_menu.setObjectName("file_menu")

        self.save_menu = QtWidgets.QMenu(self.main_menubar)
        self.save_menu.setObjectName("save_menu")

        self.setMenuBar(self.main_menubar)

        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setObjectName("statusbar")

        self.setStatusBar(self.statusbar)

        # 添加状态栏
        self.show_status_bar()
        # self.statusbar.showMessage("这是状态栏")

        self.plot_save_action = QAction(self)
        self.plot_save_action.setObjectName("plot_save_action")

        _translate = QtCore.QCoreApplication.translate
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.file_menu.setTitle(_translate("MainWindow", "保存"))
        self.save_menu.setTitle(_translate("MainWindow", "保存图片"))
        self.plot_save_action.setText(_translate("MainWindow", "保存图片"))

        self.file_menu.addAction(self.plot_save_action)
        self.main_menubar.addAction(self.menu.menuAction())
        self.main_menubar.addAction(self.file_menu.menuAction())
        self.main_menubar.addAction(self.save_menu.menuAction())

        self.retranslateUi()

        # 给菜单按钮添加绑定事件
        # QtCore.QMetaObject.connectSlotsByName(self)
        save_file_action = self.create_action("&保存图像",
                                              shortcut="Ctrl+S", slot=self.save_plot,
                                              tip="Save the plot")
        quit_action = self.create_action("&Quit", slot=self.close,
                                         shortcut="Ctrl+Q", tip="Close the application")

        self.add_actions(self.file_menu,
                         (save_file_action, None, quit_action))
        pass

    def create_main_frame(self):
        # 窗口布局
        # 添加主窗口
        self.setObjectName("MainWindow")
        # self.layout =
        self.layout = QVBoxLayout(self)
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)

        self.main_widget = QtWidgets.QWidget(self.centralwidget)
        self.main_widget.setGeometry(QtCore.QRect(10, 20, 761, 481))
        self.main_widget.setObjectName("main_widget")

        # 此区域存放图像
        self.stack_tabWidget = QtWidgets.QTabWidget(self.main_widget)
        self.stack_tabWidget.setGeometry(QtCore.QRect(30, 60, 721, 401))
        self.stack_tabWidget.setObjectName("stack_tabWidget")

        # 此区域存放图像的工具栏
        self.toolbar_stackedWidget = QStackedWidget(self.main_widget)
        self.toolbar_stackedWidget.setGeometry(QtCore.QRect(20, 0, 791, 71))
        self.toolbar_stackedWidget.setObjectName("toolbar_stackedWidget")
        self.layout.addWidget(self.centralwidget)

    def on_draw(self):
        # 添加图像
        self.draw_all_stack_tab()
        # 添加工具栏
        self.set_all_stack_tab_toolbar()
        pass

    def create_status_bar(self):

        pass

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

    def add_actions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)

    def add_button(self):
        self.save_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.save_pushButton.setGeometry(QtCore.QRect(800, 160, 75, 23))
        self.save_pushButton.setObjectName("save_pushButton")
        pass

    def on_about(self):
        # 弹出关于此软件的信息
        msg = """ A demo of using PyQt with matplotlib:

         * Use the matplotlib navigation bar
         * Add values to the text box and press Enter (or click "Draw")
         * Show or hide the grid
         * Drag the slider to modify the width of the bars
         * Save the plot to a file using the File menu
         * Click on a bar to receive an informative message
        """
        QMessageBox.about(self, "About the demo", msg.strip())

    def retranslateUi(self):
        # 设置各个菜单的名字
        _translate = QtCore.QCoreApplication.translate

        self.setWindowTitle(_translate("MainWindow", "曲线翻页"))

        # self.stack_tabWidget.setTabText(self.stack_tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        # self.stack_tabWidget.setTabText(self.stack_tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))

        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.file_menu.setTitle(_translate("MainWindow", "保存"))
        self.save_menu.setTitle(_translate("MainWindow", "状态"))
        self.plot_save_action.setText(_translate("MainWindow", "保存图片"))
        self.save_pushButton.setText(_translate("MainWindow", "点击保存"))

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
        self.stack_tabWidget.addTab(self.tab1, 'td=0.12')
        self.stack_tabWidget.addTab(self.tab2, 'td=0.144')
        self.stack_tabWidget.addTab(self.tab3, 'td=0.176')
        pass

    def set_all_stack_tab_toolbar(self):
        # 添加图像的工具栏 所有的工具栏用容器toolbar_stackedWidget保存
        self.add_stack_toolbar()
        self.tab1_ntb = NavigationToolbar(self.tab1, self.toolbar_page1)  # 添加完整的 toolbar
        self.tab2_ntb = NavigationToolbar(self.tab2, self.toolbar_page2)  # 添加完整的 toolbar
        self.tab3_ntb = NavigationToolbar(self.tab3, self.toolbar_page3)  # 添加完整的 toolbar

        self.tab1.mpl_nav_toolbar = self.tab1_ntb
        self.tab2.mpl_nav_toolbar = self.tab2_ntb
        self.tab3.mpl_nav_toolbar = self.tab3_ntb
        # log('设置了的')
        pass

    def show_status_bar(self):
        # 添加状态栏
        self.status_text = QLabel(" demo 状态栏")
        self.statusbar.addWidget(self.status_text, 1)

    def add_stack_toolbar(self):
        # 添加matplotlib的工具栏
        # toolbar_stackedWidget

        # 创建QStackedWidget容器 将matplotlib所有图像的工具栏叠加放在一起
        # self.toolbar_stackedWidget = QStackedWidget()

        # 创建不同的 QWidget保存单个matplotlib图像的工具栏
        self.toolbar_page1 = QtWidgets.QWidget()
        self.toolbar_page1.setObjectName("toolbar_page1")

        self.toolbar_page2 = QtWidgets.QWidget()
        self.toolbar_page2.setObjectName("toolbar_page2")

        self.toolbar_page3 = QtWidgets.QWidget()
        self.toolbar_page3.setObjectName("toolbar_page3")

        # 初始化空白toolbar区域
        # 添加三个空页
        self.toolbar_stackedWidget.addWidget(self.toolbar_page1)
        self.toolbar_stackedWidget.addWidget(self.toolbar_page2)
        self.toolbar_stackedWidget.addWidget(self.toolbar_page3)

        pass

    def events_all_siganl_connect(self):
        # 连接所有的事件

        # 切换tabWidget图像 显示 当前图像的toolbar
        self.stack_tabWidget.currentChanged.connect(self.event_change_toolbar_page)

        # 点击按钮 保存当前图像
        self.save_pushButton.clicked.connect(self.save_plot)

        pass

    def event_change_toolbar_page(self):
        # 切换当前td图像触发
        # 在toolbar_stackedWidget区域显示当前图像的matplotlib工具栏

        # 获取当前的tab
        # log('点击了当前的widget')
        c = self.stack_tabWidget.currentIndex()
        # 设置当前stackWidget的当前
        self.toolbar_stackedWidget.setCurrentIndex(c)
        # log("toolbar_stackedWidget 当前页面是({})".format(c))
        # 设置当前的tool stackWidget的page
        pass

    def get_current_path(self):
        # 获取当前文件目录
        paths = sys.path
        current_file = os.path.basename(__file__)
        for path in paths:
            try:
                if current_file in os.listdir(path):
                    self.current_path = path
                    break
            except (FileExistsError,FileNotFoundError) as e:
                print(e)

'''
1.mtplotlib完全显示
2.保存图像的函数
'''
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MinWindow()
    win.show()
    sys.exit(app.exec_())




