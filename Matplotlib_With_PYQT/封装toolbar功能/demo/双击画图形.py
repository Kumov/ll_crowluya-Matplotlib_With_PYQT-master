import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set(title='Click Twice', xlabel='X', ylabel='Y')

point1, point2 = fig.ginput(2) # Or equivalently, "plt.ginput"

ax.autoscale(False)
ax.axvspan(point1[0], point2[0], color='g', alpha=0.5)
fig.canvas.draw()

plt.show()