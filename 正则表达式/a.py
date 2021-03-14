import re

a = "//static.qiushibaike.com/images/web/v4/left_code.png?v=0a1153c06294049ad2da58efa408072e"

d = re.sub(r"\D", "", a)

print(d)