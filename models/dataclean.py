import pandas as pd
import os
import numpy as np

def xls(path, idx):
    df = pd.read_excel(path)
    data = df[['信息发布日期_InfoPubDt', '单位累计净值_AccUntNV']]
    #data['信息发布日期_InfoPubDt'] = pd.to_datetime(data['信息发布日期_InfoPubDt'])
    data = data.set_index('信息发布日期_InfoPubDt')
    data = (data.pct_change()[1:]).reset_index()
    data = data.drop_duplicates(['信息发布日期_InfoPubDt'], keep='first')
    data.columns = (['信息发布日期_InfoPubDt', str(idx)])
    #print(data)
    #s = pd.Series(data['单位累计净值_AccUntNV'], index = data.index)
    #print(s)
    return data


def xlsx(path, idx):
    df = pd.read_excel(path, header=None, names=['date', 'jingzhi'])
    df['date'] = pd.to_datetime(df['date'], format='%Y年%m月%d日')
    df = df.dropna(axis=0, how='any')
    df = df.set_index('date')
    df = (df.pct_change()[1:]).reset_index()
    df.columns = (['信息发布日期_InfoPubDt', str(idx)])
    return df


flag = True
idx = 0
name_list = []
for root, dirs, files in os.walk('./original data'):
    for dr in dirs:
        for rc, dc, fc in os.walk('./original data/'+dr):
            for name in fc:
                (filename, _) = os.path.splitext(name)
                name_list.append(filename)
                if name.endswith('.xls'):
                    data = xls('./original data/'+dr+'/'+name, idx)
                else:
                    data = xlsx('./original data/'+dr+'/'+name, idx)
                # print('{} {}'.format(idx, name))
                idx += 1
                if flag:
                    tol = data
                    flag = False
                else:
                    tol = pd.merge(tol, data)
tol = tol.set_index('信息发布日期_InfoPubDt')
# print(tol)
data = np.array(tol, dtype=np.double).T
np.save('data.npy', data)
np.save('name.npy', np.array(name_list))