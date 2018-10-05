# -*- coding: utf-8 -*-
'''
    【简介】


'''
import sys
import os
import PyQt5.sip
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from openpyxl import Workbook

log = print


class filedialogdemo(QWidget):
    def __init__(self, parent=None):
        super(filedialogdemo, self).__init__(parent)
        layout_grid = QGridLayout()
        # layout_grid.setHorizontalSpacing(2)
        # layout_grid.setVerticalSpacing(2)

        # self.text_load = QTextBrowser()width
        self.text_load = QLineEdit()
        # log(" 是1QTxt")
        self.text_load.resize(100, 100)
        self.text_load.setReadOnly(True)
        # self.text_load
        layout_grid.addWidget(self.text_load, 0, 1)
        # layout_grid.addChildWidget(self.text_load)

        btn_load = QPushButton("选择txt路径")
        btn_load.clicked.connect(self.getLoadFileWithPath)
        layout_grid.addWidget(btn_load, 0, 0)

        # self.text_save = QTextBrowser()
        self.text_save = QLineEdit()
        self.text_save.setReadOnly(True)
        layout_grid.addWidget(self.text_save, 1, 1)
        btn_save = QPushButton("选择保存路径")
        btn_save.clicked.connect(self.getSaveFileWithPath)
        # 选定保存位置之后立刻处理文件
        btn_save.clicked.connect(self.processFile)
        # btn_process.clicked.connect(self.process_txt_data)

        layout_grid.addWidget(btn_save, 1, 0)

        # self.save_excle_btn = QPushButton("保存excel")
        # self.save_excle_btn.clicked.connect(self.save_excel_file)
        # layout.addWidget(self.save_excle_btn)

        btn_process = QPushButton("保存为txt文件")
        # btn_process.clicked.connect(self.process_txt_data)
        btn_process.clicked.connect(self.savaWellDatasAsTxt)
        layout_grid.addWidget(btn_process, 2, 0)

        btn_process = QPushButton("保存为excel文件")
        btn_process.clicked.connect(self.savaWellDatasAsExcel)
        layout_grid.addWidget(btn_process, 2, 3)

        self.setLayout(layout_grid)
        self.resize(630, 220)
        # self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("录井分割器")
        # 初始化，以便于后面进行判断
        self.loadedFileName = ''
        self.saveDirPath = ''
        self.processedDictWellDates = ''
        self.wall_header = ''

    def getLoadFileWithPath(self):
        log(" 点击getLoadFileWithPath（）")
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter(QDir.Files)
        if dlg.exec_():
            filenames = dlg.selectedFiles()
            self.loadedFileName = filenames[0]
            log("加载的文件filename({})".format(self.loadedFileName))
            self.text_load.setText(self.loadedFileName)
            self.end_with_txt()
            return filenames[0]

    def end_with_txt(self):
        end = os.path.splitext(self.loadedFileName)[1]
        log("end", end)
        # acc
        allowed_end = '.txt'
        if end != allowed_end:
            log('文件名字', self.loadedFileName)
            # self.loadedFileName.split()
            QMessageBox.warning(self,  # 使用infomation信息框
                                "操作错误",
                                "请选择txt格式文件！",
                                QMessageBox.Ok)
            self.text_load.setText("")
            return

    def getSaveFileWithPath(self):
        # fname, _ = QFileDialog.getSaveFileName(self,
        #                                              "文件保存",
        #                                              "d:/",
        #                                              "Text Files (*.txt)")
        # 这里不是选择文件夹，是选择路径，参考：https: // blog.csdn.net / jirryzhang / article / details / 59088964
        self.saveDirPath = QFileDialog.getExistingDirectory()
        # self.le.setPixmap(QPixmap(fname))
        #
        # # 获取保存的文件夹地址
        # [dirname, filename] = os.path.split(fname)
        # print(dirname, "\n", filename)
        # self.saveDirPath = dir_path
        # self.xlsx_to_txt()
        # log('保存文件路径为({})'.format(self.saveDirPath))
        self.text_save.setText(self.saveDirPath)

    def processFile(self):
        log(" 点击processFile（）")

        if '' == self.loadedFileName:
            log('文件名字', self.loadedFileName)
            # self.loadedFileName.split()
            QMessageBox.warning(self,  # 使用infomation信息框
                                "操作错误",
                                "请选择输入文件！",
                                QMessageBox.Ok)
            end = os.path.splitext(self.loadedFileName)[1]
            log("end", end)
            return
        if '' == self.saveDirPath:
            QMessageBox.warning(self,  # 使用infomation信息框
                                "操作错误",
                                "请选择输出文件路径！",
                                QMessageBox.Ok)
            return
        # https: // www.cnblogs.com / jhao / p / 7243043.html
        if not (os.path.exists(self.loadedFileName)):
            QMessageBox.warning(self,  # 使用infomation信息框
                                "操作错误",
                                "输入文件非法！",
                                QMessageBox.Ok)
            return
        if not (os.path.exists(self.saveDirPath)):
            QMessageBox.warning(self,  # 使用infomation信息框
                                "操作错误",
                                "输出路径非法！",
                                QMessageBox.Ok)
            return
        # 是否是txt文件


        ifSuccess = self.process_loaded_txt_data()
        if ifSuccess:
            self.msg_process_success()
        pass

    def process_raw_wall(self, sourceInLine):
        # sourceInLine 是文件数据流
        # 打开文件后 处理每一行井的数据
        # 处理txt井数据
        # 井名字用dict存放 井数据用list存放

        dictWellData = {}  # 一个井一个字典值，防重复
        # iLineNum 当前行计数器
        iLineNum = 0
        for line in sourceInLine:
            iLineNum = iLineNum + 1
            if 1 == iLineNum:  # 第一行是标题，丢掉
                temp1 = line.strip('\n')
                temp2 = temp1.strip().split('\t')  # 去除空白、逗号“,”、tab
                self.wall_header = temp2
                continue
            temp1 = line.strip('\n')
            temp2 = temp1.strip().split('\t')  # 去除空白、逗号“,”、tab

            # temp1 temp2保存的是当前行的信息 如下
            #  temp1 =(Z169-34	1970.3	2) temp2=(['Z169-34', '1970.3', '2'])
            # log("temp1 =({}) temp2=({})".format(temp1,temp2))
            if temp2 == ['']:  # 防有空格的空行
                log('debug：文件第%d行是空行'.format(iLineNum))

                continue
            if len(temp2) != 3:  # 3列数据才对
                log('debug：文件第%d行格式有错误'.format(iLineNum))

                continue
            temp2[1] = float(temp2[1])
            temp2[2] = int(temp2[2])

            if temp2[0] in dictWellData.keys():
                dictWellData[temp2[0]].append([temp2[1], temp2[2]])
            else:
                dictWellData[temp2[0]] = []
                dictWellData[temp2[0]].append([temp2[1], temp2[2]])

        # 保存处理后的井的数据
        self.processedDictWellDates = dictWellData
        print(dictWellData)

        return dictWellData
        pass

    def savaWellDatasAsTxt(self):
        # 根据不重复的井名
        # 处理txt中所有井的数据
        # 根据井名保存为不同txt 保存路径为已选定的文件夹地址
        # (例如: Z164-56 --> Z164-56井.txt)

        if '' == self.processedDictWellDates:
            log('没有处理过的数据')
            # self.msg_process_success(msg='没有处理过的数据')
            QMessageBox.warning(self,  # 使用infomation信息框
                                "操作错误",
                                "没有处理过的数据！",
                                QMessageBox.Ok)
            return False
            pass
        else:
            dictWellData = self.processedDictWellDates

        dirPath = self.saveDirPath

        for strWellName in dictWellData.keys():  # 遍历所有井，参考https://www.cnblogs.com/stuqx/p/7291948.html
            fileName = os.path.join(dirPath,
                                    strWellName + '.txt')  # https://blog.csdn.net/qq_42034590/article/details/80031241
            f1 = open(fileName, 'w')
            listData = dictWellData[strWellName]
            for i in range(len(listData)):
                # strTemp="%f\t%d\n"%(listData[i][0],listData[i][1])
                strTemp = str(listData[i][0]) + "\t" + str(listData[i][1]) + "\n"
                f1.write(strTemp)

        QMessageBox.about(self,  # 使用infomation信息框
                          "消息提示",
                          "保存为txt成功！", )
        return True
        pass

    def savaWellDatasAsExcel(self):

        if '' == self.processedDictWellDates:
            log('没有处理过的数据')
            # self.msg_process_success(msg='没有处理过的数据')
            QMessageBox.warning(self,  # 使用infomation信息框
                                "操作错误",
                                "没有处理过的数据！",
                                QMessageBox.Ok)
            return False
            pass
        else:
            dictWellData = self.processedDictWellDates

        dirPath = self.saveDirPath

        # 保存当前数据到excel中
        # 创建excel文档
        # wb = Workbook()
        # ws = wb.active
        # row = ([1, ])
        # ws.append(row)
        # ws.append([1, 2, 3])
        # wb.save("sample.xlsx")

        for strWellName in dictWellData.keys():  # 遍历所有井保存为excel
            fileName = os.path.join(dirPath,
                                    strWellName + '.xlsx')  # https://blog.csdn.net/qq_42034590/article/details/80031241

            listData = dictWellData[strWellName]

            # # 井头信息 确定不添加
            # if '' == self.wall_header:
            #     pass
            # else:
            #     wall_header = self.wall_header
            wb = Workbook()
            ws = wb.active
            # 保存当前井数据到excel
            # 添加井头
            # ws.append(wall_header)
            for row in listData:
                ws.append(row)
            wb.save(fileName)
        QMessageBox.about(self,  # 使用infomation信息框
                          "消息提示",
                          "保存为excel成功！", )
        return True
        pass

    def process_loaded_txt_data(self):
        loadedFileName = self.loadedFileName
        dirPath = self.saveDirPath

        assert os.path.exists(loadedFileName)
        assert os.path.exists(dirPath)

        # 对padas不熟悉，就用最简单的，参考： https: // blog.csdn.net / xiaopihaierletian / article / details / 72530682

        # 打开文本数据
        # 处理txt井数据
        # 井名字用dict存放 井数据用list存放
        with open(loadedFileName, 'r') as f:
            # f = open(loadedFileName, "r")
            sourceInLine = f.readlines()  # 读取全部内容
            self.process_raw_wall(sourceInLine)
            # dictWellData = self.processedDictWellDates

    def msg_box(self, msg=''):
        # https: // blog.csdn.net / a359680405 / article / details / 45152131
        # 弹出关于此软件的信息
        # msgs = """ 文件处理:
        # s
        #         操作处理成功
        #         """
        titel = '操作提示'
        QMessageBox.information(self, titel, msg)


def test():
    # app = QApplication(sys.argv)
    # ex = filedialogdemo()
    # ex.process_file()

    log("测试完成")


# 1.加载excel数据
# 2.根据excel数据切割


if __name__ == '__main__':
    # # https: // blog.csdn.net / Avada_533 / article / details / 78762773
    # Back up the reference to the exceptionhook
    sys._excepthook = sys.excepthook


    def my_exception_hook(exctype, value, traceback):
        # Print the error and traceback
        print(exctype, value, traceback)
        # Call the normal Exception hook after
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)


    # Set the exception hook to our wrapping function
    sys.excepthook = my_exception_hook

    app = QApplication(sys.argv)
    ex = filedialogdemo()
    ex.show()

    sys.exit(app.exec_())
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")