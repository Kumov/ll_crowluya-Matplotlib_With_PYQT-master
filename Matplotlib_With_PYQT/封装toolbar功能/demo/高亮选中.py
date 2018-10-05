import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines


log = print


class HighlightSelected(lines.VertexSelector):
    def __init__(self, line, fmt='ro', **kwargs):
        lines.VertexSelector.__init__(self, line)
        self.point = None
        self.markers, = self.axes.plot([], [], fmt, **kwargs)

    def process_selected(self, ind, xs, ys):
        self.markers.set_data(xs, ys)
        self.line.linestyle="None"
        log('ind', ind, xs, ys)
        self.canvas.draw()
    # 设置拖动曲线


fig, ax = plt.subplots()
# x, y = np.random.rand(2, 30)
# line, = ax.plot(x, y, )

X = np.linspace(-np.pi, np.pi, 100, endpoint=True)
C, S = np.cos(X), np.sin(X)

xs, ys = X, C
# 绘制余弦曲线，使用蓝色的、连续的、宽度为 1 （像素）的线条
line, = ax.plot(X, C, 'bs', picker=5)
# line1, = lines.Line2D(X, C, 'bs-', picker=5 , linestyle="None")

selector = HighlightSelected(line)
plt.show()
