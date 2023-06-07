import prcess_plot as pplt
import numpy as np
from prcess_plot import data_process

R_ST_span = 70          #距离R峰后N个采样点作为S段开始点
ST_span = 40            #N个采样点加权作为ST段基线

def extract_ST_feature_02(File_type, File_num, ST_line, Channel):
    pplt.daolian = int(Channel)
    name, array = data_process(File_type, File_num)
    array = pplt.data_reverse(array)
    data, local = pplt.get_R_loca(File_type, File_num)
    st_segments = []
    slopes = []
    num01 = []
    data_array = np.array(array[pplt.daolian])
    for i in range(0, int(len(local))):
        r_peak = local[i]
        #确定ST段的起始位置和结束位置，目前是固定长度，未来改成动态测量
        ST_start = int(r_peak + R_ST_span)
        ST_end   = int(ST_start + ST_span)
        #计算ST段面积
        st_segment = data[ST_start:ST_end]
        slope = np.sum(st_segment)
        slope = slope - ST_line
        slopes.append(slope)
        num01.append(i)
    return slopes
