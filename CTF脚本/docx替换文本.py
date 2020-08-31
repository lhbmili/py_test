#coding: utf-8
import os, sys
# 安装docx： pip install python_docx
from docx import Document
from docx.shared import Inches

s = os.path.join(sys.path[0], r"2链接信息表 （第二税务分局）")
file_name_list = os.listdir(s)
for file_name in file_name_list:
    file_name = "".join((s,"\\",file_name))
    # print(file_name)

#创建 Document 对象，相当于打开一个 word 文档
doc = Document(file_name)


# 参考：https://www.zhihu.com/question/64235925
def replaceStr(old_text, new_text):
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                if old_text in cell.text:
                    print("row:%s,cell:%s" %(type(row),type(cell)))
                    print(cell.text)
                    cell.text = cell.text.replace(old_text, new_text)                 
old_text = "（点击展示条款内容）"
new_text = ""
replaceStr(old_text, new_text)

#保存文本
doc.save("%s.docx" % file_name)