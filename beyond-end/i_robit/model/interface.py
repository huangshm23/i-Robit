from i_robot.models import Combination,Fund
from django.forms.models import model_to_dict


# 计算用户风险系数
def calculate_risk(questionnaire):
      score = [{'A':4, 'B':3, 'C':2, 'D':1},
               {'A':1, 'B':2, 'C':3, 'D':4},
               {'A':1, 'B':2, 'C':3, 'D':4},
               {'A':1, 'B':2, 'C':3},
               {'A':1, 'B':2, 'C':3},
               {'A':1, 'B':2, 'C':3, 'D':4},
               {'A':1, 'B':2, 'C':3, 'D':4},
               {'A':1, 'B':2, 'C':3, 'D':4},
               {'A':1, 'B':3},
               {'A':1, 'B':3},
               {'A':1, 'B':2, 'C':3, 'D':4},
               {'A':1, 'B':2, 'C':3},
               {'A':1, 'B':2, 'C':3, 'D':4},]
      tol = 0
      for i in range(len(questionnaire)):
          tol += score[i][questionnaire[i]]
      A = (47-tol)/(47-13) * (6-3) + 3
      return A


# 根据问卷结果推荐基金组合
def recommendate(questionnaire):
    A = calculate_risk(questionnaire)
    A = round(A, 1)

    comb = Combination.objects.filter(risk_factor=A).first()
    return model_to_dict(comb)


# 根据所给权重计算基金收益
def simulation(fund_ratio):
    sum_val=0
    for name, w in fund_ratio.items():
        sum_val += w
    if (abs(sum_val - 1) > 0.01):
        #print("error:权值之和不为1")
        return None
    profit = []
    weights = []
    for name, w in fund_ratio.items():
        fund = Fund.objects.filter(fundname=name).first()
        p = model_to_dict(fund)['profit'] # 获取对应基金名的收益率
        profit.append(p)
        weights.append(w)
    totalProfit = sum([a*b for a,b in zip(profit, weights)])
    return {
        'expected_rate':totalProfit #预期收益率,单位为百分比
    }