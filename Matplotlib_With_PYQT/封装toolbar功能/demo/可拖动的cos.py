import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

plt.rcParams['font.sans-serif'] = ['SimHei']  # 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False  # 步骤二（解决坐标轴负数的负号显示问题）
log = print


class ZoningLine:
    # 分区线

    # 添加分区线

    # 删除分区线

    # 分区线跟随Point移动

    pass


class SectionLine:
    def __init__(self, xdata, axvline):
        self.data = xdata
        self.line = axvline

    @classmethod
    def new(cls):
        ...

    def remove(self):
        ...

    def edit(self):
        ...
    pass


class PointBrowser:
    """
    选中点并且使其高亮 --   按键‘a’查看前一个点， ‘d’查看后一个点
    """
    # 添加分区直线
    axline = plt.axvline

    # axline(3)
    def __init__(self, fig, axes, lines):
        self.figure = fig
        self.ax = axes
        self.line = lines

        # 分区线保存在sectionline中 曲线只能被添加一次
        secdata = []
        seclines = []
        # data 和lines 一一对应
        self.sectionlines = [secdata, seclines]
        # self.nowline = self.line
        self.line.set_picker(5)
        # 编辑点的时候 锁定画布
        self.islock = False
        # 是否编辑当前点
        self.editpoint = False
        # 获得当前曲线的数据
        self.xs, self.ys = self.line.get_data()

        self.pressedpoint = None

        # 当前点的序号
        self.lastind = 0

        self.text = self.ax.text(0.05, 0.95, '未选中',
                            transform=self.ax.transAxes, va='top')
        self.info =  '选中点并且使其高亮 --   按键‘a’查看前一个点， ‘d’查看后一个点 \n 双击计入\\推出编辑点的功能'
        self.letext = self.ax.text(0.05, 0.95, self.info,
                            transform=self.ax.transAxes, va='baseline')

        # 点选择器连接曲线
        self.selected, = self.ax.plot([self.xs[0]], [self.ys[0]], 'o', ms=10, alpha=0.4,
                                 color='yellow', visible=False)

        # 分区曲线
        self.selectedLine = self.ax.axvline(x=self.xs[self.lastind], visible=False)
        # self.selectedLine = self.ax.add_axvline

    def connect(self):
        # 连接所有需要的事件
        # 选中线上的点 并且高亮
        self.cidclicked = self.figure.canvas.mpl_connect(
            'pick_event', self.on_point_pick)
        # 按键‘a’查看前一个点， ‘d’查看后一个点
        self.cidpress = self.figure.canvas.mpl_connect(
            'key_press_event', self.on_point_press)
        # 编辑选中的点
        self.cidpress = self.figure.canvas.mpl_connect(
            'button_press_event', self.on_point_edit_pressure)
        # 编辑点之后释放鼠标
        self.cidpointrelease = self.figure.canvas.mpl_connect(
            'button_release_event', self.on_point_release)
        # # 移动点坐标
        self.cidpoint_motion = self.figure.canvas.mpl_connect(
            'motion_notify_event', self.on_point_motion)
        # log('连接选点器事件成功')

    def on_point_press(self, event):
        # 已选中点的情况下按压不停键位得到不同的结果
        # 选定编辑点 （self.islock） 锁定 按压回车或者双击将点加入到分区曲线中去
        # 未选定编辑点 按 a 跳到上一个点 按 d 下一个点

        # 选中曲线上的点
        if event.inaxes != self.line.axes:
            return
        log("没有锁定", self.islock)
        if self.lastind is None:
            return
        if len(self.xs) == 0:
            return

        log('arties({})'.format(event.inaxes))
        # log('arties({})'.format(len(self.ax.axvlin

        # 回车键添加当前点到分区里去
        # 因为分区线是建立在原始数据的的基础上的
        # 所以只保存原始数据的x点的顺序 不保存具体的数值
        # self.ax.axvline(-1).remove()
        if event.key == 'enter':
            secdata = self.sectionlines[0]
            if self.lastind not in secdata:
                log('没有添加过')
                key = self.lastind
                line = self.ax.axvline(self.xs[key])
                self.sectionlines.append(self.lastind)
                log('当前分区', self.sectionlines)
        # 删除分区线
        log('on_point_press', event.key)
        if event.key == 'delete':
            if self.lastind in self.sectionlines:

                self.sectionlines.remove(self.lastind)
                # 删除指定x数值 的axvline
                # 一种方法是找出所有的直线对象 删除所有的线 再重绘
                # 另一种是 ？
                # self.ax.lines[-1].remove()
                # 根据 event.ind
                log('当前的artist', event.inaxes)
                # log('当前的ind', event.ind)

                # self.update()
            log('当前分区', self.sectionlines)

        # 未选定编辑点
        # 按 a 跳到上一个点 按 d 下一个点
        if self.islock is True:
            return
        if event.key not in ('a', 'd', 'right', 'left'):
            return
        if event.key in ['d', 'right']:
            inc = 1
        else:
            inc = -1

        self.lastind += inc
        self.lastind = np.clip(self.lastind, 0, len(self.xs) - 1)
        self.update()
        log('on_point_press end func')

    def add_section_line(self):
        # 增加分区线
        # self.sectionline是 list 包含两个数组secdata[] ，secline[]
        # secdata 存放分区点的位置 secline存放曲线的实体
        # 分区位置和曲线根据数组下标一一对应

        secdata = self.sectionlines[0]
        secline = self.sectionlines[1]
        log('id of secdata', secdata is self.sectionlines)
        # 添加sectionline
        dataind = self.lastind
        # secdata里面添加dataind
        # secline里面添加line
        if dataind not in secdata:
            log('没有添加过')
            secdata.append(dataind)
            secline.append(self.ax.axvline(self.xs[self.lastind]))
            log('当前分区', self.sectionlines)
        pass

    def delete_section_line(self):
        # 删除sectionline
        secdata = self.sectionlines[0]
        secline = self.sectionlines[1]
        log('id of secdata', secdata is self.sectionlines)
        # 添加sectionline
        dataind = self.lastind
        if dataind in secdata:
            ind = secdata.index(dataind)
            secdata.pop(ind)
            secline.pop(ind)
            # secdata.remove(dataind)

        pass

    def change_section_line(self):
        # 修改section sectionline
        secdata = self.sectionlines[0]
        secline = self.sectionlines[1]
        log('id of secdata', secdata is self.sectionlines)
        # 添加sectionline
        dataind = self.lastind
        if dataind in secdata:
            ind = secdata.index(dataind)
            secdata.pop(ind)
            secline.pop(ind)
        pass

    def on_point_pick(self, event):
        # 选中线上的点 并且高亮该点
        # log("event = ", event.inaxes)
        # log(" on_point_pick artist", event.artist)
        # # log("plt coloctions ({})".format(plt.collections))
        # # log("figure coloctions ({})".format(self.figure.collections))
        # log("event attrbut  name({}) canvas ({}) guiEvent ({}) ".format(event.name, event.canvas, event.guiEvent))
        # # event.artist.remove()
        # log("start")
        log(" is axvline({})".format(event.artist == self.ax.axvline))
        log(" type axes ({})".format(type(event.artist.axes)))
        log(" type({})".format(type(event.artist)))
        log(" ind({})".format(type(event.ind)))
        # log("end")

        if self.islock is True:
            return

        if event.artist != self.line:
            return

        N = len(event.ind)
        log('n = ', N)
        if not N:
            return True
        # the click locations
        xloc = event.mouseevent.xdata
        yloc = event.mouseevent.ydata
        log("x, y", xloc, yloc)
        # self.xloc = xloc
        # 选中线上该点
        distances = np.hypot(xloc - self.xs[event.ind], yloc - self.ys[event.ind])
        # log('dis', distances)
        indmin = distances.argmin()
        # log('indmin', indmin)
        # self.editpoint =
        dataind = event.ind[indmin]
        self.lastind = dataind
        self.update()
        log('on_point_pick func end')

    def on_point_edit_pressure(self, event):
        #   移动按压点的坐标 改变编辑状态
        log("event = ", event)
        # 选中该点
        # 选中曲线上的点
        if event.inaxes != self.line.axes:
            return
        # 鼠标选中曲线
        # 获取当前点的坐标
        contains, _ = self.line.contains(event)
        if not contains:
            return
        # log(" lastind", self.lastind)
        # 获得选中曲线 点 的数值
        xp, yp = self.xs[self.lastind], self.ys[self.lastind]
        self.pressedpoint = xp, yp, event.xdata, event.ydata
        # 双击该点 改变点的编辑状态
        # 如果当前点坐标可改变 锁定该点
        if event.dblclick is True:
            self.editpoint = not self.editpoint
            self.islock = self.editpoint
            log(" 锁定编辑 ({})在编辑点么({})".format(self.islock, self.editpoint))
        # 获得当前点的坐标
        # log('on_point_edit pressure func end 当前点坐标({})'.format(self.pressedpoint))

    def on_point_motion(self, event):
        # 移动选中的点
        if self.pressedpoint is None:
            return
        if self.editpoint is False:
            return
        contains, attrd = self.line.contains(event)
        # 选中的点在曲线上
        if not contains:
            return
        # 确认当前是可用曲线（数据点数量大于1）
        line_len = len(self.xs)
        # log("确定点击after({})".format(contains, attrd))
        # log(' ', line_len)
        # 当然也可以用一下语句 但是下面的语句方便理解
        # if line_len < 2 : return
        if line_len == 0 or line_len == 1:
            return
        xdata = event.xdata
        # xydata --> 鼠标点击的matplotlib的坐标里的值 如果是放大或缩小事件该值就为None  event.inaxes 也为None
        # log('on_point_motion ', xdata)
        if xdata is None:
            return
        # log(" on_motion event = ({}) xdata=({}), contains = ({})".format(event, xdata, contains))
        # 确定x可编辑的范围
        if self.lastind == 0:
            # 选中的点是第一个点 xdata范围为负无穷到 第二个点的x坐标
            if xdata > self.xs[self.lastind + 1]:
                return
        elif self.lastind == line_len:
            # 选中的点是最后一个点 xdata范围为倒数第二个点 x坐标到正无穷
            if xdata < self.xs[self.lastind - 1]:
                return
        else:
            # 选中的点左右都有点 x范围左边点的x 到右边点的x
            xb = self.xs[self.lastind - 1]
            xp = self.xs[self.lastind + 1]
            log('xdata', event.xdata, )
            log("xb({}), xp({})".format(xb, xp))
            log('边界条件', xdata < xb or xdata > xp)
            if xdata < xb or xdata > xp:
                return
        # 获取x， y移动的范围
        # log('xdata', event.xdata, )
        xp, yp, xpress, ypress = self.pressedpoint
        dx = event.xdata - xpress
        dy = event.ydata - ypress
        # 设置线段的点
        self.xs[self.lastind] = (xp+dx)
        self.ys[self.lastind] = (yp+dy)
        self.line.set_data(self.xs, self.ys)
        # 重绘曲线
        self.update()
        # self.figure.canvas.draw()
        log('最后重绘了')

    def on_point_release(self, event):
        # 鼠标释放时间时 重置数据
        # 释放鼠标

        if event.button != 1:
            return
        self.pressedpoint = None
        self.line.figure.canvas.draw()
        # self.figure.canvas.draw()

    def update(self):
        if self.lastind is None:
            return

        # dataind = self.lastind
        # log("dataind", type(dataind), dataind)
        #
        # # 更新选中的点
        # self.selected.set_visible(True)
        # self.selected.set_data(self.xs[dataind], self.ys[dataind])
        self.update_select_point()
        self.update_selected_line()
        self.update_section_line()
        self.updata_section_span()
        self.figure.canvas.draw()
        # self.ax.hold(False)  # 每次绘图的时候不保留上一次绘图的结果

        self.line.figure.canvas.draw()
        self.figure.canvas.flush_events()
        # self.line.canvas.flush_events()
        # self.update_selected_line()

        log('update事件成功')

    def update_select_point(self):
        # 跟新选中点的外围点
        if self.lastind is None:
            return

        dataind = self.lastind
        log("dataind", type(dataind), dataind)
        # 更新选中的点
        self.selected.set_visible(True)
        self.selected.set_data(self.xs[dataind], self.ys[dataind])
        self.text.set_text('选中点:  %d' % dataind)
        # self.figure.draw_artist(self.selected)
        # self.figure.canvas.draw()
        # self.figure.canvas.flush_events()
        pass

    def update_selected_line(self):
        # 当前选中的点 的曲线
        if self.lastind is None:
            return

        dataind = self.lastind
        # log("dataind", type(dataind), dataind)
        # 更新分区曲线
        self.selectedLine.set_color("r")
        self.selectedLine.set_visible(True)
        self.selectedLine.set_xdata(self.xs[dataind])

        # # x = event.mouseevent.xdata
        # # log("x, y", x, y)
        # # self.ax.axvline(x=self.xs[dataind])
        # self.text.set_text('选中点:  %d' % dataind)
        #
        # self.figure.canvas.draw()
        # self.figure.canvas.flush_events()
        # # self.line.canvas.flush_events()
        log('update_selected_line事件成功')

    def update_section_line(self):
        # 在线的axes上 画出分区线
        # 当前坐标点加入到分区图形中去

        if len(self.sectionlines[0]) == 0:
            return
        if self.lastind is None:
            return
        # 添加sectionline

        # 删除sectionline

        # 修改sectionline

        # 清空matplotlib figure上的原来的所有的 垂直线

        # self.sectionlines.add(self.lastind)
        # 重绘曲线
        # sectionlines = []
        # 不重复的设置sectionlines
        # 修改曲线
        # 重置曲线

        # 绘制分区曲线都是一根一根绘制的
        # 即只需要绘制self.sectionlines 的最后一根曲线
        log("当前曲线一共有({})".format(self.ax.lines))
        for axl in self.sectionlines:
            xdata = self.xs[axl]
            # if axl not in sectionlines:
            #     sectionlines.append(axl)
            self.ax.axvline(xdata)
        # self.updata_section_span()
        pass

    def updata_section_span(self):
        # 根据sectionLine 里面的点的x坐标
        # 绘制分区图像
        # 从左到右绘制图像
        # 每两根线构成一个分区图形
        log('进入了  updata_section_span')
        section_len = len(self.sectionlines)

        if section_len == 0:
            return
        else:
            # 取出当前所有的
            # sections = self.sectionlines.
            sections = list(self.sectionlines)
            # sections.sort()

        dataind = self.lastind
        log("section_len({})".format(sections))
        if section_len % 2 == 0:
            # for line1 in sections
            for i in range(0, section_len, 2):
                section_left = sections[i]
                section_right = sections[i+1]
                # 绘制sectionspan
                log("还是进入画span")
                self.draw_section_span(section_left, section_right)
                log("进入画span")

            pass
        else:
            # 只有一根分区线 和当前的lastind发生反应
            # 获取最后一根加入的曲线
            section_left = self.sectionlines[-1]
            section_right = self.lastind
            if section_right == section_left:
                return
            else:
                if section_left > section_right:
                    section_right, section_left = section_left, section_right

            # 绘制图形
            log("绘制单个span")
            self.draw_section_span(section_left, section_right)
            log("完成span")

            pass
        pass

    def delete(self):

        pass

    def delete_line(self):
        '''
        删除选中的曲线
        1.获得当前选中的曲线
          1). 选中当前曲线对象

          2). 在sectionline数据里面删除当前曲线
          3). 在matplotlib 画布上 移除当前曲线.
        2.调用方法删除
        :return:
        '''
        # 鼠标点击事件
        # 确认点击到的是axvline

        pass


    def delete_section_span(self):

        pass

    def draw_section_span(self, section_left, section_right):
        # 传入两根曲线的x坐标 绘制曲线图像
        # 一种思路是清除屏幕上所有的span
        # 再重新绘制一遍

        # 一种是只绘制当前选中的span
        #  获得选中的span对象 ？ api？
        #  给选中的span 设置数据set_data
        # pass
        # 绘制当前的需要绘制的span
        secleft = section_left
        secright = section_right
        # 仅仅绘制是不行的 还要可以修改
        axvspan = self.ax.axvspan(self.xs[secleft], self.xs[secright], color='g', alpha=0.5)


        pass

    def get_section_line(self):
        # 返回分区曲线的数据
        return self.sectionlines

    def disconnect(self):
        # 断开连接的功能 让曲线不再被选中
        self.figure.canvas.mpl_disconnect(self.cidpress)
        self.figure.canvas.mpl_disconnect(self.cidrelease)
        self.figure.canvas.mpl_disconnect(self.cidclicked)
        self.figure.canvas.mpl_disconnect(self.cidpoint_motion)
        self.figure.canvas.mpl_disconnect(self.cidpointrelease)


        # self.figure.canvas.mpl_disconnect(self.cidmotion)

        # 断开曲线数据
        self.line = None
        self.figure = None
        self.ax = None
        self.line = None

        self.sectionlines = None
        # 获得当前曲线的数据
        self.xs, self.ys = [], []
        self.pressedpoint = None
        # 当前点的序号
        self.lastind = None
        self.text = None
        self.letext = None
        self.selected, = None
        # 分区曲线
        self.selectedLine = None


