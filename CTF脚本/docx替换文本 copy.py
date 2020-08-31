#coding: utf-8
import os, sys
# 安装docx： pip install python_docx
from docx import Document
from docx.shared import Inches


def getFilePath():
    """
    取得文件路径
    """
    file_name_pach = []
    s = os.path.join(sys.path[0], r"2链接信息表 （第二税务分局）")
    list1 = os.listdir(s)
    for i in list1:
        file_name_pach.append(("".join((s,"\\",i)),i))
    return file_name_pach


# 参考：https://www.zhihu.com/question/64235925
def replaceStr(doc,replace_text):
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
            for old,new in replace_text.items():
                if ord in cell.text:
                    cell.text = cell.text.replace(old, new)       


if __name__ == "__main__":
    replace_text = {"（点击展示条款内容）":"","（点击导航）":"","点击展示":"详见"}
    file_path_list = getFilePath()
    for path,name in file_path_list:
        doc = Document(path)
        replaceStr(doc,replace_text)
        doc.save("%s" % name)

    # s = os.path.join(sys.path[0], r"2链接信息表 （第二税务分局）")
    # file_name_list = os.listdir(s)
    # for file_name in file_name_list:
    # file_name = "".join((s,"\\",file_name))
    # print(file_name)
    # doc.save("%s.docx" % file_name)