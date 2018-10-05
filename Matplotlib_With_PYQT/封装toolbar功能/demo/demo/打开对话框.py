
# import os
# import tkFileDialog
#
# default_dir = r"C:\Users\lenovo\Desktop"  # 设置默认打开目录
# fname = tkFileDialog.askopenfilename(title=u"选择文件",
#                                      initialdir=(os.path.expanduser(default_dir)))
#
# print (fname  # 返回文件全路径)
# print (tkFileDialog.askdirectory()  # 返回目录路径)
import win32ui
dlg = win32ui.CreateFileDialog(1)  # 1表示打开文件对话框
# dlg.SetOFNInitialDir('E:/Python')  # 设置打开文件对话框中的初始显示目录
dlg.DoModal()
filename = dlg.GetPathName()  # 获取选择的文件名称
# dlg.GetFileName()
# dlg.GetFileTitle()
# dlg.GetPathName()
# dlg.GetPathNames()
# help(dlg)
# print(filename)
print(filename)

print(dlg.GetFileName(), dlg.GetFileTitle(), dlg.GetPathName(), dlg.GetPathNames())