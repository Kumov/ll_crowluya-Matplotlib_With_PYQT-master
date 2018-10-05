class PointBrowser(object):
    """
    选中点并且使其高亮 --   按键‘a’查看前一个点， ‘d’查看后一个点
    """

    def __init__(self):
        self.lastind = 0

        self.text = ax.text(0.05, 0.95, 'selected: none',
                            transform=ax.transAxes, va='top')
        self.selected, = ax.plot([xs[0]], [ys[0]], 'o', ms=12, alpha=0.4,
                                 color='yellow', visible=False)

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


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    X = np.linspace(-np.pi, np.pi, 100, endpoint=True)
    C, S = np.cos(X), np.sin(X)

    X = np.random.rand(100, 200)
    xs = np.mean(X, axis=1)
    ys = np.std(X, axis=1)
    log('xs =',xs, len(xs), type(xs))
    log('ys=', ys)

    # xs = C
    # ys = X

    fig, (ax) = plt.subplots(1, 1)
    ax.set_title('click on point to plot time series')
    line, = ax.plot(xs, ys, 'o', picker=6)  # 5 points tolerance

    log('line = ', type(line), line)

    browser = PointBrowser()

    fig.canvas.mpl_connect('pick_event', browser.onpick)
    fig.canvas.mpl_connect('key_press_event', browser.onpress)

    plt.show()
