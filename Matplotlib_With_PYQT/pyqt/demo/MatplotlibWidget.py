import sys
import random
import matplotlib

matplotlib.use("Qt5Agg")
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QSizePolicy, QWidget, QStackedWidget
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


class MyMplCanvas(FigureCanvas):
    """FigureCanvas的最终的父类其实是QWidget。"""

    def __init__(self, parent=None, width=5, height=4, dpi=100):

        # 配置中文显示
        plt.rcParams['font.family'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

        self.fig = Figure(figsize=(width, height), dpi=dpi)  # 新建一个figure
        self.axes = self.fig.add_subplot(111)  # 建立一个子图，如果要建立复合图，可以在这里修改
        # zoom_pic()
        # 使用QStackedWidget控件将所有的的曲线图放入其中
        self.stack = QStackedWidget()

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
        lines = load_all_lines()
        width = 9
        height = 6
        dpi = 100
        for i in range(len(lines)):
            fig = Figure(figsize=(width, height), dpi=dpi)
            # 添加数据到当前画布

        pass

    def start_static_plot(self):
        self.fig.suptitle('测试静态图')

        # t = arange(0.0, 3.0, 0.01)
        # s = sin(2 * pi * t)
        # 记载所有曲线信息
        lines = load_all_lines()
        # log("lines = ({})".format(lines))

        # i是曲线的颜色参数
        i = 0
        # title, rd, Td = lines[0]

        for line in lines:
            title, rd, Td = line
            xarr = rd
            yarr = Td

            line_color = chose_color(i)
            i += 1

            self.axes.plot(xarr, yarr, color=line_color, linewidth=2.5, linestyle='-',
                           label='Td=({})'.format(title))
            # # 获取当前yarr拐点位置
            t = find_inflection_point(yarr)
            # # log('y的拐点({})'.format(t))
            # # 将拐点显示出来
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
        self.axes.set(xlim=zoom_xlim)
        self.axes.set_ylabel('静态图：Y轴')
        self.axes.set_xlabel('静态图：X轴')
        self.axes.grid(True)

        # 设置图例可拖动
        leg = self.axes.legend()
        if leg:
            leg.draggable()

    '''启动绘制动态图'''

    def start_dynamic_plot(self, *args, **kwargs):
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)  # 每隔一段时间就会触发一次update_figure函数。
        timer.start(1000)  # 触发的时间间隔为1秒。

    '''动态图的绘图逻辑可以在这里修改'''

    def update_figure(self):
        self.fig.suptitle('测试动态图')
        l = [random.randint(0, 10) for i in range(4)]
        self.axes.plot([0, 1, 2, 3], l, 'r')
        self.axes.set_ylabel('动态图：Y轴')
        self.axes.set_xlabel('动态图：X轴')
        self.axes.grid(True)
        self.draw()

    def start_dynamic_draw(self, *args, **kwargs):
        timer = QtCore.QTimer(self)
        self.page = 0
        timer.timeout.connect(self.update_figure_one)  # 每隔一段时间就会触发一次update_figure函数。
        # self.page += 1
        timer.start(500)  # 触发的时间间隔为1秒。

    def get_now_page(self):
        # t = random(1, 3)

        pass

    def update_figure_one(self, page=0):
        from main import load_all_lines
        from main import chose_color
        from main import find_inflection_point
        from main import get_zoomed_x_axes_limts
        log = print
        # 这是模仿点击事件 传入不同的page
        lines = load_all_lines()
        # i = 1
        i = self.page

        self.page = i
        if i == len(lines) or i < 0:
            log("i=({})".format(i))
            i = 0
            return None
            # break
        line = lines[i]
        log("i=({})".format(i))

        self.drow_one_line(line)
        self.page += 1

        #
        # self.fig.suptitle('测试动态图')
        # l = [random.randint(0, 10) for i in range(4)]
        #
        # self.axes.plot([0, 1, 2, 3], l, 'r')
        #
        # self.axes.set_ylabel('翻页图：Y轴')
        # self.axes.set_xlabel('翻页图：X轴')
        # self.axes.grid(True)
        # self.draw()

    def draw_one_line(self, now_line):
        # 接收的是一个曲线的数组
        # 无返回
        # 本函数功能是画单条曲线的图的图

        # 加载数据
        log = print

        # 创建figure
        # self.fig.suptitle('翻页图')
        fig = self.fig
        # 设置当前画布
        src = fig.axes

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
        src.plot(xarr, yarr, color=line_color, linewidth=2.5, linestyle='-',
                 label='Td=({})'.format(title))  # 增加了label以便增加图例

        # 获取当前yarr拐点位置
        t = find_inflection_point(yarr)
        # log('y的拐点({})'.format(t))

        # 将拐点显示出来
        xzb = xarr[t]
        yzb = yarr[t]
        src.plot(xzb, yzb, 'o')

        # 下面部分是是操作lenged标签位置
        src.legend(loc='best')  # 添加个图例 设置图例自动调整

        # 根据所有拐点的数据
        # 设置src缩放图的x轴上下限 和title
        xlim_min, xlim_max = get_zoomed_x_axes_limts()
        zoom_xlim = (xlim_min, xlim_max)
        # zoom_ylim = (ylim_min, ylim_max)
        src.set(xlim=zoom_xlim, autoscale_on=False, title='翻页图像td={}图像'.format(title))

        # 设置图例可拖动
        leg = src.legend()
        if leg:
            leg.draggable()
        # self.stack.addWidget(src)
        return src
        # self.draw()

    def draw_all_line(self, all_lines):
        # lines = all_lines
        lines = load_all_lines()
        for i in range(len(lines)):
            line = lines[i]
            pic = self.draw_one_line(line)
            self.stack.addWidget(pic)
        pass

    def zoom_pic(self):
        from main import load_all_lines
        from main import chose_color
        from main import find_inflection_point
        from main import get_zoomed_x_axes_limts
        log = print

        self.fig.suptitle('图')

        # 设置当前画布
        # src = self.axes
        # src = plt.subplot(111)  # 第一行的图 211 --> 类似(n,m,o) (n) 代表 主图分n两行 每行分成m列代表每行分成

        # 记载所有曲线信息
        # lines = load_all_lines()
        # log("lines = ({})".format(lines))

        # i是曲线的颜色参数
        i = 0
        for line in lines:
            title, rd, Td = line
            xarr = rd
            yarr = Td

            # log('rd = {}'.format(rd))
            # 自动获取不同线条颜色
            line_color = chose_color(i)
            i += 1

            # 选择颜色, 绘制曲线
            # 分别将曲线数据 加载到src图上
            log("log xarr({}) yarr ({})".format(xarr, yarr))
            l = [random.randint(0, 10) for i in range(4)]
            # self.axes.plot([0, 1, 2, 3], l, 'r')
            # self.axes.plot([0, 1, 2, 3], [0, 1, 2, 3], 'r')
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
        # self.axes.set(xlim=zoom_xlim, autoscale_on=False, title='缩放图像')

        # 设置图例可拖动
        leg = self.axes.legend()
        if leg:
            leg.draggable()


