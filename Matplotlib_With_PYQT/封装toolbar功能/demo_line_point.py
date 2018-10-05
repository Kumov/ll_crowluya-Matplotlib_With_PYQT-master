import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

plt.rcParams['font.sans-serif'] = ['SimHei']  # 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False  # 步骤二（解决坐标轴负数的负号显示问题）
log = print



class PointBrowser:
    """
    选中点并且使其高亮 --   按键‘a’查看前一个点， ‘d’查看后一个点
    """
    def __init__(self, fig, axes, lines):
        self.figure = fig
        self.ax = axes
        self.line = lines

        self.lastind = 0
        self.text = self.ax.text(0.05, 0.95, '未选中',
                            transform=self.ax.transAxes, va='top')

        # 点选择器连接曲线
        log(" line ax figure", type(lines), type(fig), type(axes))

        x0, y0 = self.line.get_data()
        self.xs = self.line.get_data()[0]
        self.ys = self.line.get_data()[1]
        self.selected, = self.ax.plot([self.xs[0]], [self.ys[0]], 'o', ms=10, alpha=0.4,
                                 color='yellow', visible=False)
        self.selectedLine = self.ax.axvline(x=self.xs[self.lastind], visible=False)


    def connect(self):
        # 连接所有需要的事件
        self.cidclicked = self.figure.canvas.mpl_connect(
            'pick_event', self.on_point_pick)
        self.cidpress = self.figure.canvas.mpl_connect(
            'key_press_event', self.on_point_press)
        # self.cidrelease = self.figure.canvas.mpl_connect(
        #     'button_release_event', self.on_release)
        # self.cidmotion = self.figure.canvas.mpl_connect(
        #     'motion_notify_event', self.on_motion)
        log('连接选点器事件成功')

    def on_point_press(self, event):
        if self.lastind is None:
            return

        if len(self.xs) == 0:
            return

        if event.key not in ('a', 'd'):
            return
        if event.key == 'd':
            inc = 1
        else:
            inc = -1

        self.lastind += inc
        self.lastind = np.clip(self.lastind, 0, len(self.xs) - 1)
        self.update()
        log('on_point_press')

    def on_point_pick(self, event):
        log("event = ", event)
        log("artist", event.artist)
        if event.artist != self.line:
            return True

        N = len(event.ind)
        log('n = ', N)
        if not N:
            return True

        # the click locations
        xloc = event.mouseevent.xdata
        yloc = event.mouseevent.ydata
        log("x, y", xloc, yloc)

        self.xloc = xloc
        distances = np.hypot(xloc - self.xs[event.ind], yloc - self.ys[event.ind])
        log('dis', distances)
        indmin = distances.argmin()
        dataind = event.ind[indmin]

        self.lastind = dataind
        self.update()

    def update(self):
        if self.lastind is None:
            return

        dataind = self.lastind
        log("dataind", type(dataind), dataind)

        # 更新选中的点
        self.selected.set_visible(True)
        self.selected.set_data(self.xs[dataind], self.ys[dataind])

        # 更新分区曲线
        self.selectedLine.set_visible(True)
        self.selectedLine.set_xdata(self.xs[dataind])
        # self.selectedLine.set_visible(True)
        # self.selectedLine = self.ax.axvline(x=self.xs[self.lastind])

        # x = event.mouseevent.xdata
        # log("x, y", x, y)
        # self.ax.axvline(x=self.xs[dataind])
        self.text.set_text('选中点:  %d' % dataind)
        self.figure.canvas.draw()

        log('update事件成功')


    def disconnect(self):
        # 断开连接的功能 让曲线不再被选中
        self.figure.canvas.mpl_disconnect(self.cidpress)
        self.figure.canvas.mpl_disconnect(self.cidrelease)
        # self.figure.canvas.mpl_disconnect(self.cidmotion)

        # 断开曲线数据
        self.line = None