class DraggableLines:
    def __init__(self, line):
        self.line = line
        self.press = None

        # 当前曲线是否可操作
        self.lock = False
        self.canmove = False
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
        # self.cidmotion = self.line.figure.canvas.mpl_connect(
        #     'motion_notify_event', self.on_motion)
        # self.cidonclick = self.line.figure.canvas.mpl_connect(
        #     'pick_event', self.on_pick)
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

        # 判断当前曲线是够可移动
        if self.canmove is False:
            return
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
        if event.inaxes != self.line.axes: return
        # x0, y0, xpress, ypress = self.press
        # dx = event.xdata - xpress
        # dy = event.ydata - ypress
        # print('x0=%f, xpress=%f, event.xdata=%f, dx=%f, x0+dx=%f' %
        #      (x0, xpress, event.xdata, dx, x0+dx))
        # self.rect.set_x(x0+dx)
        # self.rect.set_y(y0+dy)
        # log("on_clicked 就是这里")
        # 改变鼠标样式
        # 改变线段的样式
        # self.rect.set_marker('.')

        # 曲线的样式为不填充
        # self.rect.set_linestyle('none')
        # 改变鼠标样式
        # 改变线段的样式
        # 选中了该点 设置该点的样式
        self.line.set_marker('.')
        # log('on_pick_point event', event, type(event))
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
        self.line.figure.canvas.draw()

    def on_release(self, event):
        # 鼠标释放时间时 重置数据
        self.press = None
        self.line.figure.canvas.draw()
        # self.line.canvas.flush_events()

    def disconnect(self):
        # 断开连接的功能 让曲线不再被选中
        self.line.figure.canvas.mpl_disconnect(self.cidpress)
        self.line.figure.canvas.mpl_disconnect(self.cidrelease)
        self.line.figure.canvas.mpl_disconnect(self.cidmotion)


