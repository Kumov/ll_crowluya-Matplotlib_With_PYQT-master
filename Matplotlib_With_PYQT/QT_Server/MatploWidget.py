import sys
import random
import matplotlib

matplotlib.use("Qt5Agg")
from PyQt5 import QtCore
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QSizePolicy,
                             QWidget,QStackedWidget, QPushButton,QTabWidget)
# from PyQt5.Con import QFarme
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
# from main import zoom_pic
from main import load_all_lines
from main import chose_color
from main import find_inflection_point
from main import get_zoomed_x_axes_limts
from Winform import Winform

class MyMplCanvas(FigureCanvas):
    """FigureCanvas的最终的父类其实是QWidget。"""

    def __init__(self, parent=None, width=5, height=4, dpi=100):

        # 配置中文显示
        plt.rcParams['font.family'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

        self.fig = Figure(figsize=(width, height), dpi=dpi)  # 新建一个figure
        self.axes = self.fig.add_subplot(111)  # 建立一个子图，如果要建立复合图，可以在这里修改
        # self.axes.hold(False)  # 每次绘图的时候不保留上一次绘图的结果
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        '''定义FigureCanvas的尺寸策略，这部分的意思是设置FigureCanvas，使之尽可能的向外填充空间。'''
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    '''绘制静态图，可以在这里定义自己的绘图逻辑'''
    def load_all_lines(self):
        # self.stack
        # 加载所有的曲线数据
        lines = load_all_lines()

        return lines

    def draw_one_line(self, now_line):
        # 接收的是一个曲线的数组
        # 无返回
        # 本函数功能是画单条曲线图

        # 创建figure
        # 在初始化的时候就有了figuare
        # self.fig.suptitle('翻页图')
        # fig = self.fig


        # 加载数据
        line = now_line
        # lines = load_all_lines()
        # line = lines[0]
        # log("lines = ({})".format(lines))

        # 提取数组数据
        title, rd, Td = line
        xarr = rd
        yarr = Td

        colori = 1
        # 自动获取不同线条颜色
        line_color = chose_color(colori)
        colori += 1

        # 选择颜色, 绘制曲线
        # 分别将曲线数据 加载到src图上
        # log("log xarr({}) yarr ({})".format(xarr, yarr))

        # 将曲线添加到axes上
        self.axes.plot(xarr, yarr, color=line_color, linewidth=2.5, linestyle='-',
                       label='Td=({})'.format(title))  # 增加了label以便增加图例

        # 获取当前yarr拐点位置
        t = find_inflection_point(yarr)
        # log('y的拐点({})'.format(t))

        # 将拐点显示出来
        xzb = xarr[t]
        yzb = yarr[t]
        self.axes.plot(xzb, yzb, 'o')

        # 下面部分是是操作lenged标签位置
        self.axes.legend(loc='best')  # 添加个图例 设置图例自动调整

        # 根据所有拐点的数据
        # 设置src缩放图的x轴上下限 和title
        xlim_min, xlim_max = get_zoomed_x_axes_limts()
        zoom_xlim = (xlim_min, xlim_max)
        # zoom_ylim = (ylim_min, ylim_max)
        self.axes.set(xlim=zoom_xlim, autoscale_on=False, title='td={}的图像'.format(title))
        # 设置图例可拖动
        leg = self.axes.legend()
        if leg:
            leg.draggable()
        # self.stack.addWidget(src)
        # return self.axes
        self.draw()


class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)

        # 创建QTabWidget分页窗口
        self.stack = QTabWidget()
        self.initUi()

    def initUi(self):
        self.layout = QVBoxLayout(self)

        # 创建matplot画布
        self.mpl = MyMplCanvas(self, width=9, height=6, dpi=100)
        self.mpl2 = MyMplCanvas(self, width=9, height=6, dpi=100)
        self.mpl3 = MyMplCanvas(self, width=9, height=6, dpi=100)
        # mpl.draw_one_line()

        # 加载数据
        # 在不同的画布上画出来
        # 将所有f分页加入到tabWidget上
        lines = load_all_lines()

        self.mpl.draw_one_line(lines[0])
        self.mpl2.draw_one_line(lines[1])
        self.mpl3.draw_one_line(lines[2])


        self.stack.addTab(self.mpl, 'td=0.12')
        self.stack.addTab(self.mpl2, 'td=0.144')
        self.stack.addTab(self.mpl3, 'td=0.176')

        # self.mpl.start_static_plot() # 如果你想要初始化的时候就呈现静态图，请把这行注释去掉
        # self.mpl.start_dynamic_draw()

        # self.mpl.start_dynamic_plot() # 如果你想要初始化的时候就呈现动态图，请把这行注释去掉
        self.mpl_ntb = NavigationToolbar(self.mpl, self)  # 添加完整的 toolbar
        self.mpl2_ntb = NavigationToolbar(self.mpl2, self)  # 添加完整的 toolbar
        self.mpl3_ntb = NavigationToolbar(self.mpl3, self)  # 添加完整的 toolbar

        self.layout.addWidget(self.mpl_ntb)
        self.layout.addWidget(self.stack)

# 给windows添加一个button

        # self.btn1 = QPushButton("Button1")
        # self.btn1.setCheckable(True)
        # self.btn1.toggle()
        # self.btn1.clicked.connect(lambda: self.whichbtn(self.btn1))
        # self.btn1.clicked.connect(self.btnstate)
        # layout.addWidget(self.btn1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = Winform()
    ui = MatplotlibWidget(parent=windows)
    ui.setWindowTitle("pyqt 和matplotlib")
    ui.resize(900, 500)
    windows.show()
    sys.exit(app.exec_()) 
