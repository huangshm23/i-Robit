import os
import xlrd

path = "C:\\Users\\Lancelot\\Desktop\\rubbish\\data_of_xlsx\\"  # ����ʵ�ֿɸ�Ϊ���·��

def trans_name():  # ����������ͳһΪ����
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