class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)
        self.initUi()

    def initUi(self):
        self.layout = QVBoxLayout(self)
        # s1 = my
        mpl = MyMplCanvas(self, width=9, height=6, dpi=100)
        mpl2 = MyMplCanvas(self, width=9, height=6, dpi=100)

        self.stack = QStackedWidget()

        self.stack.addWidget(mpl)
        self.stack.addWidget(mpl2)

        # self.mpl.start_static_plot() # 如果你想要初始化的时候就呈现静态图，请把这行注释去掉
        self.mpl.start_dynamic_draw()

        # self.mpl.start_dynamic_plot() # 如果你想要初始化的时候就呈现动态图，请把这行注释去掉
        # self.mpl_ntb = NavigationToolbar(self.mpl, self)  # 添加完整的 toolbar
        # self.zoom_pic
        # self.mpl.zoom_pic()
        self.mpl.draw_all_line('add')

        # self.layout.addWidget(self.mpl)
        # self.layout.addWidget(self.mpl_ntb)
        self.layout.addWidget(self.stack)
        # self.zoom_pic()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MatplotlibWidget()
    # ui.setWindowTitle("asdasdkl")
    ui.setWindowTitle("pyqt 和matplotlib")
    #
    # ui.mpl.start_static_plot()  # 测试静态图效果
    # ui.mpl.start_dynamic_plot() # 测试动态图效果
    ui.show()
    sys.exit(app.exec_())
