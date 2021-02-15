import time
from datetime import datetime, timedelta

# 1.生成10位时间戳【秒】
timestamp = time.time()
print("10位时间戳:", timestamp)

# 2.将时间戳转换成日期时间格式
date = datetime.fromtimestamp(timestamp)
print("日期：", date)
print("类型：", type(date))

# 3.将日期转换成日期字符串
# 方案1：标准日期字符串
date_str = datetime.isoformat(date)
# date.isoformat()
print("日期字符串:", date_str)

# 方案2：将日期转换成自定义格式的字符串
date_str1 = datetime.strftime(date, "%Y-%m-%d %H:%M:%S")
print("自定义格式的时间字符串：", date_str1)

# 4.将日期字符串转换成日期
date1 = datetime.strptime(date_str1, "%Y-%m-%d %H:%M:%S")
print("日期：", date1)

# 5.将日期转换成时间戳
timestamp1 = datetime.timestamp(date)
timestamp2 = date.timestamp()

print("时间戳：", timestamp1, timestamp2)
