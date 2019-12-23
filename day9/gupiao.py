import tushare as ts
import pandas as pd
from pandas import Series, DataFrame
import numpy as np

data = ts.get_k_data(code='300785', start='2000-01-01')
data.to_csv('./zdm.csv')

# 将csv中的date作为数据的行索引，将字符串形式的时间转换为时间类型
csv = pd.read_csv('./zdm.csv', index_col='date', parse_dates=['date'])
# 删除csv的某一列
csv.drop(labels='Unnamed: 0', axis=1, inplace=True)

# 输出该股票所有收盘比开盘上涨3%以上的日期
# (收盘-开盘)/开盘 > 0.03

da = (csv['close'] - csv['open']) / csv['open'] > 0.03
# 一旦遇到了一组布尔值，直接将布尔值作为源数据的行索引
result = csv.loc[da]
# print(result.index)

# 输出该股票所有开盘比收盘跌幅超过2%的日期
#  (开盘-前日收盘)/前日收盘 < -0.02

bool_list = (csv['open'] - csv['close'].shift(1)) / csv['close'].shift(1) < 0.02
date = csv.loc[bool_list]
# print(date.index)

# 2019-08-01 - 今天
new_csv = csv['2019-08-01': '2019-12-20']

# 将买股票对应的行数据找出
df_monthly = new_csv.resample('M').first()
df_year = new_csv.resample('A').last()

# 买入股票一共花了多少钱
cost_money = df_monthly['open'].sum() * 100
recv_money = df_year['open'].sum() * 500

print(recv_money - cost_money)
