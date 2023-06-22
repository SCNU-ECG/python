from prcess_plot import data_process
import os
import time
import numpy as np
import scipy.io as sio
import pandas as pd
import ST_loca as st
import prcess_plot as pplt
import ST_feature2 as fea02
import Get_file_name as Get_basic
df = []
a = 'STD'; b = 'STE'; c = 'Others'; d = 'DE';

def get_feature(File_type,index_max,index_min):
    for index in range(index_min, index_max):
        print(index)
        data_01, warn = fea02.extract_ST_feature(File_type, index)
        if warn >= 8:
            print('AAA')
        else:
            data_02 = Get_basic.Get_type_int(File_type, index)
            data_01.append(data_02)
            if index == min(index_min, index_max):
                df = data_01
            else:
                df = np.concatenate([df, data_01])
    # #用于删除缺失值
    # df3 = df3.dropna(axis = 0, how = 'any')
    return df