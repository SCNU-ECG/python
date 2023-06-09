import prcess_plot as pplt
import numpy as np
from prcess_plot import data_process

R_ST_span = 70          #距离R峰后N个采样点作为S段开始点
ST_span = 40            #N个采样点加权作为ST段基线
step = 5                #步长

def extract_ST_feature_02(File_type, File_num):
    # 整个导联数据读取以及预处理
    slopes = []
    warn = 0
    # 每个导联的ST基线获取
    for Channel in range(0, 12):
        pplt.daolian = Channel
        ST_line = 0
        warn = 0
        data, local = pplt.get_R_loca(File_type, File_num)
        local = np.array(local)
        for i in range(3):  # 取中间的R峰算起往后，共3个R峰
            if len(local) <= 10:
                warn += 1
                break
            num_R = local[(int(len(local) / 2)) + i]  # 中间的R峰的位置
            # 确定基线以及ST段的开始位置
            ST_start = num_R + R_ST_span
            # 根据设定的采样数从开始进行数据累加
            for i in range(0, ST_span):
                ST_line = ST_line + data[ST_start + i]
        # 3个R峰前后采集到的数据进行平均计算
        ST_line = ST_line / (ST_span * 3)
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
            slope = slope - ST_line*(int(len(st_segment)))
            if File_type == 'a':
                slope_sum = max(slope_sum, slope)
            elif File_type == 'b':
                slope_sum = min(slope_sum, slope)
            elif File_type == 'c':
                slope_sum = max(slope_sum, slope)
        # 把每个导联的计算结果加入到数组中
        slopes.append(slope_sum)
    return slopes, warn
