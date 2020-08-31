import os
# python -m pip install pypiwin32
from win32com import client

'''
将对应文件夹下的doc文件转为docx文件
'''
def doc_to_docx(path):
    if os.path.splitext(path)[1] == ".doc":
        word = client.Dispatch('Word.Application')
        doc = word.Documents.Open(path)  # 目标路径下的文件
        doc.SaveAs(os.path.splitext(path)[0]+".docx", 16)  # 转化后路径下的文件
        doc.Close()
        word.Quit()
        print(os.path.splitext(path)[0]+".docx：转换完成")

def find_file(path, ext, file_list=[]):
    dir = os.listdir(path)
    for i in dir:
        i = os.path.join(path, i)
        if os.path.isdir(i):
            find_file(i, ext, file_list)
        else:
            if ext == os.path.splitext(i)[1]:
                file_list.append(i)
    return file_list

def main():
    #批量转换文件夹
    dir_path = "D:\\GitHub program\\py_test\\未完成\\doc"
    ext = ".doc"
    file_list = find_file(dir_path, ext)
    for file in file_list:
        doc_to_docx(file) 
    print("任务全部完成！")
 
if __name__ == "__main__":
    main()