from docxtpl import DocxTemplate
import docxtpl

doc = DocxTemplate("../data/50-XXX室集体讨论记录.docx")


def word50(time, occupation, men, mens):
    context = {
        'time': time,
        'occupation': occupation,
        'men': men, 'mens': mens
    }
    doc.render(context)
    doc.save("张三.docx")


word50(time="2020.5.12", occupation='广东省禅城区', men="大苏打", mens="sd")
