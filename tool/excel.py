import xlrd

filePath = "/Users/chenbing/github/python/tool/1.xls"
workbook = xlrd.open_workbook(filePath)

sheet_names= workbook.sheet_names()

for sheet_name in sheet_names:

	sheet2 = workbook.sheet_by_name(sheet_name)

	print(sheet_name )

	rows = sheet2.row_values(3) # 获取第四行内容

	cols = sheet2.col_values(1) # 获取第二列内容

	print(rows)

	print(cols)