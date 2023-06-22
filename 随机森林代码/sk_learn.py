# 拆分数据集
import joblib
from sklearn.model_selection import train_test_split
# 导入决策树
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
import pandas as pd
import joblib as model
import ST_feature2 as fea02
import Get_file_name as Get_basic

File_type = ['STD','STE','DE']
feature_name = ['da0_area_max', 'da0_area_min', 'da0_slope_max', 'da0_slope_min', 'da0_peak_max', 'da0_peak_min',
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
                'da11_area_max', 'da11_area_min', 'da11_slope_max', 'da11_slope_min', 'da11_peak_max', 'da11_peak_min']
df = []
df_temp = []
data_03 = []
a = 'STD'; b = 'STE'; c = 'Others'; d = 'DE';

df = pd.read_csv('my_data_temp.csv')
print(df)
# df.to_csv('my_data.csv')
# 将数据集分成训练集和测试集
train, test = train_test_split(df, test_size=0.3)
print(train)
print("！！！！！")
print(test)
# 创建一个随机森林分类器对象并训练它
rf = RandomForestClassifier(n_estimators=150, max_depth=8, random_state=0)
param_grid = {
  'n_estimators': [150],
  'max_features': [0.2],
  'max_depth': [4, 6, 8, 10],
  'min_samples_split': [2, 4, 6, 8, 12, 14]
 }
# 传入train的4个特征数据及标签
# rf.fit(train[['da0_area_max', 'da0_area_min', 'da1_area_max', 'da1_area_min', 'da2_area_max', 'da2_area_min',
#               'da3_area_max', 'da3_area_min', 'da4_area_max', 'da4_area_min', 'da5_area_max', 'da5_area_min',
#               'da6_area_max', 'da6_area_min', 'da7_area_max', 'da7_area_min', 'da8_area_max', 'da8_area_min',
#               'da9_area_max', 'da9_area_min', 'da10_area_max', 'da10_area_min', 'da11_area_max', 'da11_area_min']],
#        train['target'])

# 使用网格搜索
grid_search = GridSearchCV(rf, param_grid=param_grid, cv=5, n_jobs=-1)

# 拟合训练数据
grid_search.fit(train[['da0_area_max', 'da0_area_min', 'da0_slope_max', 'da0_slope_min', 'da0_peak_max', 'da0_peak_min',
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
                       'da11_peak_max', 'da11_peak_min']],
                       train['target'])



# 输出最佳参数组合和得分
print("Best parameters: ", grid_search.best_params_)
print("Best score: ", grid_search.best_score_)

# model.dump(rf, 'mymodel.pkl')
# rf = joblib.load('mymodel.pkl')
# # #自己输出查看一下，然后调节一下各种参数看看
# predictions = rf.predict(train[['da0_area_max', 'da0_area_min', 'da0_slope_max', 'da0_slope_min', 'da0_peak_max', 'da0_peak_min',
#                                 'da1_area_max', 'da1_area_min', 'da1_slope_max', 'da1_slope_min', 'da1_peak_max', 'da1_peak_min',
#                                 'da2_area_max', 'da2_area_min', 'da2_slope_max', 'da2_slope_min', 'da2_peak_max', 'da2_peak_min',
#                                 'da3_area_max', 'da3_area_min', 'da3_slope_max', 'da3_slope_min', 'da3_peak_max', 'da3_peak_min',
#                                 'da4_area_max', 'da4_area_min', 'da4_slope_max', 'da4_slope_min', 'da4_peak_max', 'da4_peak_min',
#                                 'da5_area_max', 'da5_area_min', 'da5_slope_max', 'da5_slope_min', 'da5_peak_max', 'da5_peak_min',
#                                 'da6_area_max', 'da6_area_min', 'da6_slope_max', 'da6_slope_min', 'da6_peak_max', 'da6_peak_min',
#                                 'da7_area_max', 'da7_area_min', 'da7_slope_max', 'da7_slope_min', 'da7_peak_max', 'da7_peak_min',
#                                 'da8_area_max', 'da8_area_min', 'da8_slope_max', 'da8_slope_min', 'da8_peak_max', 'da8_peak_min',
#                                 'da9_area_max', 'da9_area_min', 'da9_slope_max', 'da9_slope_min', 'da9_peak_max', 'da9_peak_min',
#                                 'da10_area_max', 'da10_area_min', 'da10_slope_max', 'da10_slope_min', 'da10_peak_max', 'da10_peak_min',
#                                 'da11_area_max', 'da11_area_min', 'da11_slope_max', 'da11_slope_min', 'da11_peak_max', 'da11_peak_min']])
# pro = accuracy_score(train['target'], predictions)
# print(predictions, pro)

