import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines


from function.dragline import DraggableLines


fig = plt.figure()
ax = fig.add_subplot(111)
# rects = ax.bar(range(10), 20*np.random.rand(10))
# 换成曲线
X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)
#
# # 绘制余弦曲线，使用蓝色的、连续的、宽度为 1 （像素）的线条
line1 = ax.plot(X, C, color="blue", linewidth=1.0, linestyle="-")
#
# # 绘制正弦曲线，使用绿色的、连续的、宽度为 1 （像素）的线条
# line2 = ax.plot(X, S, color="green", linewidth=1.0, linestyle="-")

drs = []
for rect in line1:
    dr = DraggableLines(rect)
    dr.connect()
    drs.append(dr)

plt.show()


