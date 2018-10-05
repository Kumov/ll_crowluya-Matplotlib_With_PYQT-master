import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
# 从 −π−π 到 +π+π 等间隔的 256 个值
mpl.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
mpl.rcParams['axes.unicode_minus']=False #用来正常显示负号
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)




plt.figure(figsize=(10,6), dpi=80)

xmin ,xmax = X.min(), X.max()
ymin, ymax = C.min(), C.max()

dx = (xmax - xmin) * 0.2
dy = (ymax - ymin) * 0.2

plt.xlim(xmin - dx, xmax + dx)
plt.ylim(ymin - dy, ymax + dy)

plt.xticks( [-np.pi, -np.pi/2, 0, np.pi/2, np.pi]) # 设置x轴坐标点
plt.yticks([-1, 0, +1]) # 设置y轴坐标点

plt.plot(X, C, color='blue', linewidth=2.5, linestyle='-')
plt.plot(X, S, color="red",  linewidth=2.5, linestyle="-")
plt.show()