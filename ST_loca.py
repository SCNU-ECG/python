import prcess_plot as pplt
import numpy as np


R_QQ_span = 55          #距离R峰前N个采样点作为Q段开始点
R_ST_span = 70          #距离R峰后N个采样点作为S段开始点

QQ_span = 30            #N个采样点加权作为Q段基线
ST_span = 40            #N个采样点加权作为ST段基线



def basic_line_st(File_type, File_num, daolian):
    '''
    参数：File_type:    要判断的ST段类型
            File_num：  第num个文件
            daolian：   要判断文件中哪个导联的数据
    '''
    pplt.daolian = daolian
    Q_line = 0
    ST_line = 0

    data , loca = pplt.get_R_loca(File_type, File_num)
    for i in range(3):                      #取中间的R峰算起往后，共3个R峰
        if(len(loca) == 0):
            break
        num_R = loca[(int(len(loca)/2)) + i]  #中间的R峰的位置
        
        #确定基线以及ST段的开始位置
        QQ_start = num_R - R_QQ_span
        ST_start = num_R + R_ST_span

        #根据设定的采样数从开始进行数据累加
        for i in range(0, QQ_span):
            if(abs(data[QQ_start + i]) > 0.1):  
                data[QQ_start + i] = 0
            Q_line = Q_line + data[QQ_start + i]

        for i in range(0, ST_span):
            ST_line = ST_line + data[ST_start + i]
    
    #3个R峰前后采集到的数据进行平均计算
    Q_line = Q_line/(QQ_span*3)    
    ST_line = ST_line/(ST_span*3)


    if(ST_line < Q_line):
        print("This is STD:","Q_line = {}, ST_line = {}, 差值 = {}".format(Q_line,ST_line, abs(Q_line - ST_line)))
    elif(ST_line == Q_line ==0):
        print("All is 0")
    else:
        print("This is STD:","Q_line = {}, ST_line = {}, 差值 = {}".format(Q_line,ST_line, abs(Q_line - ST_line)))
    return Q_line, ST_line

# def ST_line_judge(File_type, File_num):
#     STE_count = 0
#     STD_count = 0
#     for i in range(12):
#         Q_line, ST_line = basic_line_st(File_type, File_num, i)
#         if(ST_line )

def extract_ST_feature(File_type, File_num, Channel):
    pplt.daolian = Channel

    data, local = pplt.get_R_loca(File_type, File_num)

    st_segments = []
    slopes = []
    for i in range((int(len(local)/2 - 1)), (int(len(local)/2)) + 3):
        r_peak = local[i]
        #确定ST段的开始位置
        ST_start = int(r_peak + R_ST_span)
        ST_end   = int(ST_start + ST_span)
        #ST段形状数据
        st_segment = data[ST_start:ST_end]
        st_segments.append(st_segment)
        #计算ST段斜率
        slope = np.mean(np.diff(st_segment))
        slopes.append(slope)

    return np.sum(st_segments), np.mean(slopes)
