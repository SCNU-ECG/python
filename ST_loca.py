import prcess_plot as pplt



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
        num_R = loca[(int(len(loca)/2)) + i]  #中间的R峰的位置
        
        #确定基线以及ST段的开始位置
        QQ_start = num_R - R_QQ_span
        ST_start = num_R + R_ST_span

        #根据设定的采样数从开始进行数据累加
        for i in range(0, QQ_span):
            Q_line = Q_line + data[QQ_start + i]

        for i in range(0, ST_span):
            ST_line = ST_line + data[ST_start + i]
    
    #3个R峰前后采集到的数据进行平均计算
    Q_line = Q_line/(QQ_span*3)    
    ST_line = ST_line/(ST_span*3)


    if(ST_line < Q_line):
        print("This is STD:","Q_line = {}, ST_line = {}".format(Q_line,ST_line))
    elif(ST_line == Q_line ==0):
        print("All is 0")
    else:
        print("This is STE:","Q_line = {}, ST_line = {}".format(Q_line,ST_line))
    return Q_line, ST_line