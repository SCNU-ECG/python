import time
import numpy as np
import scipy.io as sio
import pandas as pd
import joblib as model
import ST_loca as st
import prcess_plot as pplt
import ST_feature2 as fea02
import Get_file_name as Get_basic
import feature_learn as feature
File_type = ['STD','STE']
feature_name = ['data0', 'data1', 'data2', 'data3', 'data4', 'data5', 'data6', 'data7', 'data8', 'data9', 'data10', 'data11', 'target']
result01 = []
index_min = 0
index_max = 49
start = time.process_time()
print('芝士雪豹')
multi_work = model.Parallel(n_jobs = -1,backend='loky')
result01 = multi_work(model.delayed(feature.get_feature)(type, index_max, index_min) for type in File_type)
output = np.concatenate(result01)
output = np.reshape(output,(-1,13))
df = pd.DataFrame(output, columns=[feature_name])
end = time.process_time()
print('程序运行时间:%s秒' %((end - start)*1000))
print('芝士顶针')
df.to_csv('my_data_temp.csv')