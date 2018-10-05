import sys
from UI_MainWindows import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from UI_HELP import Ui_Help



# class MainWindow(QMainWindow, Ui_MainWindow):
#     def __init__(self, parent=None):
#         super(MainWindow, self).__init__(parent)
#         self.setupUi(self)
#         self.action_about.triggered.connect(self.Ui_Help)
#
#
#     def help_window(self):
#         self.window = Ui_Help()
#         print('秀饿了 ')
#         self.window.show()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.action_about.triggered.connect(self.help_window)

    def help_window(self):
        # If you pass a parent (self) will block the Main Window,
        # and if you do not pass both will be independent,
        # I recommend you try both cases.
        widget = QDialog(self)
        ui=Ui_Help()
        ui.setupUi(widget)
        print('秀饿了 ')

        widget.exec_()


class Help(QDialog, Ui_Help):
    def __init__(self, parent=None):
        super(Help, self).__init__(parent)
        self.setupUi(self)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.action_about.triggered.connect(self.help_window)

    def help_window(self):
        # widget = Help()
        # widget.exec_()
        print("danjile help")
        widget = QDialog(self)
        print('danjile ')

        ui = Ui_Help()
        ui.setupUi(widget)
        print('秀饿了 ')
        widget.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())