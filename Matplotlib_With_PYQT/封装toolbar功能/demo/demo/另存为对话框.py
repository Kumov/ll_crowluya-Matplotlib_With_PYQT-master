# import win32ui
#
# dlg = win32ui.CreateFileDialog(0)
# dlg.SetOFNInitialDir("C:")
# flag = dlg.DoModal()
# print(flag)
# if 1 == flag:
#     print(dlg.GetPathName())
# else:
#     print("取消另存为...")


import win32gui
from win32com.shell import shell, shellcon

desktop_pidl = shell.SHGetFolderLocation (0, shellcon.CSIDL_DESKTOP, 0, 0)
pidl, display_name, image_list = shell.SHBrowseForFolder (
  win32gui.GetDesktopWindow (),
  desktop_pidl,
  "Choose a folder",
  0,
  None,
  None
)
print(shell.SHGetPathFromIDList (pidl))
l = shell.SHGetPathFromIDList (pidl)
print(l)



# import os
# import win32gui
# from win32com.shell import shell, shellcon
#
# mydocs_pidl = shell.SHGetFolderLocation (0, shellcon.CSIDL_PERSONAL, 0, 0)
# pidl, display_name, image_list = shell.SHBrowseForFolder (
#   win32gui.GetDesktopWindow (),
#   mydocs_pidl,
#   "Select a file or folder",
#   shellcon.BIF_BROWSEINCLUDEFILES,
#   None,
#   None
# )
#
# if (pidl, display_name, image_list) == (None, None, None):
#   print("Nothing selected")
# else:
#   path = shell.SHGetPathFromIDList (pidl)
#   print("Opening", path)
#   os.startfile (path)