# 拆分数据集
from sklearn.model_selection import train_test_split
# 导入决策树
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score
from sklearn.datasets import make_classification

from prcess_plot import data_process

import os
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio
import pandas as pd
import joblib as model
import ST_loca as st
import prcess_plot as pplt
import ST_feature2 as fea02
import Get_file_name as Get_basic

# feature_name = ['data0', 'data1', 'data2', 'data3', 'data4', 'data5', 'data6', 'data7', 'data8', 'data9', 'data10', 'data11', 'target']
# df = []
# df_temp = []
# data_03 = []
# a = 'STD'; b = 'STE'; c = 'Others'; d = 'DE';
# index_min = 75
# index_max = 125
# for index in range(index_min, index_max):
#     print(index)
#     data_01, warn = fea02.extract_ST_feature_02(d, index)
#     if warn >= 8:
#         print('AAA')
#     else:
#         data_02 = Get_basic.Get_type_int(d, index)
#         data_01.append(data_02)
#         df_temp = pd.DataFrame([data_01], columns=[feature_name])
#         if index == min(index_min, index_max):
#             df = df_temp
#         else:
#             df = pd.concat([df, df_temp], axis=0)
# print('!!!')
# for index in range(index_min, index_max):
#     print(index)
#     data_01, warn = fea02.extract_ST_feature_02(a, index)
#     if warn >= 8:
#         print('BBB')
#     else:
#         data_02 = Get_basic.Get_type_int(a, index)
#         data_01.append(data_02)
#         df_temp = pd.DataFrame([data_01], columns=[feature_name])
#         df = pd.concat([df, df_temp], axis=0)
# print('!!!')
# for index in range(index_min, index_max):
#     print(index)
#     data_01, warn = fea02.extract_ST_feature_02(b, index)
#     if warn >= 8:
#         print('CCC')
#     else:
#         data_02 = Get_basic.Get_type_int(a, index)
#         data_01.append(data_02)
#         df_temp = pd.DataFrame([data_01], columns=[feature_name])
#         df = pd.concat([df, df_temp], axis=0)
# print('!!!')
# print(df)
# #用于删除缺失值
# df3 = df3.dropna(axis = 0, how = 'any')

df = pd.read_csv('my_data.csv')
print(df)
# df.to_csv('my_data.csv')
# 将数据集分成训练集和测试集immb
train, test = train_test_split(df, test_size=0.3)
print(train)
print("！！！！！")
print(test)
# 创建一个随机森林分类器对象并训练它
rf = RandomForestClassifier(n_estimators=150, max_depth=6, random_state=0)
# #传入train的4个特征数据及标签
rf.fit(train[['data0', 'data1', 'data2', 'data3','data4', 'data5', 'data6', 'data7','data8', 'data9', 'data10', 'data11']], train['target'])

model.dump(rf, 'mymodel.pkl')
# #自己输出查看一下，然后调节一下各种参数看看
predictions = rf.predict(test[['data0', 'data1', 'data2', 'data3','data4', 'data5', 'data6', 'data7','data8', 'data9', 'data10', 'data11']])
pro = accuracy_score(test['target'], predictions)
print(predictions, pro)

