# Model
实现模型

# 功能
根据输入和数据，计算并返回结果

simulation:模拟功能
```python
  post：
      fund_ratio: dict
    {
        '000080': 0.15 # 基金编号: 比例
        '000307': 0.6 # 基金编号: 比例
        ……
    }   *权重为0的基金也要包含在字典中
   
       return: dict
    {  
      'expected_rate': 0.2 # 预期收益率
    }
  ```
 
 Filename2Num.py:将给的原始数据的名字改为基金的代号

xls2xlsx.txt:里面为VBA代码，在excel运行。执行将当前目录下的xls另存为xlsx的批量操作。用来解决因格式问题而无法调用xlrd进行读操作的问题

data_of_xlsx：数据


## checkpoint
- 8/15 建立文件夹
- 8/20 初始的模拟功能
