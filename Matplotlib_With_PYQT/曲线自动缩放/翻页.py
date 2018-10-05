

import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QStackedWidget

app = QApplication(sys.argv)

window = QMainWindow()
stack = QStackedWidget(parent=window)
label1 = QLabel('label1')
label2 = QLabel('label2')
label3 = QLabel('label3')
stack.addWidget(label1)
stack.addWidget(label2)
stack.addWidget(label3)
print('current', stack.currentIndex())
window.show()

def next():
      stack.setCurrentIndex(stack.currentIndex()+1)
      print('current', stack.currentIndex())

QTimer.singleShot(1000, next)
QTimer.singleShot(2000, next)
QTimer.singleShot(3000, next)
QTimer.singleShot(4000, app.quit)

sys.exit(app.exec_())
# 1.首先拿到frame
# 2.在frame上添加matplotlib
# 3.生成两个图像
# 4.添加到stack
# 5 点击一下显示下一个图像

