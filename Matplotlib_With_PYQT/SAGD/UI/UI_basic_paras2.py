# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_basic_paras2.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_basic_Paras2(object):
    def setupUi(self, basic_Paras2):
        basic_Paras2.setObjectName("basic_Paras2")
        basic_Paras2.resize(585, 432)
        self.groupBox_Gas_Injection_paras = QtWidgets.QGroupBox(basic_Paras2)
        self.groupBox_Gas_Injection_paras.setGeometry(QtCore.QRect(60, 20, 471, 111))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.groupBox_Gas_Injection_paras.setFont(font)
        self.groupBox_Gas_Injection_paras.setObjectName("groupBox_Gas_Injection_paras")
        self.lineEdit_para_P_s = QtWidgets.QLineEdit(self.groupBox_Gas_Injection_paras)
        self.lineEdit_para_P_s.setGeometry(QtCore.QRect(220, 30, 71, 21))
        self.lineEdit_para_P_s.setObjectName("lineEdit_para_P_s")
        self.label = QtWidgets.QLabel(self.groupBox_Gas_Injection_paras)
        self.label.setGeometry(QtCore.QRect(150, 30, 61, 21))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_para_Xs = QtWidgets.QLineEdit(self.groupBox_Gas_Injection_paras)
        self.lineEdit_para_Xs.setGeometry(QtCore.QRect(220, 70, 71, 21))
        self.lineEdit_para_Xs.setObjectName("lineEdit_para_Xs")
        self.label_12 = QtWidgets.QLabel(self.groupBox_Gas_Injection_paras)
        self.label_12.setGeometry(QtCore.QRect(10, 70, 201, 21))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_2 = QtWidgets.QLabel(self.groupBox_Gas_Injection_paras)
        self.label_2.setGeometry(QtCore.QRect(300, 30, 41, 21))
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(basic_Paras2)
        self.widget.setGeometry(QtCore.QRect(100, 390, 336, 41))
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
        self.groupBox_Wellbore_paras = QtWidgets.QGroupBox(basic_Paras2)
        self.groupBox_Wellbore_paras.setGeometry(QtCore.QRect(60, 150, 471, 111))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.groupBox_Wellbore_paras.setFont(font)
        self.groupBox_Wellbore_paras.setObjectName("groupBox_Wellbore_paras")
        self.lineEdit_para_Rwellbore = QtWidgets.QLineEdit(self.groupBox_Wellbore_paras)
        self.lineEdit_para_Rwellbore.setGeometry(QtCore.QRect(220, 30, 71, 21))
        self.lineEdit_para_Rwellbore.setObjectName("lineEdit_para_Rwellbore")
        self.label_3 = QtWidgets.QLabel(self.groupBox_Wellbore_paras)
        self.label_3.setGeometry(QtCore.QRect(150, 30, 61, 21))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_para_well_T_L = QtWidgets.QLineEdit(self.groupBox_Wellbore_paras)
        self.lineEdit_para_well_T_L.setGeometry(QtCore.QRect(220, 70, 71, 21))
        self.lineEdit_para_well_T_L.setObjectName("lineEdit_para_well_T_L")
        self.label_13 = QtWidgets.QLabel(self.groupBox_Wellbore_paras)
        self.label_13.setGeometry(QtCore.QRect(140, 70, 71, 21))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(9)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_4 = QtWidgets.QLabel(self.groupBox_Wellbore_paras)
        self.label_4.setGeometry(QtCore.QRect(300, 30, 41, 21))
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.groupBox_Wellbore_paras)
        self.label_7.setGeometry(QtCore.QRect(300, 70, 51, 21))
        self.label_7.setObjectName("label_7")
        self.groupBox_Count_control_paras = QtWidgets.QGroupBox(basic_Paras2)
        self.groupBox_Count_control_paras.setGeometry(QtCore.QRect(60, 270, 471, 111))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.groupBox_Count_control_paras.setFont(font)
        self.groupBox_Count_control_paras.setObjectName("groupBox_Count_control_paras")
        self.lineEdit_para_total_time_T = QtWidgets.QLineEdit(self.groupBox_Count_control_paras)
        self.lineEdit_para_total_time_T.setGeometry(QtCore.QRect(220, 30, 71, 21))
        self.lineEdit_para_total_time_T.setReadOnly(True)
        self.lineEdit_para_total_time_T.setObjectName("lineEdit_para_total_time_T")
        self.label_5 = QtWidgets.QLabel(self.groupBox_Count_control_paras)
        self.label_5.setGeometry(QtCore.QRect(160, 30, 41, 21))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_para_time_step_dt = QtWidgets.QLineEdit(self.groupBox_Count_control_paras)
        self.lineEdit_para_time_step_dt.setGeometry(QtCore.QRect(220, 70, 71, 21))
        self.lineEdit_para_time_step_dt.setReadOnly(True)
        self.lineEdit_para_time_step_dt.setObjectName("lineEdit_para_time_step_dt")
        self.label_14 = QtWidgets.QLabel(self.groupBox_Count_control_paras)
        self.label_14.setGeometry(QtCore.QRect(150, 70, 61, 20))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(9)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_6 = QtWidgets.QLabel(self.groupBox_Count_control_paras)
        self.label_6.setGeometry(QtCore.QRect(300, 30, 41, 21))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(basic_Paras2)
        QtCore.QMetaObject.connectSlotsByName(basic_Paras2)

    def retranslateUi(self, basic_Paras2):
        _translate = QtCore.QCoreApplication.translate
        basic_Paras2.setWindowTitle(_translate("basic_Paras2", "基础参数2"))
        self.groupBox_Gas_Injection_paras.setTitle(_translate("basic_Paras2", "注气参数"))
        self.label.setText(_translate("basic_Paras2", "注汽压力"))
        self.label_12.setText(_translate("basic_Paras2", "饱和蒸汽温度下注入井底蒸汽的干度"))
        self.label_2.setText(_translate("basic_Paras2", "MPa"))
        self.pushButton_Thermophysical_LastStep.setText(_translate("basic_Paras2", "上一步"))
        self.pushButton_oil_para_load.setText(_translate("basic_Paras2", "读入参数"))
        self.pushButton_oil_para_finish.setText(_translate("basic_Paras2", "完成"))
        self.pushButton_oil_para_next.setText(_translate("basic_Paras2", "下一步"))
        self.groupBox_Wellbore_paras.setTitle(_translate("basic_Paras2", "井筒参数"))
        self.label_3.setText(_translate("basic_Paras2", "井筒半径"))
        self.label_13.setText(_translate("basic_Paras2", "井筒的温度"))
        self.label_4.setText(_translate("basic_Paras2", "m"))
        self.label_7.setText(_translate("basic_Paras2", "摄氏度"))
        self.groupBox_Count_control_paras.setTitle(_translate("basic_Paras2", "计算控制参数"))
        self.label_5.setText(_translate("basic_Paras2", "总时间"))
        self.label_14.setText(_translate("basic_Paras2", "时间步长"))
        self.label_6.setText(_translate("basic_Paras2", "天"))

