#Models
模型实现。

#Original Data
包含了原始的基金数据，包括xlsx和xls两种格式的文件。  

- xls: 数据来源 RESSET数据库（使用校园网访问）[链接](http://library.sysu.edu.cn/article/1543)
- xlsx: 数据来源不详

命名格式：基金名_基金编号(6位)

#dataclean
处理原始数据，生成data.npy和name.npy文件。前者为二维numpy数组，每行为一支基金的单日增长率序列；后者记录对应的基金名。

#algorithm & model
运行马科维茨模型，并根据效用函数计算出每个风险系数所选中的最佳组合权重、年化期望收益率与年化标准差，并将结果保存入数据库。

- 风险系数区间为[3.0, 6.0]，步长0.1，共31个
- 由于采用了django的ORM来进行数据库操作，因此需要加入django的运行环境方可运行。
- **只有当基金数据有更新时才需要重新运行模型**

#interface
提供给后端调用的接口。

- 根据用户问卷计算风险系数并查询数据库得到组合：

```python
def recommendate(questionnaire):
    """
    输入问卷答案返回推荐的基金比例，风险系数，期望收益率
    questionnaire: list 
    [ # 问卷
        'A',
        'B',
        'C',
        'D'
    ]
    returns: dict
    {  
       'recommendation':{
            '中石油': 0.15
            '中石化': 0.6
        } # 基金名: 比例
        'expected_rate': 0.2 # 预期收益率
        'risk_factor': 1.5 # 风险系数
		'std': 0.1			# 组合方差
    }
    """
```

- 根据用户输入的权重计算预期收益率：

```python
def simulation(fund_ratio):
    """
    输入基金名和比例，返回预期收益率
    fund_ratio: dict
    {
        '中石油': 0.15 # 基金名: 比例
        '中石化': 0.6 # 基金名: 比例
    } 
    return: dict
    {  
      'expected_rate': 0.2 # 预期收益率
    }
    """
```