class DraggableLines:
    def __init__(self, line):
        self.line = line
        self.press = None

        # 当前曲线是否可操作
        self.lock = False
        #
        # # 选择点相关属性
        # self.lastind = 0
        # self.text = ax.text(0.05, 0.95, 'selected: none',
        #                     transform=ax.transAxes, va='top')
        # # self.selected, = ax.plot([self.xs[0]], [self.ys[0]], 'o', ms=12, alpha=0.4,
        # #                          color='yellow', visible=False)

    def connect(self):
        # 连接所有需要的事件
        self.cidpress = self.line.figure.canvas.mpl_connect(
            'button_press_event', self.on_press)
        self.cidrelease = self.line.figure.canvas.mpl_connect(
            'button_release_event', self.on_release)
        # self.cidmotion = self.rect.figure.canvas.mpl_connect(
        #     'motion_notify_event', self.on_motion)
        self.cidonclick = self.line.figure.canvas.mpl_connect(
            'pick_event', self.on_pick)
        # self.cidonpickpoint = self.rect.figure.canvas.mpl_connect(
        #     'pick_event', self.on_pick_point)

    def on_press(self, event):
        # 按下鼠标 是否是在选中的数据上
        'on button press we will see if the mouse is over us and store some data'
        if event.inaxes != self.line.axes: return

        contains, attrd = self.line.contains(event)
        if not contains: return
        # print('event contains', self.rect.xy)
        # print('event contains', self.rect.get_data())
        # print('event contains', self.rect.ydata)
        # 曲线的样式为不填充
        self.line.set_linestyle('none')
        # 改变鼠标样式
        # 改变线段的样式
        self.line.set_marker('.')

        x0, y0 = self.line.get_data()
        # log('poc', x0, len(x0))
        self.press = x0, y0, event.xdata, event.ydata

        # 设置曲线点为可操作

        if self.lock is False:
            self.line.set_picker(5)
        pass


        # log('end on_press', self.press)

    def on_motion(self, event):
        # 移动选中的线段数据
        if self.press is None: return
        if event.inaxes != self.line.axes: return
        x0, y0, xpress, ypress = self.press
        dx = event.xdata - xpress
        dy = event.ydata - ypress
        # print('x0=%f, xpress=%f, event.xdata=%f, dx=%f, x0+dx=%f' %
        #      (x0, xpress, event.xdata, dx, x0+dx))
        # self.rect.set_x(x0+dx)
        # self.rect.set_y(y0+dy)

        # 改变鼠标样式
        # 改变线段的样式
        self.line.set_marker('.')
        self.line.set_data((x0 + dx), (y0 + dy))

        self.line.figure.canvas.draw()

    def on_pick(self, event):
        # 移动选中的线段数据
        log('到了 onpick press', self.press)
        # if self.press is None: return
        # if event.inaxes != self.rect.axes: return
        # x0, y0, xpress, ypress = self.press
        # dx = event.xdata - xpress
        # dy = event.ydata - ypress
        # print('x0=%f, xpress=%f, event.xdata=%f, dx=%f, x0+dx=%f' %
        #      (x0, xpress, event.xdata, dx, x0+dx))
        # self.rect.set_x(x0+dx)
        # self.rect.set_y(y0+dy)
        log("on_clicked 就是这里")
        # 改变鼠标样式
        # 改变线段的样式
        # self.rect.set_marker('.')

        # 曲线的样式为不填充
        # self.rect.set_linestyle('none')
        # 改变鼠标样式
        # 改变线段的样式
        # 选中了该点 设置该点的样式
        self.line.set_marker('.')
        log('on_pick_point event', event, type(event))
        thisline = event.artist
        xdata = thisline.get_xdata()
        ydata = thisline.get_ydata()
        ind = event.ind
        log('ind,', ind)
        log('thisline,', thisline)
        log('xdata,', xdata)
        # 找到线的上一个axes
        # self.rect.set_markevery((0.5, 0.1))
        # self.selected, = self.rect.set_markevery(xdata, ydata, 'o', ms=12, alpha=0.4, color='yellow', visible=True)
        points = tuple(zip(xdata[ind], ydata[ind]))
        print('on_pick_point onpick points:', points)



        # self.rect.pick(event)
        # log(self.rect.get_xydata())
        # self.rect.set_data((x0+dx), (y0+dy))

        self.line.figure.canvas.draw()

    def on_release(self, event):
        # 鼠标释放时间时 重置数据
        self.press = None
        self.line.figure.canvas.draw()

    def on_pick_point(self, event):
        # if event.artist != line:
        #     return True
        # if self.press is None:
        #     return
        log("event = ", event)

        # log("artist", event.artist)
        # if event.artist != self.rect:
        #     return True

        if event.inaxes != self.line.axes:
            return
        log('jin ru shi jian le')

        log('on_pick_point event', event, type(event))
        thisline = event.artist
        xdata = thisline.get_xdata()
        ydata = thisline.get_ydata()
        ind = event.ind
        log('ind,', ind)

        points = tuple(zip(xdata[ind], ydata[ind]))
        print('on_pick_point onpick points:', points)
        # N = len(event.ind)
        # if not N:
        #     return True

        # the click locations
        x = event.xdata
        y = event.ydata

        log('x, y = ', x, y)
        # distances = np.hypot(x - xs[event.ind], y - ys[event.ind])
        # indmin = distances.argmin()
        # dataind = event.ind[indmin]

        # self.lastind = dataind
        # self.update()

    def chose_point(self):

        pass

    def disconnect(self):
        # 断开连接的功能 让曲线不再被选中
        self.line.figure.canvas.mpl_disconnect(self.cidpress)
        self.line.figure.canvas.mpl_disconnect(self.cidrelease)
        self.line.figure.canvas.mpl_disconnect(self.cidmotion)
