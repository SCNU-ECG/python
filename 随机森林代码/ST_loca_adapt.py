import prcess_plot as pplt
import numpy as np
from prcess_plot import data_process
import time
R_ST_span = 16          #距离R峰后N个采样点作为S段开始点
ST_span = 8            #N个采样点加权作为ST段基线

def extract_ST_feature(File_type, File_num):
    # 整个导联数据读取以及预处理
    feature_data = []
    warn = 0
    elapsed_time = 0
    # 每个导联的ST基线获取
    file_name, data_temp = data_process(File_type, File_num)#获取文件名和文件12导联数据
    data_temp = pplt.data_reverse(data_temp)
    for Channel in range(0, 12):
        pplt.daolian = Channel
        ST_line = 0
        start = time.time()
        data, local = pplt.get_R_loca(File_type, File_num, data_temp)
        end = time.time()
        elapsed_time += (end-start)
        local = np.array(local)
        for i in range(3):  # 取中间的R峰算起往后，共3个R峰
            if len(local) <= 6:
                warn += 1
                break
            num_R = local[(int(len(local) / 2)) + i]  # 中间的R峰的位置
            # 确定基线以及ST段的开始位置
            ST_start = num_R + R_ST_span
            # 根据设定的采样数从开始进行数据累加
            for i in range(0, ST_span):
                num = ST_start + i
                if num < 1500:
                    ST_line = ST_line + data[ST_start + i]
        # 3个R峰前后采集到的数据进行平均计算
        ST_line = ST_line / (ST_span * 3)
        # 初始化待存储变量
        area_sum_max, area_sum_min, slope_max, slope_min, peak_max, peak_min,curvature_max = 0, 0, 0, 0, 0, 0,0
        for i in range(0, int(len(local))):
            r_peak = local[i]
            possible = r_peak + 30
            for i in possible:
                # 确定ST段的起始位置和结束位置，目前是固定长度，未来改成动态测量
                ST_start = 
                ST_end   =
            print(ST_start,ST_end)
            if ST_start <= 1500 and ST_end <= 1500:
                # 计算ST段面积
                st_segment = data[ST_start:ST_end]
                area = np.sum(st_segment)
                area = area - ST_line*(int(len(st_segment)))
                area_sum_max = max(area_sum_max, area)
                area_sum_min = min(area_sum_min, area)
                # 计算斜率
                slope_max = max(np.max(np.gradient(st_segment)), slope_max)
                slope_min = min(np.min(np.gradient(st_segment)), slope_min)
                # 计算ST段峰值
                peak_max = max(np.max(st_segment), peak_max)
                peak_min = min(np.min(st_segment), peak_min)
                # 计算ST段曲率
                dx = np.gradient(st_segment)
                ddx = np.gradient(dx)
                curvature = ddx / (1 + dx ** 2) ** 1.5
                curvature_max = max(curvature)
            # 把每个导联的计算结果加入到数组中
        feature_data.append(area_sum_max)
        feature_data.append(area_sum_min)
        feature_data.append(slope_max)
        feature_data.append(slope_min)
        feature_data.append(peak_max)
        feature_data.append(peak_min)
        feature_data.append(curvature_max)
    print("程序执行时间为：", elapsed_time, "秒")
    return feature_data, warn
