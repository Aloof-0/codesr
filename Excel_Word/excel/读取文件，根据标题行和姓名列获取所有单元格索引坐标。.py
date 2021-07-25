import xlrd
import xlwt
from xlutils.copy import copy

workbook = xlrd.open_workbook('32-案件恢复审调查呈批表.xls')  # 打开工作簿
Data_sheet = workbook.sheets()[0]
row1 = Data_sheet.row_values(0)  # 取出第一行


# col2 = Data_sheet.col_values(1)  # 取出第二列，
# dic_row_s = {str(i): col2[i] for i in
#              range(0, len(col2))}  # 将第二列的每个元素加个序数标记，标记为第二列的列表索引。让名字和列表索引对应，就可以在字典中由名字得行号，即列表索引+1。这里需要的是这个索引
# print(dic_row_s)
# print(dic_col_s)
# mtitle = "爱好"  # 需要修改哪个标题
# mname = "小郭吹雪"  # 需要修改哪个人的
# rindex = "".join([i for i in dic_row_s if dic_row_s[i] == mname])  # 获取要修改的标题所在行的索引
# cindex = "".join([i for i in dic_col_s if dic_col_s[i] == mtitle])  # 获取要修改的那个人所在的列索引
# print(rindex, cindex)  # 获得要修改的单元格的行索引和列索引

# TODO:获取第一行所有单元个索引坐标
dic_col_s = {}
for i in range(0, len(row1)):
    dic_col_s[str(i)] = row1[i]
print(dic_col_s)

print("=======================================================")
# TODO:获取所有单元索引坐标
dic_col = {}
for i in range(Data_sheet.nrows):
    row = Data_sheet.row_values(i)
    for k in range(0, len(row)):
        dic_col[str(k)] = row[k]
    print(dic_col)

# TODO: 列表存入所有单元索引坐标
list_col = []
dic_col = {}
for i in range(Data_sheet.nrows):
    row = Data_sheet.row_values(i)
    for k in range(0, len(row)):
        dic_col[str(k)] = row[k]
        list_col.append(dic_col)
print(list_col)
