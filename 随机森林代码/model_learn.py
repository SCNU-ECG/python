# 拆分数据集
from sklearn.model_selection import train_test_split
# 导入决策树
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd
import joblib as model
#feature_name = ['STD','STE','DE']
feature_name = ['Others','STD','STE','DE']
#df = pd.read_csv('my_data_no_other.csv')
df = pd.read_csv('my_data_temp.csv')
# print(df)
# df.to_csv('my_data.csv')
# 将数据集分成训练集和测试集immb
train, test = train_test_split(df, test_size=0.01)
# print(train)
# print("！！！！！")
# print(test)
# test.to_csv('my_data_temp_04.csv')
# 创建一个随机森林分类器对象并训练它
rf = RandomForestClassifier(n_estimators=50, max_depth=6, max_features=0.3, min_samples_split= 8, random_state=0,class_weight={0: 1, 1: 12 ,2: 12, 3: 12})
# #传入train的特征数据及标签
rf.fit(train[['da0_area_max', 'da0_area_min', 'da0_slope_max', 'da0_slope_min', 'da0_peak_max', 'da0_peak_min',
              'da1_area_max', 'da1_area_min', 'da1_slope_max', 'da1_slope_min', 'da1_peak_max', 'da1_peak_min',
              'da2_area_max', 'da2_area_min', 'da2_slope_max', 'da2_slope_min', 'da2_peak_max', 'da2_peak_min',
              'da3_area_max', 'da3_area_min', 'da3_slope_max', 'da3_slope_min', 'da3_peak_max', 'da3_peak_min',
              'da4_area_max', 'da4_area_min', 'da4_slope_max', 'da4_slope_min', 'da4_peak_max', 'da4_peak_min',
              'da5_area_max', 'da5_area_min', 'da5_slope_max', 'da5_slope_min', 'da5_peak_max', 'da5_peak_min',
              'da6_area_max', 'da6_area_min', 'da6_slope_max', 'da6_slope_min', 'da6_peak_max', 'da6_peak_min',
              'da7_area_max', 'da7_area_min', 'da7_slope_max', 'da7_slope_min', 'da7_peak_max', 'da7_peak_min',
              'da8_area_max', 'da8_area_min', 'da8_slope_max', 'da8_slope_min', 'da8_peak_max', 'da8_peak_min',
              'da9_area_max', 'da9_area_min', 'da9_slope_max', 'da9_slope_min', 'da9_peak_max', 'da9_peak_min',
              'da10_area_max', 'da10_area_min', 'da10_slope_max', 'da10_slope_min', 'da10_peak_max', 'da10_peak_min',
              'da11_area_max', 'da11_area_min', 'da11_slope_max', 'da11_slope_min',
              'da11_peak_max', 'da11_peak_min']], train['target'])

model.dump(rf, 'mymodel.pkl')
# #自己输出查看一下，然后调节一下各种参数看看
predictions = rf.predict(test[['da0_area_max', 'da0_area_min', 'da0_slope_max', 'da0_slope_min', 'da0_peak_max', 'da0_peak_min',
                               'da1_area_max', 'da1_area_min', 'da1_slope_max', 'da1_slope_min', 'da1_peak_max', 'da1_peak_min',
                               'da2_area_max', 'da2_area_min', 'da2_slope_max', 'da2_slope_min', 'da2_peak_max', 'da2_peak_min',
                               'da3_area_max', 'da3_area_min', 'da3_slope_max', 'da3_slope_min', 'da3_peak_max', 'da3_peak_min',
                               'da4_area_max', 'da4_area_min', 'da4_slope_max', 'da4_slope_min', 'da4_peak_max', 'da4_peak_min',
                               'da5_area_max', 'da5_area_min', 'da5_slope_max', 'da5_slope_min', 'da5_peak_max', 'da5_peak_min',
                               'da6_area_max', 'da6_area_min', 'da6_slope_max', 'da6_slope_min', 'da6_peak_max', 'da6_peak_min',
                               'da7_area_max', 'da7_area_min', 'da7_slope_max', 'da7_slope_min', 'da7_peak_max', 'da7_peak_min',
                               'da8_area_max', 'da8_area_min', 'da8_slope_max', 'da8_slope_min', 'da8_peak_max', 'da8_peak_min',
                               'da9_area_max', 'da9_area_min', 'da9_slope_max', 'da9_slope_min', 'da9_peak_max', 'da9_peak_min',
                               'da10_area_max', 'da10_area_min', 'da10_slope_max', 'da10_slope_min', 'da10_peak_max', 'da10_peak_min',
                               'da11_area_max', 'da11_area_min', 'da11_slope_max', 'da11_slope_min', 'da11_peak_max', 'da11_peak_min']])
pro = accuracy_score(test['target'], predictions)
proba = rf.predict_proba(test[['da0_area_max', 'da0_area_min', 'da0_slope_max', 'da0_slope_min', 'da0_peak_max', 'da0_peak_min',
                               'da1_area_max', 'da1_area_min', 'da1_slope_max', 'da1_slope_min', 'da1_peak_max', 'da1_peak_min',
                               'da2_area_max', 'da2_area_min', 'da2_slope_max', 'da2_slope_min', 'da2_peak_max', 'da2_peak_min',
                               'da3_area_max', 'da3_area_min', 'da3_slope_max', 'da3_slope_min', 'da3_peak_max', 'da3_peak_min',
                               'da4_area_max', 'da4_area_min', 'da4_slope_max', 'da4_slope_min', 'da4_peak_max', 'da4_peak_min',
                               'da5_area_max', 'da5_area_min', 'da5_slope_max', 'da5_slope_min', 'da5_peak_max', 'da5_peak_min',
                               'da6_area_max', 'da6_area_min', 'da6_slope_max', 'da6_slope_min', 'da6_peak_max', 'da6_peak_min',
                               'da7_area_max', 'da7_area_min', 'da7_slope_max', 'da7_slope_min', 'da7_peak_max', 'da7_peak_min',
                               'da8_area_max', 'da8_area_min', 'da8_slope_max', 'da8_slope_min', 'da8_peak_max', 'da8_peak_min',
                               'da9_area_max', 'da9_area_min', 'da9_slope_max', 'da9_slope_min', 'da9_peak_max', 'da9_peak_min',
                               'da10_area_max', 'da10_area_min', 'da10_slope_max', 'da10_slope_min', 'da10_peak_max', 'da10_peak_min',
                               'da11_area_max', 'da11_area_min', 'da11_slope_max', 'da11_slope_min', 'da11_peak_max', 'da11_peak_min']])
# 输出各个标签的概率
print(proba)
print(predictions, pro)
proba = pd.DataFrame(proba, columns=[feature_name])
test_data = np.reshape(test['target'],(-1,1))
proba['predict_target'] = predictions
proba['Currect_target'] = test_data
proba.to_csv('my_data_predict_proba.csv')