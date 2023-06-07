#拆分数据集
from sklearn.model_selection import train_test_split
#导入决策树
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score
from sklearn.datasets import make_classification

from prcess_plot import data_process

import os
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio
import pandas as pd
import ST_loca as ST
import prcess_plot as pplt
import ST_feature2 as fea02
import Get_file_name as Get_basic
file = "..\\data_set\\"+"292.mat"
# data_mat = sio.loadmat(file)#读取mat文件中的数据
df3 = []
a = 'STD'; b = 'STE'; c = 'Others'; d = 'DE'
# for index in range(1,2):
#     print(index)
#     print("!!!")\
temp_list=[]
for index in range(12,13):
    for i in range(12):
        Q_line, ST_line = ST.basic_line_st(d, index, i)
        data_01 = fea02.extract_ST_feature_02(b,index,ST_line,i)
        # df1 = pd.DataFrame(num, columns=['num'])
        data = 'data' + str(i)
        df2 = pd.DataFrame(data_01, columns = [data])
        if(i == 0 and index == 12):
            df3 = df2
        df3 = pd.concat([df3, df2], axis = 1)
        print(i)
print(df3)
data_01 = [1,0,1,1 ,1,0,1,0 ,1,1,0,0 ,1,0,1]
# df2 = pd.DataFrame(data_01, columns = ['Target'])
# df3 = pd.concat([df3, df2], axis = 1)
df3['target'] = data_01
df3 = df3.dropna(axis = 0, how = 'any')
print(df3)
# # 将数据集分成训练集和测试集
train, test = train_test_split(df3, test_size=0.5)
print(train)
print(train.shape)
print("！！！！！")
print(test)
print(test.shape)
#创建一个随机森林分类器对象并训练它
rf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
# #传入train的4个特征数据及标签
rf.fit(train[['data0', 'data1', 'data2', 'data3','data4', 'data5', 'data6', 'data7','data8', 'data9', 'data10', 'data11']], train['target'])


# #自己输出查看一下，然后调节一下各种参数看看
predictions = rf.predict(train[['data0', 'data1', 'data2', 'data3','data4', 'data5', 'data6', 'data7','data8', 'data9', 'data10', 'data11']])
pro = accuracy_score(test['target'], predictions)
print(predictions,pro)