def draw_line():

    fig = plt.figure()
    ax = fig.add_subplot(111)
    # rects = ax.bar(range(10), 20*np.random.rand(10))
    drs = []

    X = np.linspace(-np.pi, np.pi, 100, endpoint=True)
    C, S = np.cos(X), np.sin(X)

    xs, ys = X, C
    # 绘制余弦曲线，使用蓝色的、连续的、宽度为 1 （像素）的线条
    line1 = mlines.Line2D(X, C, color="blue", linewidth=1.0, linestyle="-")
    # line1 =[]
    # 绘制正弦曲线，使用绿色的、连续的、宽度为 1 （像素）的线条
    # line2 = ax.plot(X, S, color="green", linewidth=1.0, linestyle="-")
    line2 = mlines.Line2D(X, S, color="green", linewidth=1.0, linestyle="-")
    line1 = line2

    ax.add_line(line1)
    # ax.add_line(line2)

    lines = [line1, line2]

    for lin in ax.lines:
        dr = DraggableLines(lin)
        # log("type lin ", type(lin))
        dr.connect()
        drs.append(dr)
        # log("len ", len(ax.lines))

    prs = []
    # log('type line1', type(line1), line1)
    # log('type line2', type(line2), line2)

    pr = PointBrowser(fig, ax, line1)
    pr.connect()
    # log("type line1", type(line1))
    prs.append(pr)
    # log("len ", len(ax.lines))

    # 设置点为可选中
    for line in ax.lines:
        line.set_picker(5)

    # pr = PointBrowser(fig, ax)
    # pr.connect(line1)
    # prs.append(dr)

    plt.show()


def main():
    draw_line()


if __name__ == '__main__':
    main()
