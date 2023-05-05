import prcess_plot as pplt
import matplotlib.pyplot as plt
from scipy import signal
import Pan_Tompkins as pt
from Pan_Tompkins import fs #采样频率
import numpy as np

a = 'STD'; b = 'STE'; c = 'Others'; d = 'DE'
#定义二维数组，存放12导联数据
array = [[], [], [], [], [], [], [], [], [], [], [], []]
mwin = [[], [], [], [], [], [], [], [], [], [], [], []]


SG_window = 60  #SG滤波缓存大小
SG_k = 6        #SG拟合系数

#输出R峰处理的图像
file_name, data = pplt.data_process(a, 110, SG_window, SG_k)#获取文件名和文件12导联数据
#对每个导联的数据进行处理输出
for i in range(0, len(array)):
    mwin[i] = pt.solve(data[i])
    hr = pt.heart_rate(data[i], fs, mwin[i])
    result = hr.find_r_peaks()
    result = np.array(result)
    result = result[result > 0]
    plt.subplot(6,2,i+1)
    # Plotting the R peak locations in ECG signal
    plt.plot(data[i], linewidth = 1)        
    plt.scatter(result, data[i][result], color = 'red', s = 50, marker= '*')
    plt.xlim(4000, 6000)
'''

'''
#输出原信号基本处理的图像
plt.figure(2)
pplt.plot_DEO(a, 110, 12, SG_window, SG_k)

plt.show()
# Plotting bandpassed signal
#pplt.plot_DEO(a, 33, 12, 60, 6)
'''
file_name, data = pplt.data_process(a, 110, SG_window, SG_k)
for i in range(0, len(array)):
    data[i] = pt.band_pass_filter(data[i])

for i in range(0, len(array)):
    data[i] = pt.solve(data[i])
pplt.data_DEO(file_name, data, 12)
'''