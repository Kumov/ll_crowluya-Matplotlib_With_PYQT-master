import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QDialog
'''
1.取出 UI_Original 文件夹下 qtdesiger生成的*.ui文件转化的*.py文件
2.将1得到的文件经过加工后给窗口添加函数功能
'''


from UI_Original.UI_MainWindows import Ui_MainWindow
from UI_Original.UI_thermophysical_para import Ui_Widget_Thermophysical_paras  # 热物性参数
from UI_Original.UI_oil_reservoir_para import Ui_Widget_Oil_pool_paras  # 油藏参数
from UI_Original.UI_basic_paras2 import Ui_basic_Paras2  # 基本参数2
from UI_Original.UI_fragment_paras import Ui_fragment_Paras  # 分段参数
log = print


def msg_box(message):
    from PyQt5.QtWidgets import QMessageBox
    # customMsgBox = QMessageBox(self)
    msg = message
    # QMessageBox.information(self, "标题",  "消息",  QMessageBox.Yes | QMessageBox.No)
    pass


msg_box('不能为空')


class Widget_fragment(QMainWindow, Ui_fragment_Paras):
    # 分段参数弹窗
    def __init__(self, parent=None):
        super(Widget_fragment, self).__init__(parent)
        self.setupUi(self)


class Widget_basic_Paras2(QMainWindow, Ui_basic_Paras2):
    # 基本参数2弹窗
    def __init__(self, parent=None):
        super(Widget_basic_Paras2, self).__init__(parent)
        self.setupUi(self)


class Widget_Oil_para(QMainWindow, Ui_Widget_Oil_pool_paras):
    # 油藏参数弹窗
    def __init__(self, parent=None):
        super(Widget_Oil_para, self).__init__(parent)
        self.setupUi(self)
        self.oil_values = dict()
        self.singal_all()

    def msg_box(self, title, message):
        from PyQt5.QtWidgets import QMessageBox
        # customMsgBox = QMessageBox(self)
        msg = message
        til = title
        # log('进入了 msg_box')
        QMessageBox.information(self,til, msg, QMessageBox.Yes | QMessageBox.No)

    def singal_all(self):
        # 信号
        self.pushButton_oil_para_cancel.clicked.connect(self.btn_clicked_cancel)
        self.pushButton_oil_para_finish.clicked.connect(self.check_and_update_data)
        self.pushButton_oil_para_next.clicked.connect(self.check_and_update_data)
        pass

    def get_value(self):
        # 获取弹窗输入的值
        para_oil_layer_H = self.lineEdit_para_oil_layer_H.text()
        para_space_W = self.lineEdit_para_well_space_W.text()
        para_Roi = self.lineEdit_para_Roi.text()
        para_Rr = self.lineEdit_para_Rr.text()
        para_P_r = self.lineEdit_para_P_r.text()
        para_T_r = self.lineEdit_para_T_r.text()
        log('para_oil_layer_H({})'.format(para_oil_layer_H))
        # 点击完成之后 设置当前的self.oil_values

        return self.oil_values

    def set_value(self, dict):
        # 传入dict 保存的值
        # 设置弹窗的值

        self.oil_values = dict
        para_oil_layer_H = self.oil_values.get('para_oil_layer_H', '24')
        para_space_W = self.oil_values.get('para_space_W', '40.5')
        para_Roi = self.oil_values.get('para_Roi', '960')
        para_Rr = self.oil_values.get('para_Rr', '2320')
        para_P_r = self.oil_values.get('para_P_r', '2')
        para_T_r = self.oil_values.get('para_T_r', '326.57')

        # 设置界面的初值
        self.lineEdit_para_oil_layer_H.setText(para_oil_layer_H)
        self.lineEdit_para_well_space_W.setText(para_space_W)
        self.lineEdit_para_Roi.setText(para_Roi)
        self.lineEdit_para_Rr.setText(para_Rr)
        self.lineEdit_para_P_r.setText(para_P_r)
        self.lineEdit_para_T_r.setText(para_T_r)

        pass

    # 四个按钮对于的函数事件
    def btn_clicked_cancel(self):
        log(" btn_clicked_close")
        # self.window().hide()
        self.window().close()
        # self.()
        pass

    def btn_clicked_finish(self):
        # log(" btn_clicked  finsh ")
        pass

    def btn_clicked_next(self):
        pass

    def btn_clicked_load(self):
        log(" btn_clicked  load")
        self.get_value()
        pass

    def check_and_update_data(self):
        # 最后检查数据合法性
        # 并且将数据完整赋值到self.oil_values

        values = []
        para_oil_layer_H = self.lineEdit_para_oil_layer_H.text()
        para_space_W = self.lineEdit_para_well_space_W.text()
        para_Roi = self.lineEdit_para_Roi.text()
        para_Rr = self.lineEdit_para_Rr.text()
        para_P_r = self.lineEdit_para_P_r.text()
        para_T_r = self.lineEdit_para_T_r.text()
        # values.append(para_oil_layer_H)

        values.append(para_oil_layer_H)
        values.append(para_space_W)
        values.append(para_Roi)
        values.append(para_Rr)
        values.append(para_P_r)
        values.append(para_T_r)

        # 不能为空字符串
        for va in values:
            if va == '':
                # log('当前的 va （{}）'.format(va))
                self.msg_box('提示', '数据不完整')
                return

        # 存放数据
        self.oil_values['para_oil_layer_H'] = para_oil_layer_H
        self.oil_values['para_space_W'] = para_space_W
        self.oil_values['para_Roi'] = para_Roi
        self.oil_values['para_Rr'] = para_Rr
        self.oil_values['para_T_r'] = para_T_r
        self.oil_values['para_P_r'] = para_P_r
        pass

    def init_values(self):
        # 初始化值
        self.oil_values['para_oil_layer_H'] = ''
        self.oil_values['para_space_W'] = ''
        self.oil_values['para_Roi'] = ''
        self.oil_values['para_Rr'] = ''
        self.oil_values['para_P_r'] = ''
        self.oil_values['para_T_r'] = ''


