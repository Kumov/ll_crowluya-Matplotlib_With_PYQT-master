'''
# 9.3 任务
3.2 放大模式	✔
    选中放大 鼠标左键放大
3.3 缩小模式   ✔
    选中放大 鼠标右键缩小

3.4 X轴放大模式  ✔
    选中放大 按住x键 x轴放大

3.5 Y轴放大模式  ✔
    选中放大 按住y键 y轴放大

3.6 移动画布模式	✔

3.1 选择模式
# 选中区域内的曲线上大点
# 点的样式改变 鼠标样式改变

3.8 移动曲线模式 ✔
    移动曲线 -->选中曲线 曲线形态不变 曲线坐标跟随变化


3.7 分区编辑模型

3.9 坐标锁定模式

3.10 edit 点
    编辑x轴点 左右上限
    编辑Y轴点 无上限
    编辑x，y轴


# 使用matplotlib的快捷键实现



VisPy 学习
 百度 google
	YouTube
	官方文档

# python 图文混排
    1.暂时停止
# 	1. python docx
        python-docx包  https://python-docx.readthedocs.io/en/latest/  用的最多的
            创建docx文档， 图文等word文档中能常用的功能都支持 修改功能不强
             python docx库使用样例   https://blog.csdn.net/u011932355/article/details/51769803/
            python操作docx文档  https://blog.csdn.net/sinat_37005367/article/details/77855359

        python-docx-template https://docxtpl.readthedocs.io/en/latest/
            对docx文档进行修改 jinjia2模板语言结合

        pandoc https://pandoc.org/
            文本格式转换 docx -->pdf

        docx-mailmerge
            可用于动态生成数据报告，类似于公司word版工资条的生成
             http://pbpython.com/python-word-template.html        Populating MS Word Templates with Python
             http://chuansong.me/n/1608675952516   利用Python实现报告自动生成
             https://pypi.org/project/docx-mailmerge/ 文档

# 	2. python pdf
        PDFMiner  针对内容提取的 处理字体或图像
        pip3 install pdfminer3k

          官方文档  http://www.unixuser.org/~euske/python/pdfminer/programming.html
         Python使用PDFMiner解析PDF    https://www.cnblogs.com/jamespei/p/5339769.html
        PyPDF2
            官方文档 https://pythonhosted.org/PyPDF2/
            PyPDF2可以从PDF文件中提取数据，或者操纵现有的PDF来生成新文件
            PyPDF2 处理 PDF 文件 https://blog.csdn.net/xingxtao/article/details/79056341

            如果只折腾现成的PDF文件,用pyPdf,如果要生成新内容的PDF文件用ReportLab,如果要分析现有PDF文件的内容,用PDFMiner
    3. Sphinx python  生成文档 文档就是用这个写的 但是现在我们用不到

    最后决定使用python-docx 创建docx文档   pandoc 进行文本格式转换 docx -->pdf


'''
