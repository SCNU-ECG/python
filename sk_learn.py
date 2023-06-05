#拆分数据集
from sklearn.model_selection import train_test_split
#导入决策树
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score
from sklearn.datasets import make_classification
import os
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio
import pandas as pd

# file = "..\\data_set\\"+"13.mat"
# data_mat = sio.loadmat(file)#读取mat文件中的数据




# # 创建一个样本数据集
# x, y = make_classification(n_samples=1000, n_features=4,
#                             n_informative=2, n_redundant=0,
#                             random_state=5, shuffle=False)

# # 将数据转换为pandas的数据框格式,自己注意输出一下查看格式要怎么样，到时候直到怎么放置数据
# df = pd.DataFrame(x, columns=['Feature 1', 'Feature 2', 'Feature 3', 'Feature 4'])
# df['Target'] = y
# print(df)
# # 将数据集分成训练集和测试集
# train, test = train_test_split(df, test_size=0.2)

# #创建一个随机森林分类器对象并训练它
# rf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
# #传入train的4个特征数据及标签
# rf.fit(train[['Feature 1', 'Feature 2', 'Feature 3', 'Feature 4']], train['Target'])


# #自己输出查看一下，然后调节一下各种参数看看
# predictions = rf.predict(test[['Feature 1', 'Feature 2', 'Feature 3', 'Feature 4']])
# pro = accuracy_score(test['Target'], predictions)
# print(predictions, pro)

