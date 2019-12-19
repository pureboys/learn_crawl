import pandas as pd
from pandas import Series, DataFrame
import numpy as np

# series = Series(data=[1, 2, 3])
# print(series)
# series2 = Series(data=[1, 2, 3], index=['a', 'b', 'c'])  # 显示索引
# print(series2)

# s = Series(data=np.random.randint(0, 100, size=(4,)), index=['a', 'b', 'c', 'd'])
# print(s[0:3])
# print(s.values)
# print(s.index)

# s = Series(data=[1, 2, 2, 2, 3, 4, 5, 6, 7, 8])
# print(s.unique())

# s1 = Series(data=[1, 2, 3], index=['a', 'b', 'c'])
# s2 = Series(data=[1, 2, 3], index=['a', 'b', 'd'])
# s = s1 + s2
# print(s.isnull())
# print(s.notnull())
#
# print(s[[1, 2]])
# print(s[[True, False, False, True]])
# print(s[s.notnull()])

#
# df = DataFrame(data=np.random.randint(0, 100, size=(3, 4)), index=['a', 'b', 'c'], columns=['A', 'B', 'C', 'D'])
# # 切出单个/多个元素
# print(df.loc['a', 'D'])
# print(df.loc[['a', 'b'], 'D'])
#
# # 切出两列
# print(df[['A', 'B']])
# print(df.loc[:, 'A':'B'])
#
# # 切出前两行
# print(df.loc[['a', 'b']])
# print(df['a': 'b'])

dic = {
    '张三': [11, 22, 33, 44],
    '李四': [56, 66, 77, 88]
}

df_score = DataFrame(data=dic, index=['语文', '数学', '英语', '理综'])

qizhong = df_score
qimo = df_score

print((qizhong + qimo) / 2)

qizhong.loc['数学', '张三'] = 0
print(qizhong)

qizhong['李四'] += 100
print(qizhong)

qizhong += 10
print(qizhong)


