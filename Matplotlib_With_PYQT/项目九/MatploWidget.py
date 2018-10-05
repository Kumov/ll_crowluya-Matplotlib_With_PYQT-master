import sys
import random
import matplotlib

matplotlib.use("Qt5Agg")
from PyQt5 import QtCore
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QSizePolicy,
                             QWidget,QStackedWidget, QPushButton,QTabWidget, QDesktopWidget)
# from PyQt5.QtCore import QT.StrongFocus
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig
# from main import zoom_pic


from loadlines import load_all_lines

from ZoomCurve import chose_color
from ZoomCurve import find_inflection_point
from ZoomCurve import get_zoomed_x_axes_limts

from Winform import Winform


class MatplotlibWidget(QWidget):
    # 测试加载图像的数据
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.setLayout(QVBoxLayout())
        # self.canvas = PlotCanvas(self, width=10, height=8)
        # self.toolbar = NavigationToolbar(self.canvas, self)

        self.stack = QTabWidget()
        # self.layout().addWidget(self.toolbar)
        # self.layout().addWidget(self.canvas)
        self.layout().addWidget(self.stack)

        # self.initUi()
        pass

    def initUi(self):
        self.layout = QVBoxLayout(self)

        # 创建matplot画布
        self.mpl = PlotCanvas(self, width=9, height=6, dpi=100)
        self.mpl2 = PlotCanvas(self, width=9, height=6, dpi=100)
        self.mpl3 = PlotCanvas(self, width=9, height=6, dpi=100)
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

        self.layout.addWidget(self.stack)
        # self.center()


class PlotCanvas(FigureCanvas):
    # pyqt显示matplotlib图像的类
    def __init__(self, parent=None, width=10, height=8, dpi=100):
        # 配置中文显示
        plt.rcParams['font.family'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

        self.fig = Figure(figsize=(width, height), dpi=dpi)  # 新建一个figure
        # self.canvas.setParent(self.main_frame)

        self.dpi = dpi
        self.axes = self.fig.add_subplot(111)  # 建立一个子图，如果要建立复合图，可以在这里修改
        # self.toolbar = sel
        # self.axes.hold(False)  # 每次绘图的时候不保留上一次绘图的结果

        FigureCanvas.__init__(self, self.fig)
        # self.canvas = FigureCanvas(self.fig)
        self.mpl_nav_toolbar = ''
        # 添加事件响应
        # FigureCanvas.mpl_connect('key_press_event', self.on_key_press)
        # FigureCanvas.setFocusPolicy(self, QFocusPolicy.StrongFocus)

        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)

        FigureCanvas.updateGeometry(self)
        # self.plot()

    # def plot(self):
    #     data = [random.random() for i in range(250)]
    #     ax = self.figure.add_subplot(111)
    #     ax.plot(data, 'r-', linewidth = 0.5)
    #     ax.set_title('PyQt Matplotlib Example')
    #     self.draw()
# 给windows添加一个button

        # self.btn1 = QPushButton("Button1")
        # self.btn1.setCheckable(True)
        # self.btn1.toggle()
        # self.btn1.clicked.connect(lambda: self.whichbtn(self.btn1))
        # self.btn1.clicked.connect(self.btnstate)
        # layout.addWidget(self.btn1)
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

    # def add_subplot(self):
    #
    #     pass
if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = Winform()
    ui = MatplotlibWidget(parent=windows)
    ui.setWindowTitle("pyqt 和matplotlib")
    ui.resize(900, 500)
    windows.show()
    sys.exit(app.exec_()) 
