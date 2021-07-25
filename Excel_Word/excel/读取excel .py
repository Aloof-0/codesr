import xlrd
# 创建一个workbook 设置编码

data = xlrd.open_workbook("32-案件恢复审调查呈批表.xls")


table = data.sheet_by_index(0)  # 通过索引顺序获取sheet

print(table.name)  # sheet名

print(table.ncols)  # sheet列数

print(table.nrows)  # sheet行数

print(table.row(1))  # 返回由rowx行中所有的单元格对象组成的列表

'''
获取rowx行第一个单元格的类型
0. empty（空的）,1 string（text）, 2 number, 3 date, 4 boolean, 5 error， 6 blank（空白表格）
'''

print(table.row(0)[0].value)  # TODO: 读取第一行第一个单元格的值
print(table.row(2)[0].value)  # TODO: 读取第二行第一个单元格的值


for i in range(table.nrows):  # TODO:循环输出单元格
    print(table.row(i)[0].value)


