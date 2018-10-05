from openpyxl import Workbook
wb = Workbook()
ws = wb.active
row = ([1,])
ws.append(row)
ws.append([1, 2, 3])
wb.save("sample.xlsx")