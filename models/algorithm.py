import numpy as np
# import matplotlib.pyplot as plt
import cvxopt
from model import *


cvxopt.solvers.options['show_progress'] = False     # 关闭求解过程打印
# np.random.seed(1)

# 随机生成n个权重，和为1，且不超过0.4
def random_weights(n):
    flag = True
    while flag:
        w = np.random.rand(n)
        w = w / w.sum()
        flag = False
        for value in w:
            if value > 0.4:
                flag = True
                break
    return w


# 计算采样点的收益和标准差, mu为1*n
def random_compute(mu, cov):
    n = mu.shape[1]
    w = np.array([random_weights(n)])

    p, sigma = compute(w, mu, cov)
    return np.array([[p], [sigma]])


#计算某组合的收益和标准差（w，mu均为1*n）
def compute(w, mu, cov):
    p = w.dot(mu.T)  # 收益
    sigma = np.sqrt(w.dot(cov).dot(w.T))  # 标准差
    return float(p), float(sigma)


# 随机采样权重，求出最小方差对应的Erp和Erp最大值
def sample(n, mu, cov):
    means, stds = np.column_stack([random_compute(mu, cov) for i in range(n)])
    idx = np.argmin(stds)
    minstd_p = means[idx]                      # 最小方差对应的Erp
    max_p = np.max(means)

    # plt.plot(stds, means, 'o')
    # plt.plot(0, minstd_p, 'ro')
    # plt.plot(0, max_p, 'ro')
    return minstd_p, max_p


# 马科维茨模型求最小风险点
def Markowitz(mu, cov, minstd_p, max_p, n_sample):
    n = mu.shape[1]                                     # 基金数量
    sample_list = np.linspace(minstd_p, max_p, n_sample)       # 采样Erp点

    C = 2*cvxopt.matrix(cov)                   # 优化问题 min (1/2)x.T*C*x

    # 不等式约束Gx<h，权重全部大于等于0小于等于0.4
    G = cvxopt.matrix(np.row_stack((np.eye(n), -np.eye(n))))
    h = cvxopt.matrix(np.row_stack((0.4*np.ones((n, 1)), np.zeros((n, 1)))))

    # 等式约束Ax=b，权重之和为1；总收益为mu
    A = cvxopt.matrix(np.row_stack((np.ones((1,n)), mu)))
    res = [cvxopt.solvers.qp(C, cvxopt.matrix(np.zeros((n,1))), G, h, A, cvxopt.matrix(np.array([[1],[u]])))['x'] for u in sample_list]
    npres = [np.array(mat).T for mat in res]
    # print(np.squeeze(np.array(npres)))
    return np.squeeze(np.array(npres))       # 返回为n*w，n为投资组合数，w为权重


Fund.objects.all().delete()
Combination.objects.all().delete()                      # 先清空数据库中原先的数据
return_vec = np.load('data.npy')				        # 读取数据

mu = np.array([np.mean(return_vec, axis=1)])*252        # 年化收益率/协方差
cov = np.cov(return_vec)*252

mu_list = list(mu[0])
nameno_list = list(np.load('name.npy'))

# 向数据库中保存基金名、代码、预期收益率，以npy形式保存协方差矩阵
name_list = []
no_list = []
for i in nameno_list:
    iop = i.split('_')
    name_list.append(iop[0])
    no_list.append(iop[1])

for i in range(len(mu_list)):
    fund = Fund()
    fund.fundname = name_list[i]
    fund.fundno = no_list[i]
    fund.profit = mu_list[i]
    fund.save()
np.save('covar.npy',cov)

minstd_p, max_p = sample(50000, mu, cov)        # 取最小方差对应Erp和最大Erp
eff_fro = Markowitz(mu, cov, minstd_p, max_p, 50)   # 计算有效前沿(50个点)
means = [float(w.dot(mu.T)) for w in eff_fro]           # 有效前沿的组合收益率
stds = [np.sqrt(w.dot(cov).dot(w.T)) for w in eff_fro]  # 有效前沿的组合方差
# plt.plot(stds, means, 'y-o')

risk = []			# 风险系数，范围[3.0, 6.0], 间距0.1
risk_d = 3
risk_u = 6
for i in range(31):
    risk.append(risk_d + i * (risk_u - risk_d)/30)

V_index	= []		# 不同风险系数下选择的组合下标
V_means = []
V_stds = []
for r in risk:
    V = []
    for i in range(len(eff_fro)):
        V.append(means[i] - 1.25 * r * (stds[i] ** 2))  # 效用函数
    max_index = V.index(max(V))     # 遍历有效前沿，找出当前风险系数使效用函数最大的组合
    res_list = list(eff_fro[max_index])

    # 将组合的权重向量保留3位小数，并保证加和为1
    mylist = []
    sum = 0
    for i in res_list:
        i*=1000
        i=round(i)
        sum += i
        mylist.append(i)

    # 截断后产生的误差加在权重向量第二大的元素上
    rest = 1000 - sum
    checklist = mylist.copy()
    checklist.remove(max(checklist))
    for i in range(len(mylist)):
        if mylist[i] == max(checklist):
            mylist[i] += rest
            break

    # 以字典形式保存进数据库
    mapping = {}
    for i in range(len(mylist)):
        mapping[name_list[i]] = mylist[i] / 1000
    # print(mapping)
    combination = Combination()
    combination.risk_factor = r
    combination.expected_rate = means[max_index]
    combination.std = stds[max_index]
    combination.recommendation = str(mapping)
    combination.save()

# plt.plot(V_stds, V_means, 'r-o')
# plt.show()