# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_fragment_paras.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fragment_Paras(object):
    def setupUi(self, fragment_Paras):
        fragment_Paras.setObjectName("fragment_Paras")
        fragment_Paras.resize(758, 541)
        self.groupBox_Gas_Injection_paras = QtWidgets.QGroupBox(fragment_Paras)
        self.groupBox_Gas_Injection_paras.setGeometry(QtCore.QRect(40, 20, 701, 451))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.groupBox_Gas_Injection_paras.setFont(font)
        self.groupBox_Gas_Injection_paras.setObjectName("groupBox_Gas_Injection_paras")
        self.tableWidget_fragment_Paras = QtWidgets.QTableWidget(self.groupBox_Gas_Injection_paras)
        self.tableWidget_fragment_Paras.setGeometry(QtCore.QRect(30, 20, 631, 361))
        self.tableWidget_fragment_Paras.setObjectName("tableWidget_fragment_Paras")
        self.tableWidget_fragment_Paras.setColumnCount(9)
        self.tableWidget_fragment_Paras.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fragment_Paras.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fragment_Paras.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fragment_Paras.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fragment_Paras.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fragment_Paras.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fragment_Paras.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fragment_Paras.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fragment_Paras.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fragment_Paras.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fragment_Paras.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fragment_Paras.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fragment_Paras.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fragment_Paras.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fragment_Paras.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fragment_Paras.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fragment_Paras.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fragment_Paras.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fragment_Paras.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fragment_Paras.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fragment_Paras.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fragment_Paras.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fragment_Paras.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fragment_Paras.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fragment_Paras.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fragment_Paras.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fragment_Paras.setItem(0, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fragment_Paras.setItem(0, 8, item)
        self.widget = QtWidgets.QWidget(fragment_Paras)
        self.widget.setGeometry(QtCore.QRect(180, 470, 336, 41))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Thermophysical_LastStep = QtWidgets.QPushButton(self.widget)
        self.pushButton_Thermophysical_LastStep.setObjectName("pushButton_Thermophysical_LastStep")
        self.horizontalLayout.addWidget(self.pushButton_Thermophysical_LastStep)
        self.pushButton_oil_para_load = QtWidgets.QPushButton(self.widget)
        self.pushButton_oil_para_load.setObjectName("pushButton_oil_para_load")
        self.horizontalLayout.addWidget(self.pushButton_oil_para_load)
        self.pushButton_oil_para_finish = QtWidgets.QPushButton(self.widget)
        self.pushButton_oil_para_finish.setObjectName("pushButton_oil_para_finish")
        self.horizontalLayout.addWidget(self.pushButton_oil_para_finish)
        self.pushButton_oil_para_next = QtWidgets.QPushButton(self.widget)
        self.pushButton_oil_para_next.setObjectName("pushButton_oil_para_next")
        self.horizontalLayout.addWidget(self.pushButton_oil_para_next)

        self.retranslateUi(fragment_Paras)
        QtCore.QMetaObject.connectSlotsByName(fragment_Paras)

    def retranslateUi(self, fragment_Paras):
        _translate = QtCore.QCoreApplication.translate
        fragment_Paras.setWindowTitle(_translate("fragment_Paras", "分段参数2"))
        self.groupBox_Gas_Injection_paras.setTitle(_translate("fragment_Paras", "分段参数"))
        item = self.tableWidget_fragment_Paras.horizontalHeaderItem(0)
        item.setText(_translate("fragment_Paras", "段名"))
        item = self.tableWidget_fragment_Paras.horizontalHeaderItem(1)
        item.setText(_translate("fragment_Paras", "段长(m)"))
        item = self.tableWidget_fragment_Paras.horizontalHeaderItem(2)
        item.setText(_translate("fragment_Paras", "孔隙度(%)"))
        item = self.tableWidget_fragment_Paras.horizontalHeaderItem(3)
        item.setText(_translate("fragment_Paras", "水平渗透率(m^2)"))
        item = self.tableWidget_fragment_Paras.horizontalHeaderItem(4)
        item.setText(_translate("fragment_Paras", "垂向渗透率(m^2)"))
        item = self.tableWidget_fragment_Paras.horizontalHeaderItem(5)
        item.setText(_translate("fragment_Paras", "原始含油饱和度(无量纲)"))
        item = self.tableWidget_fragment_Paras.horizontalHeaderItem(6)
        item.setText(_translate("fragment_Paras", "初始束缚水饱和度(无量纲)"))
        item = self.tableWidget_fragment_Paras.horizontalHeaderItem(7)
        item.setText(_translate("fragment_Paras", "束缚水饱和度增量(无量纲)"))
        item = self.tableWidget_fragment_Paras.horizontalHeaderItem(8)
        item.setText(_translate("fragment_Paras", "最大可动油饱和度(无量纲)"))
        __sortingEnabled = self.tableWidget_fragment_Paras.isSortingEnabled()
        self.tableWidget_fragment_Paras.setSortingEnabled(False)
        self.tableWidget_fragment_Paras.setSortingEnabled(__sortingEnabled)
        self.pushButton_Thermophysical_LastStep.setText(_translate("fragment_Paras", "上一步"))
        self.pushButton_oil_para_load.setText(_translate("fragment_Paras", "读入参数"))
        self.pushButton_oil_para_finish.setText(_translate("fragment_Paras", "完成"))
        self.pushButton_oil_para_next.setText(_translate("fragment_Paras", "下一步"))
