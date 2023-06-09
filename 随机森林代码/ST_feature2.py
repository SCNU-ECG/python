import prcess_plot as pplt
import numpy as np
import ST_loca as loca
from prcess_plot import data_process

R_ST_span = 70          #距离R峰后N个采样点作为S段开始点
ST_span = 40            #N个采样点加权作为ST段基线
step = 5                #步长

def extract_ST_feature_02(File_type, File_num):
    # 整个导联数据读取以及预处理
    name, array = data_process(File_type, File_num)
    array = pplt.data_reverse(array)
    slopes = []
    warn = 0
    # 每个导联的ST基线获取
    for Channel in range(0, 12):
        Q_line, ST_line, warn = loca.basic_line_st(File_type, File_num, Channel)
        pplt.daolian = int(Channel)
        # 获取每个导联的所有R锋
        data, local = pplt.get_R_loca(File_type, File_num)
        # 初始化待存储变量
        slope_sum = 0
        for i in range(0, int(len(local))):
            r_peak = local[i]
            # 确定ST段的起始位置和结束位置，目前是固定长度，未来改成动态测量
            ST_start = int(r_peak + R_ST_span)
            ST_end   = int(ST_start + ST_span)
            # 计算ST段面积
            st_segment = data[ST_start:ST_end:5]
            slope = np.sum(st_segment)
            slope = slope - ST_line*(int(len(data)))
            slope_sum += slope
        # 把每个导联的计算结果加入到数组中
        slopes.append(slope_sum)
    return slopes, warn
