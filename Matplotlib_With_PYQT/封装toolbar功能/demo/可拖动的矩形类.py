import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

log = print

class DraggableLines:
    def __init__(self, rect):
        self.rect = rect
        self.press = None
        self.lock = False  # only one can be animated at a time

    def connect(self):

        # 连接所有需要的事件
        self.cidpress = self.rect.figure.canvas.mpl_connect(
            'button_press_event', self.on_press)
        self.cidrelease = self.rect.figure.canvas.mpl_connect(
            'button_release_event', self.on_release)
        self.cidonclick = self.rect.figure.canvas.mpl_connect(
            'button_press_event', self.on_clicked)
        self.cidmotion = self.rect.figure.canvas.mpl_connect(
            'motion_notify_event', self.on_motion)
        log('连接了所有事件')
        # print('event contains', self.rect.get_data())

    def on_press(self, event):
        # print('event contains', self.rect.get_data())
        log("on_press event = ", event)

        # 按压事件，我们将看到鼠标是否在线段上 之后存储线段的数据 以及在屏幕上的数据

        # 鼠标选中曲线
        if event.inaxes != self.rect.axes: return

        # 曲线包含数据
        contains, attrd = self.rect.contains(event)
        log("contains({})  attrd({})".format(contains, attrd))
        if not contains: return
        # print('event contains', self.rect.xy)
        # print('event contains', self.rect.get_data())
        # print('event contains', self.rect.ydata)
        #
        x0, y0 = self.rect.get_data()
        self.press = x0, y0, event.xdata, event.ydata

    def on_motion(self, event):
        # log('选中事件')
        # 移动选中的线段数据
        if self.lock is True: return
        if self.press is None: return
        if event.inaxes != self.rect.axes: return

        # log('按住了曲线', event.contains)
        x0, y0, xpress, ypress = self.press
        dx = event.xdata - xpress
        dy = event.ydata - ypress
        #print('x0=%f, xpress=%f, event.xdata=%f, dx=%f, x0+dx=%f' %
        #      (x0, xpress, event.xdata, dx, x0+dx))
        # self.rect.set_x(x0+dx)
        # self.rect.set_y(y0+dy)

        # 改变鼠标样式
        # 改变线段的样式
        # log(" on_motion event = ", event)

        self.rect.set_marker('.')

        # 曲线的样式为不填充
        self.rect.set_linestyle('none')
        # log(        self.rect.markers.MarkerStyle.get_alt_path())
        # log('cursor', self.rect.get_cursor_data(event))
        # self.set_fillstyle('none')
        # self.rect.set_linestyle('o')

        # 根据鼠标移动的数值 重新设置线段的的数值
        self.rect.set_data((x0+dx), (y0+dy))

        self.rect.figure.canvas.draw()


    def on_release(self, event):
        # 鼠标释放时间时 重置数据
        # 释放鼠标
        self.press = None
        self.rect.figure.canvas.draw()

    def on_clicked(self, event):
        # log('选中事件')
        # 移动选中的线段数据
        # log('点击的on_clicked', event.inaxes)
        log(" on_clicked event = ", event)
        log('self.press',self.press, type(self.press))

        if self.press is None: return
        log('点击到曲线press')

        if event.inaxes != self.rect.axes: return
        log('点击到曲线')
        x0, y0, xpress, ypress = self.press
        dx = event.xdata - xpress
        dy = event.ydata - ypress
        #print('x0=%f, xpress=%f, event.xdata=%f, dx=%f, x0+dx=%f' %
        #      (x0, xpress, event.xdata, dx, x0+dx))
        # self.rect.set_x(x0+dx)
        # self.rect.set_y(y0+dy)

        # 改变鼠标样式
        # 改变线段的样式
        self.rect.set_linestyle('none')
        log('点击的set_linestyle')

        self.rect.set_marker('.')
        log('set_marker')

        # 曲线的样式为不填充
        # log(        self.rect.markers.MarkerStyle.get_alt_path())
        # log('cursor', self.rect.get_cursor_data(event))
        # self.set_fillstyle('none')
        # self.rect.set_linestyle('o')

        self.rect.figure.canvas.draw()

    def can_chose_point(self):

        pass

    def can_edit_point(self):

        pass

    def disconnect(self):
        # 断开连接
        # 断开连接的功能 让曲线不再被选中
        self.rect.figure.canvas.mpl_disconnect(self.cidpress)
        self.rect.figure.canvas.mpl_disconnect(self.cidrelease)
        self.rect.figure.canvas.mpl_disconnect(self.cidmotion)

class DraggableRectangle:
    def __init__(self, rect):
        self.rect = rect
        self.press = None

    def connect(self):
        'connect to all the events we need'
        self.cidpress = self.rect.figure.canvas.mpl_connect(
            'button_press_event', self.on_press)
        self.cidrelease = self.rect.figure.canvas.mpl_connect(
            'button_release_event', self.on_release)
        self.cidmotion = self.rect.figure.canvas.mpl_connect(
            'motion_notify_event', self.on_motion)

    def on_press(self, event):
        'on button press we will see if the mouse is over us and store some data'
        if event.inaxes != self.rect.axes: return

        contains, attrd = self.rect.contains(event)
        if not contains: return
        print('event contains', self.rect.xy)
        x0, y0 = self.rect.xy
        self.press = x0, y0, event.xdata, event.ydata
        log("按住了曲线")

    def on_motion(self, event):
        'on motion we will move the rect if the mouse is over us'
        if self.press is None: return
        if event.inaxes != self.rect.axes: return
        x0, y0, xpress, ypress = self.press
        dx = event.xdata - xpress
        dy = event.ydata - ypress
        #print('x0=%f, xpress=%f, event.xdata=%f, dx=%f, x0+dx=%f' %
        #      (x0, xpress, event.xdata, dx, x0+dx))
        self.rect.set_x(x0+dx)
        self.rect.set_y(y0+dy)

        self.rect.figure.canvas.draw()


    def on_release(self, event):
        'on release we reset the press data'
        self.press = None
        self.rect.figure.canvas.draw()

    def disconnect(self):
        'disconnect all the stored connection ids'
        self.rect.figure.canvas.mpl_disconnect(self.cidpress)
        self.rect.figure.canvas.mpl_disconnect(self.cidrelease)
        self.rect.figure.canvas.mpl_disconnect(self.cidmotion)

fig = plt.figure()
ax = fig.add_subplot(111)
# rects = ax.bar(range(10), 20*np.random.rand(10))
drs = []

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

# 绘制余弦曲线，使用蓝色的、连续的、宽度为 1 （像素）的线条
line1 = ax.plot(X, C, color="blue", linewidth=1.0, linestyle="-")

# 绘制正弦曲线，使用绿色的、连续的、宽度为 1 （像素）的线条
# line2 = ax.plot(X, S, color="green", linewidth=1.0, linestyle="-")
line2 = mlines.Line2D(X, S, color="green", linewidth=1.0, linestyle="-")

ax.add_line(line2)
# line2.xda


for rect in line1:
    dr = DraggableLines(rect)
    dr.connect()
    drs.append(dr)

plt.show()