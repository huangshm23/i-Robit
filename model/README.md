# Model
实现模型

# 功能
根据输入和数据，计算并返回结果

模拟功能：
```python
  post：
      fund_ratio: dict
    {
        '000080': 0.15 # 基金编号: 比例
        '000307': 0.6 # 基金编号: 比例
        ……
    }   *权重为0的基金也要包含在字典中
    return：
       return: dict
    {  
      'expected_rate': 0.2 # 预期收益率
    }
  ```
  

## checkpoint
- 8/15 建立文件夹
- 8/20 初始的模拟功能
