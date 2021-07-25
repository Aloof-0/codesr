import xlrd
import xlwt
from xlutils.copy import copy
# 打开想要更改的excel文件
old_excel = xlrd.open_workbook('32-案件恢复审调查呈批表.xls', formatting_info=True)
# 将操作文件对象拷贝，变成可写的workbook对象
new_excel = copy(old_excel)
# 获得第一个sheet的对象
ws = new_excel.get_sheet(0)

# 写入数据
ws.write(4, 1, '第一行，第一列')
ws.write(5, 1, '第一行，第二列')
ws.write(5, 3, '第一行，第三列')
ws.write(6, 1, '第二行，第一列')
ws.write(6, 3, '第二行，第二列')
ws.write(7, 1, '第二行，第三列')
# 另存为excel文件，并将文件命名，可以重新命名，应该也可以覆盖掉
new_excel.save('new_mcw_test.xls')

