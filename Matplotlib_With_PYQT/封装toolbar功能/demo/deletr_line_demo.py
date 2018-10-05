from matplotlib import pyplot as plt
import numpy as np


log = print


fig = plt.figure()
ax = fig.add_subplot(211)
ax.plot(np.random.rand(10))

ax = fig.add_subplot(212)
ax.plot(np.random.rand(15))


def OnClick(event):
    print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f'%(
        event.button, event.x, event.y, event.xdata, event.ydata))


def OnOver(event):
   if len(ax.lines) > 1 :
      log('ax.lines', ax.lines, type(ax.lines))

      ax.lines[-1].remove()
      ax.lines[-1].remove()
   ax.axhline(event.ydata)
   ax.axvline(event.xdata)
   plt.draw()

lhor = ax.axhline (0.5)
lver = ax.axvline (1)
def OnOver2(event):
   lhor.set_ydata(event.ydata)
   lver.set_xdata(event.xdata)
   plt.draw()


did = fig.canvas.mpl_connect('motion_notify_event', OnOver2)
#iii = fig.canvas.mpl_disconnect(did) # get rid of the click-handler
cid = fig.canvas.mpl_connect('button_press_event', OnClick)
plt.show()
