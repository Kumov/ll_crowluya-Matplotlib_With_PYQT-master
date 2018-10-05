from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox


def f(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)


class Draw(QWidget):

    def __init__(self):
        super().__init__()
        self.main_frame()

    def main_frame(self):
        t1 = np.arange(0, 5, 0.1)
        t2 = np.arange(0, 5, 0.02)
        self.fig = Figure((5, 4), dpi=100)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self)

        self.ax1 = self.fig.add_subplot(111)
        self.ax1.plot(t1, f(t1), 'bo', t2, f(t2), 'r--')

        self.ax2 = self.fig.add_subplot(111)
        self.ax2.plot(t2, np.cos(2 * np.pi * t2), 'r--')

        self.ax3 = self.fig.add_subplot(211)
        self.ax3.plot([1, 2, 3, 4], [1, 4, 9, 16])

        # Create the navigation toolbar, tied to the canvas
        #
        self.mpl_toolbar = NavigationToolbar(self.canvas, self)
        self.ax2.set_visible("false")

        self.canvas.draw()

        self.show()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dlg = Draw()
    dlg.show()
    app.exec_()
