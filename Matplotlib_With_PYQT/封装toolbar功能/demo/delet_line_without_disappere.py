from matplotlib import pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(np.random.rand(10))


def OnClick(event):
    print ('button=%d, x=%d, y=%d, xdata=%f, ydata=%f'%(
        event.button, event.x, event.y, event.xdata, event.ydata))

def OnOver(event):
    x = event.xdata
    y = event.ydata
    ax.axhline(y)
    ax.axvline(x)
    plt.draw()


did = fig.canvas.mpl_connect('motion_notify_event', OnOver)
#iii = fig.canvas.mpl_disconnect(did) # get rid of the click-handler
cid = fig.canvas.mpl_connect('button_press_event', OnClick)

plt.show()