import os
import xlrd

path = "C:\\Users\\Lancelot\\Desktop\\rubbish\\data_of_xlsx\\"  # 具体实现可改为相对路径

def trans_name():  # 将基金名字统一为代码
    fileList = os.listdir(path)
    n = 0
    for i in fileList:
        oldname = path + fileList[n]
        tempname = oldname
        count = 0
        for letter in oldname:
            count += 1
            if letter == '(':
                tempname = oldname[count:count + 6]
                break

        newname = path + tempname + ".xls"
        os.rename(oldname, newname)
        print(oldname, "----->", newname)

        n += 1
trans_name()