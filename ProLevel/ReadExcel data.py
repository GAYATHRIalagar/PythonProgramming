import xlrd
workbook = xlrd.open_workbook("file.xlsx")
worksheet = workbook.sheet_by_index(0)
print("the value at row 4 and column 2 is :{0}".format(worksheet.cell(4,2).value))
