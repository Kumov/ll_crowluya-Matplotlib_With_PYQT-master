import numpy as np
import matplotlib.pyplot as plt


log = print


fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('click on points')

# line, = ax.plot(np.random.rand(100), 'o', picker=5)  # 5 points tolerance
X = np.linspace(-np.pi, np.pi, 100, endpoint=True)
C, S = np.cos(X), np.sin(X)

# 绘制余弦曲线，使用蓝色的、连续的、宽度为 1 （像素）的线条
line1 = ax.plot(X, C, color="blue", linewidth=1.0, marker='o', linestyle="none")


def onpick(event):
    log('event', event, type(event))
    thisline = event.artist
    xdata = thisline.get_xdata()
    ydata = thisline.get_ydata()
    ind = event.ind
    log('ind,', ind)

    points = tuple(zip(xdata[ind], ydata[ind]))
    print('onpick points:', points)

# 设置线段为可选中， 范围为5（px）
for line in ax.lines:
    line.set_picker(5)


fig.canvas.mpl_connect('pick_event', onpick)

plt.show()