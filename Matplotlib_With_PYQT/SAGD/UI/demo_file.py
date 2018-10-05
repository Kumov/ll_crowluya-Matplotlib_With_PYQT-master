import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QDialog

from UI_Factory import Ui_MainWindow
from UI_Factory import  Widget_Thermophysical # 热物性参数
from UI_Factory import Widget_Oil_para # 油藏参数
from UI_Factory import Widget_basic_Paras2 # 基本参数2
from UI_Factory import Widget_fragment  # 分段参数

log =  print


class MinUIWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MinUIWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.setupUi(self)
        # self.center()
        # self.on_draw()
        # self.load_event()
        self.singal_connect_all()

    def singal_connect_all(self):
        # 绑定所有的信号函数
        # self.top_menu_help.addAction('&关于', self.about_Handle,
        #                              QtCore.Qt.CTRL + QtCore.Qt.Key_H)
        self.ui.action_SAGD_add_paras.triggered.connect(self.show_Widget_Oil)

    def show_Widget_Oil(self):
        # from ..Function.utils import log
        # log(" show _wight")
        print(" 触发了 MinUIWindow show_Widget_Oil")

        # 显示弹窗
        self.dialog = Widget_Oil_para(self)
        # 设置或显示数据
        self.dialog.show()
        self.dialog.set_value()



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # self.action_about.triggered.connect(self.help_window)
        self.singal_connect_all()

    def singal_connect_all(self):
        # 绑定所有的信号函数
        # self.top_menu_help.addAction('&关于', self.about_Handle,
        #                              QtCore.Qt.CTRL + QtCore.Qt.Key_H)
        self.action_SAGD_add_paras.triggered.connect(self.show_Widget_Oil)
        # self.Pophelp.triggered.connect(self.Ui_Help)

        # log("绑定了")
        # self.window.action_SAGD_add_paras.addAction('&关于', self.show_Widget_Oil)
        pass

    def show_Widget_Oil(self):
        # from ..Function.utils import log
        # log(" show _wight")
        print(" 触发了 show_Widget_Oil")

        # 显示弹窗
        # widget = QDialog()
        # self.showdialog()
        self.dialog = Widget_Oil_para(self)
        # oil_weight.setupUi(self)
        self.dialog.show()
        # oil_weight().show()

    def showdialog(self):
        dialog = QDialog()
        # btn = QPushButton("ok", dialog)
        # btn.move(50, 50)
        dialog.setWindowTitle("Dialog")
        # dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()


class MyMainWindow(QMainWindow):
    # from ..Function.utils import log

    from PyQt5.QtCore import pyqtSignal
    from PyQt5 import QtCore
    singal_show_Widget_Oil = pyqtSignal()

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.window = Ui_MainWindow()
        # self.show_Widget_Oil()
        self.window.setupUi(self)

        self.singal_connect_all()

    def singal_connect_all(self):
        # 绑定所有的信号函数
        # self.top_menu_help.addAction('&关于', self.about_Handle,
        #                              QtCore.Qt.CTRL + QtCore.Qt.Key_H)
        self.window.action_SAGD_add_paras.triggered.connect(self.show_Widget_Oil)
        # self.Pophelp.triggered.connect(self.Ui_Help)

        # log("绑定了")
        # self.window.action_SAGD_add_paras.addAction('&关于', self.show_Widget_Oil)

        pass

    def load_data_ui(self):

        pass

    def export_data_ui(self):

        pass

    def show_Widget_Oil(self):
        # from ..Function.utils import log
        # log(" show _wight")
        print(" 触发了 dkaksd1")
        oil_weight = UI_Widget_Oil()
        # oil_weight.exec_()
        oil_weight.show()




    def show_Widget_Thermophysical(self):

        pass

    def show_Widget_fragment (self):
        pass

    def show_Widget_basic_Paras2(self):

        pass


def test():
    # 这是一个测试函数

    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MinUIWindow()
    myWin.show()
    sys.exit(app.exec_())