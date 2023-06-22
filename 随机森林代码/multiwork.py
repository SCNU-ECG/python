import time
import numpy as np
import pandas as pd
import joblib as model
import feature_learn as feature
File_type = ['STD','STE','DE']
File_data = [0,865,1730,2585]
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
                'da11_area_max', 'da11_area_min', 'da11_slope_max', 'da11_slope_min', 'da11_peak_max', 'da11_peak_min',
                'target']
index_min = 0
index_max = 180
start = time.time()
print('芝士雪豹')
multi_work = model.Parallel(n_jobs=-1, backend='loky')
result01 = multi_work(model.delayed(feature.get_feature)(type, index_max, index_min) for type in File_type)
#result02 = multi_work(model.delayed(feature.get_feature)('Others', (index_min + 865), index_min) for index_min in File_data)
output = np.concatenate(result01)
#output = np.concatenate(result02)
output = np.reshape(output, (-1, 73))
df = pd.DataFrame(output, columns=[feature_name])
end = time.time()
print('程序运行时间:%s秒' %(end - start))
print('芝士顶针')
df.to_csv('my_data_no_other.csv')