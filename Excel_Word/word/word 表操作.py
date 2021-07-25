from docx import Document

# %cd D:YanZan_python2018word

from docx import Document
from docx.enum.text import WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt  # 磅数
from docx.oxml.ns import qn  # 中文格式
from docx.shared import Inches  # 图片尺寸

document = Document("../table/11-函询通知书.docx")
tables = document.tables
document.styles['Normal'].font.name = u'黑体'
document.styles['Normal'].font.size = Pt(16)
document.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'黑体')

table = tables[0]  # 获取文件中的第9个表格
# for i in range(1, len(table.rows)):#从表格第二行开始循环读取表格数据
#         idNum = table.cell(i,0).text #序号
#         print(idNum)
#         companyName = table.cell(i,1).text  #控股企业名称
#         investmentRate = table.cell(i,2).text   #投资比例
#         stock= table.cell(i,3).text  #股权链

# print(table.cell(0, 2).text)
table.cell(0, 2).text = "御文耀"  # 姓名
table.cell(0, 4).text = "18696969694"
table.cell(1, 2).text = "中国电信营业部经理"
table.cell(2, 2).text = "44089898989856565245"
table.cell(3, 1).text = "为了进一步做好人才开发资金资助工作，根据各地在上报申请资助材料时存在的不够完整、规范，有些事项还不够清楚的实际状况，说明和强调几个具体问题。一、申报人才开发资金必须提供的资料二、申报材料必须提供的内容三、资助申请书必须按要求规范填写四、审核上报资助材料必须明确的问题五、" \
                        "对上报申请资助材料提出几点要求一、　 申报省人才开发资金资助必须提供的资料1、提供评审工作报告。将地区或部门对申报项目的评审情况、评审过程、时间、" \
                        "参评专家及有关人员、评审结果或意见等，形成书面材料。一式一份。2、提供《吉林省人才开发资金申请情况一览表》和电子光盘。"
table.cell(4, 1).text = "所谓“上”就是各级政府党员干部。应该看到，形式主义、官僚主义、享乐主义和奢靡之风虽然只是在个别领域存在，但是“千里之堤毁于蚁穴”，我们要防微杜渐、未雨绸缪，克服各种脱离群众的不良现象，就必须从上级部门做起，率先垂范。这一点，党中央做出了杰出的表率。中央政治局按照“照镜子、正衣冠、洗洗澡、" \
                       "治治病”的总要求，以身作则，自上而下在全党深入开展，起到很好的示范带头作用，各促进了党风政风转变，带动了社会风气的明显好转，让人民群众切实得到了实惠。"

c = table.cell(5, 1).text
a = "dasdasd"
b = a + c
table.cell(5, 1).text = b
document.save("asd.docx")