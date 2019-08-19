import os
import xlrd

path = "C:\\Users\\Lancelot\\Desktop\\rubbish\\data_of_xlsx\\"  # ����ʵ�ֿɸ�Ϊ���·��


def create_dict():  # ���ɸ������Ӧ���ֵ�
    fileList = os.listdir(path)
    fundDict = {}
    n = 0
    for i in fileList:
        filename = fileList[n]
        numOfFund = filename[0:6]

        fundDict[numOfFund] = 0

        n += 1
    return numOfFund


def isNum(a):  # �ж��Ƿ�Ϊ������
    try:
        float(a)
    except:
        return 0
    else:
        return 1


def fundAvg(fundnum):  # ����һ�������ƽ���껯�ʣ�����Ϊ�����
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
    return 252 * sum / len(hisdata)  # �˴���252��365����


def create_dict():  # ���ɸ������Ӧ�ĳ�ʼ���ֵ�,�������ݣ�������.xlsx����ֵ��Ϊ0
    fileList = os.listdir(path)
    fundDict = {}
    n = 0
    for i in fileList:
        filename = fileList[n]
        numOfFund = filename[0:6]

        fundDict[numOfFund] = 0

        n += 1
    return fundDict


def create_weight():  # ���ɲ����ظ��������Ȩ���ֵ䣬funDictΪcreate_dict()������ֵΪ0���ֵ�
    fundDict = create_dict()
    while True:
        try:
            fund = input("�������Ĵ���(����quit�˳�)��")
            print(fund)
            if fund == "quit":
                break
            if not fund in fundDict:
                print("���������Ų��ڷ�Χ��")
                continue

            value = float(input("��������Ȩ��weight(0<=weight<=1)&&sum(weight)==1:"))
            if not (value >= 0 and value <= 1):
                print("����Ȩ�ز��ڷ�Χ��")
                continue
            if value == "quit":
                break
        except:
            print("error:�������ֵ")
            continue
        else:
            fundDict[fund] = value
    sum = 0
    for i in fundDict:
        sum += fundDict[i]
    if (abs(sum - 1) > 0.01):
        print("error:Ȩֵ֮�Ͳ�Ϊ1")
        return
    return fundDict


def create_prof():  # ����ÿ���������ʷƽ���껯�ʣ����ض�Ӧ�ֵ� {������ţ��껯��}
    fundDict = create_dict()
    for i in fundDict:
        fundDict[i] = fundAvg(i)
    return fundDict


def simulation(fund_ratio):  # ������ʷ�껯��,Ϊ������
    sum=0
    for i in fund_ratio:
        sum += fund_ratio[i]
    if (abs(sum - 1) > 0.01):
        print("error:Ȩֵ֮�Ͳ�Ϊ1")
        return
    profit = create_prof()#{����ƽ���껯��}
    temp_weight = fund_ratio
    for i in temp_weight:
        temp_weight[i] *= profit[i]
    totalProfit = 0

    for i in temp_weight:
        totalProfit += temp_weight[i]

    return {
        'expected_rate':totalProfit #Ԥ��������,��λΪ�ٷֱ�
    }

print(simulation(create_weight()))
