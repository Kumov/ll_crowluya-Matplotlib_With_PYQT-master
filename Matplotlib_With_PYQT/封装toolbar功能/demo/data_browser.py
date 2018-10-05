"""
============
Data Browser
============

Connecting data between multiple canvases.

This example covers how to interact data with multiple canvases. This
let's you select and highlight a point on one axis, and generating the
data of that point on the other axis.
"""
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.artist import Artist

log = print


class PointBrowser(object):
    """
    选中点并且使其高亮 --   按键‘a’查看前一个点， ‘d’查看后一个点
    """

    def __init__(self, line):
        self.line = line
        log('line', type(line), line)
        self.lastind = 0
        self.lock = False
        self.pressedpoint = None
        self.text = ax.text(0.05, 0.95, 'selected: none',
                            transform=ax.transAxes, va='top')
        # self.selected = ax.plot([xs[0]], [ys[0]], 'o', ms=12, alpha=0.4,
        #                          color='yellow', visible=False)

    def connect(self):

        pass

    def onpress(self, event):
        if self.lastind is None:
            return
        if event.key not in ('n', 'p'):
            return
        if event.key == 'n':
            inc = 1
        else:
            inc = -1

        self.lastind += inc
        self.lastind = np.clip(self.lastind, 0, len(xs) - 1)
        self.update()

    def onpick(self, event):
        log("event = ", event)
        log("artist", event.artist)
        if event.artist != line:
            return True

        N = len(event.ind)
        log('n = ', N)
        if not N:
            return True

        # the click locations
        x = event.mouseevent.xdata
        y = event.mouseevent.ydata
        log("x, y", x, y)

        distances = np.hypot(x - xs[event.ind], y - ys[event.ind])
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

        self.selected.set_visible(True)
        self.selected.set_data(xs[dataind], ys[dataind])

        self.text.set_text('selected: %d' % dataind)
        fig.canvas.draw()

    def on_point_pressure(self, event):
        # 双击该点修改改点的值
        log("event = ", event)
        # 选中该点
        # 选中曲线上的点
        log("event = ", event)
        # log("artist", event.artist)

        # 双击选中该点
        if event.dblclick is False:
            return
        log("双击了啊")
        # 获取当前点的坐标

        # 其他点锁定
        self.lock = True
        log(" lastind", self.lastind)
        self.pressedpoint = self.lastind

        # 获得当前曲线的数据


        # 获得选中曲线 点 的数值
        xp, yp = self.xs[self.lastind], self.ys[self.lastind]

        self.pressedpoint = xp, yp, event.xdata, event.ydata

        # 获得当前点的坐标

    def on_point_motion(self, event):
        # log('选中事件')
        # 移动选中的线段数据

        # if self.lock is True:
        #     return
        # if self.press is None: return
        # if event.inaxes != self.rect.axes: return
        if self.pressedpoint is None:
            return
        xp, yp, xpress, ypress = self.pressedpoint
        dx = event.xdata - xpress
        dy = event.ydata - ypress
        #print('x0=%f, xpress=%f, event.xdata=%f, dx=%f, x0+dx=%f' %
        #      (x0, xpress, event.xdata, dx, x0+dx))
        # self.rect.set_x(x0+dx)
        # self.rect.set_y(y0+dy)

        # 改变鼠标样式
        # 改变线段的样式
        log(" on_motion event = ", event)

        # 曲线的样式为不填充
        # log(        self.rect.markers.MarkerStyle.get_alt_path())
        # log('cursor', self.rect.get_cursor_data(event))
        # self.set_fillstyle('none')
        # self.rect.set_linestyle('o')
        # 设置线段的点
        self.xs[self.lastind] = (xp+dx)
        self.ys[self.lastind] = (yp+dy)
        self.update()
        # 根据xs 和 ys 重新绘制图像
        self.figure.canvas.draw()
        log('最后重绘了')

    def on_point_release(self, event):
        # 鼠标释放时间时 重置数据
        # 释放鼠标
        self.pressedpoint = None
        self.line.figure.canvas.draw()
        fig.canvas.draw()


        # if self.line.stale:
        #     self.canvas.draw_idle()
        # # self.canvas.restore_region(self.background)
        # self.ax.draw_artist(self.poly)
        # self.ax.draw_artist(self.line)
        # self.canvas.blit(self.ax.bbox)


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    X = np.linspace(-np.pi, np.pi, 100, endpoint=True)
    C, S = np.cos(X), np.sin(X)

    # X = np.random.rand(100, 200)
    # xs = np.mean(X, axis=1)
    # ys = np.std(X, axis=1)
    # log('xs =',xs, len(xs), type(xs))
    # log('ys=', ys)

    # xs = X
    # ys = C

    fig, (ax) = plt.subplots(1, 1)
    ax.set_title('click on point to plot time series')
    # line, = ax.plot(xs, ys, 'o', picker=6)  # 5 points tolerance
    # line = a(X, C, marker='o', picker=6)  # 5 points tolerance
    # ax.add_line(line)
    line = ax.plot(X, C, marker='o', picker=6)  # 5 points tolerance

    log('line = ', type(line), line)
    # ax.draw_artist(line)
    for l in line:
        browser = PointBrowser(l)

    fig.canvas.mpl_connect('pick_event', browser.onpick)
    fig.canvas.mpl_connect('key_press_event', browser.onpress)
    fig.canvas.mpl_connect('button_press_event', browser.on_point_pressure)
    fig.canvas.mpl_connect('motion_notify_event', browser.on_point_motion)
    fig.canvas.mpl_connect('button_release_event', browser.on_point_release)



    plt.show()
