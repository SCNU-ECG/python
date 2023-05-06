import prcess_plot as pplt
import matplotlib.pyplot as plt
from scipy import signal
import Pan_Tompkins as pt
import numpy as np

a = 'STD'; b = 'STE'; c = 'Others'; d = 'DE'
#定义二维数组，存放12导联数据
array = [[], [], [], [], [], [], [], [], [], [], [], []]
index = 150

#输出R峰处理的图像
pplt.plot_R_peak(a, index, 12)


'''

'''
#输出原信号基本处理的图像
plt.figure(2)
pplt.plot_DEO(a, index, 12)

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