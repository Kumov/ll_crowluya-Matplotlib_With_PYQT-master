import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import time

'''
选择模式 ：
    选中点



'''
log = print


class DraggableLines:
    def __init__(self, rect):
        self.rect = rect
        self.press = None

    def connect(self):
        # 连接所有需要的事件
        self.cidclicked = self.rect.figure.canvas.mpl_connect(
            'button_press_event', self.on_click)
        self.cidpress = self.rect.figure.canvas.mpl_connect(
            'button_press_event', self.on_press)
        self.cidrelease = self.rect.figure.canvas.mpl_connect(
            'button_release_event', self.on_release)
        self.cidmotion = self.rect.figure.canvas.mpl_connect(
            'motion_notify_event', self.on_motion)

    def on_press(self, event):
        # 按下鼠标 是否是在选中的数据上
        if event.inaxes != self.rect.axes: return

        contains, attrd = self.rect.contains(event)
        if not contains: return
        # print('event contains', self.rect.xy)
        print('event contains', self.rect.get_data())
        # print('event contains', self.rect.ydata)
        x0, y0 = self.rect.get_data()
        self.press = x0, y0, event.xdata, event.ydata

    def on_motion(self, event):
        # 移动选中的线段数据
        if self.press is None: return
        if event.inaxes != self.rect.axes: return
        x0, y0, xpress, ypress = self.press
        dx = event.xdata - xpress
        dy = event.ydata - ypress
        #print('x0=%f, xpress=%f, event.xdata=%f, dx=%f, x0+dx=%f' %
        #      (x0, xpress, event.xdata, dx, x0+dx))
        # self.rect.set_x(x0+dx)
        # self.rect.set_y(y0+dy)

        # 改变鼠标样式
        # 改变线段的样式
        # self.rect.set_marker('.')
        self.rect.set_data((x0+dx), (y0+dy))

        self.rect.figure.canvas.draw()

    def on_release(self, event):
        # 鼠标释放时间时 重置数据
        self.press = None
        self.rect.figure.canvas.draw()

    def on_click(self, event):
        # 按下鼠标 是否是在选中的数据上
        if event.inaxes != self.rect.axes: return

        contains, attrd = self.rect.contains(event)
        if not contains: return
        # 点击时 曲线样式改变
        #
        self.rect.set_linestyle('dotted')

        pass
    # 改变鼠标的样式

    # 点击点 生成一根y轴的线段


    def disconnect(self):
        # 断开连接的功能 让曲线不再被选中
        self.rect.figure.canvas.mpl_disconnect(self.cidpress)
        self.rect.figure.canvas.mpl_disconnect(self.cidrelease)
        self.rect.figure.canvas.mpl_disconnect(self.cidmotion)


def raw_line():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # rects = ax.bar(range(10), 20*np.random.rand(10))
    drs = []

    X = np.linspace(-np.pi, np.pi, 50, endpoint=True)
    C, S = np.cos(X), np.sin(X)

    # 绘制余弦曲线，使用蓝色的、连续的、宽度为 1 （像素）的线条
    line1 = ax.plot(X, C, color="blue", linewidth=1.0, linestyle="-")

    # 绘制正弦曲线，使用绿色的、连续的、宽度为 1 （像素）的线条
    # line2 = ax.plot(X, S, color="green", linewidth=1.0, linestyle="-")
    line2 = mlines.Line2D(X, S, color="green", linewidth=1.0, linestyle="-")

    ax.add_line(line2)

    lines = [line1, line2]

    # for rect in line1:
    for rect in ax.lines:
        dr = DraggableLines(rect)
        dr.connect()
        drs.append(dr)

    # fig.canvas.draw()
    plt.show()

    # 十秒后断开链接
    # log('准备断开链接了')
    # time.sleep(30)
    # log('断开链接了')
    #
    # for d in drs:
    #     d.disconnect()


def test():

    pass


def main():
    raw_line()

    pass


if __name__ == '__main__':
    main()