class Widget_Thermophysical(QMainWindow, Ui_Widget_Thermophysical_paras):
    # 热物性参数弹窗
    def __init__(self, parent=None):
        super(Widget_Thermophysical, self).__init__(parent)
        self.setupUi(self)

    def msg_box(self, title, message):
        from PyQt5.QtWidgets import QMessageBox
        # customMsgBox = QMessageBox(self)
        msg = message
        til = title
        # log('进入了 msg_box')
        QMessageBox.information(self, til, msg, QMessageBox.Yes | QMessageBox.No)

    def singal_all(self):
        # 信号
        self.pushButton_oil_para_cancel.clicked.connect(self.btn_clicked_cancel)
        self.pushButton_oil_para_finish.clicked.connect(self.check_and_update_data)
        self.pushButton_oil_para_next.clicked.connect(self.check_and_update_data)
        pass


class TestMinUIWindow(QMainWindow):
    def __init__(self, parent=None):
        super(TestMinUIWindow, self).__init__(parent)
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
        # self.dialog1 = Widget_Thermophysical(self)
        # self.dialog2= Widget_fragment(self)
        # self.dialog3 = Widget_basic_Paras2(self)

        # 设置或显示数据
        self.dialog.show()
        # dict = {'oil_layer_H' : '20', 'space_W': '15'}
        dict = {}
        self.dialog.set_value(dict)
        # self.dialog.get_value()

        # self.dialog1.show()
        # self.dialog2.show()
        # self.dialog3.show()



def test():
    app = QApplication(sys.argv)
    myWin = TestMinUIWindow()
    myWin.show()
    sys.exit(app.exec_())
    pass


if __name__ == '__main__':
    test()
