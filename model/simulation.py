import os
import xlrd

path = "C:\\Users\\Lancelot\\Desktop\\rubbish\\data_of_xlsx\\"  # 具体实现可改为相对路径


def create_dict():  # 生成各基金对应的字典
    fileList = os.listdir(path)
    fundDict = {}
    n = 0
    for i in fileList:
        filename = fileList[n]
        numOfFund = filename[0:6]

        fundDict[numOfFund] = 0

        n += 1
    return numOfFund


def isNum(a):  # 判断是否为浮点数
    try:
        float(a)
    except:
        return 0
    else:
        return 1


def fundAvg(fundnum):  # 返回一个基金的平均年化率，输入为基金号
    file = path + fundnum + ".xlsx"
    workbook = xlrd.open_workbook(file)
    worksheet = workbook.sheet_by_index(0)
    nrows = worksheet.nrows
    # ncols = table.ncols

    hisdata = []

    for i in range(1, nrows):
        cell_value = worksheet.cell_value(i, 1)
        if isNum(cell_value):
            hisdata.append(float(cell_value))
    sum = 0
    for i in hisdata:
        sum += i
    return 252 * sum / len(hisdata)  # 此处乘252或365待定


def create_dict():  # 生成各基金对应的初始化字典,基金数据：“代号.xlsx”，值均为0
    fileList = os.listdir(path)
    fundDict = {}
    n = 0
    for i in fileList:
        filename = fileList[n]
        numOfFund = filename[0:6]

        fundDict[numOfFund] = 0

        n += 1
    return fundDict


def create_weight():  # 生成并返回各个基金的权重字典，funDict为create_dict()创建的值为0的字典
    fundDict = create_dict()
    while True:
        try:
            fund = input("输入基金的代号(输入quit退出)：")
            print(fund)
            if fund == "quit":
                break
            if not fund in fundDict:
                print("输入基金代号不在范围内")
                continue

            value = float(input("输入基金的权重weight(0<=weight<=1)&&sum(weight)==1:"))
            if not (value >= 0 and value <= 1):
                print("输入权重不在范围内")
                continue
            if value == "quit":
                break
        except:
            print("error:输入非数值")
            continue
        else:
            fundDict[fund] = value
    sum = 0
    for i in fundDict:
        sum += fundDict[i]
    if (abs(sum - 1) > 0.01):
        print("error:权值之和不为1")
        return
    return fundDict


def create_prof():  # 创建每个基金的历史平均年化率，返回对应字典 {基金代号：年化率}
    fundDict = create_dict()
    for i in fundDict:
        fundDict[i] = fundAvg(i)
    return fundDict


def simulation(fund_ratio):  # 计算历史年化率,为主函数
    sum=0
    for i in fund_ratio:
        sum += fund_ratio[i]
    if (abs(sum - 1) > 0.01):
        print("error:权值之和不为1")
        return
    profit = create_prof()#{基金：平均年化率}
    temp_weight = fund_ratio
    for i in temp_weight:
        temp_weight[i] *= profit[i]
    totalProfit = 0

    for i in temp_weight:
        totalProfit += temp_weight[i]

    return {
        'expected_rate':totalProfit #预期收益率,单位为百分比
    }

print(simulation(create_weight()))
