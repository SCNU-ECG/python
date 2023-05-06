import scipy.io as sio
import matplotlib.pyplot as plt
from pylab import *
from Get_file_name import Get_name
from Get_file_name import Get_type
from scipy import signal        #导入滤波器的库
import Pan_Tompkins as pt
from scipy import signal
from Pan_Tompkins import fs

mwin = [[], [], [], [], [], [], [], [], [], [], [], []]
bpass = [[], [], [], [], [], [], [], [], [], [], [], []]
ecg1 = [[], [], [], [], [], [], [], [], [], [], [], []]
ecg2 = [[], [], [], [], [], [], [], [], [], [], [], []]
ecg3 = [[], [], [], [], [], [], [], [], [], [], [], []]
ecg4 = [[], [], [], [], [], [], [], [], [], [], [], []]

global xfrom ;  xfrom = 0        #绘图的开始位置
global xend ;   xend = 6000         #绘图的结束位置

SG_window = 60  #SG滤波缓存大小
SG_k = 6        #SG拟合系数

#定义基线漂移函数
t1 = int(0.2*500)
t2 = int(0.6*500)

#R峰绘制线宽
ld = 0.7

'''函数说明：
    参数：  File_type:从abcd中对应四种不同类型文件
            File_num:某一种类型的文件中第num个文件
            Channel_num:需要显示的导联数
            SG_window:SG滤波器的windo参数大小
            SG_k:SG滤波器的k值参数大小
使用改函数，进行文件数据处理并绘图
'''

def data_process(File_type, File_num):
    '''
    使用该函数对文件类型为File_type, 第File_num个文件进行数据处理
    处理为SG滤波器平滑处理
    return 值为找到的文件名"xxx.mat", 和处理完的数据data_array
    '''
    #读取文件名字
    sheet = Get_name(File_type)
    #设置sheet中第i个mat文件作为读取文件
    file = "..\\data_set\\"+sheet[File_num]
    data_mat = sio.loadmat(file)#读取mat文件中的数据

    data_array =(data_mat['ecg']) #将数据中的ecg数据12导联导出

    #使用Savitzky-Golay 滤波器实现曲线平滑
    # k值6对大，越接近真实曲线，越小越平滑。
    #window_length值50为数据缓存长度，越小越贴近原曲线，越大越平滑
    if(SG_k != 0 | SG_window != 0):
        data_array = signal.savgol_filter(data_array, SG_window, SG_k)
        
    for i in range(0, len(bpass)):
        data_array[i] = pt.band_pass_filter(data_array[i])

#对数据进行基线漂移处理
    data_array = deal_base_line(data_array)
    file = sheet[File_num]

    return  file,data_array


def data_DEO(File, data_array, Channel_num):
    '''
    对传入的数据data_array和Channel_num进行绘图
    param:
        File:传入的文件名，用于绘图时显示
        data_array:根据此数据进行绘图
        Channel_num:绘制图像数
    '''
    ST_type = Get_type(File)
    if((Channel_num+1) % 2 != 0):
        row = (Channel_num)
    else:
        row = (Channel_num+1)
    for i in range(0,Channel_num):#导联数据范围
        y = data_array[i]   #取出某导联i处数据
        plt.subplot(int(row/2),2,i+1)
        plt.plot(y, linewidth = ld)
        plt.title(File + '  channel %d ' %(i+1) + ST_type)
        plt.subplots_adjust(hspace = 1)     #设置每个图像之间的间距
        plt.xlim(xfrom,xend)                    #设置x的显示范围



def plot_DEO(File_type, File_num, Channel):
    '''
    使用该函数进行绘图，结合data_process和data_DEO形成完整绘制，调用时只需要传参就好
    使用带通滤波对每个导联数据进行处理
    
    '''
    name, bpass = data_process(File_type, File_num)
    data_DEO(name, bpass, Channel)

#巴沃特斯滤波器，暂时用不到
def Butter_band_pass(unfiltered_ecg_signal, fs):
    nyquist = 0.5 * fs
    low_cutoff = 5 / nyquist
    high_cutoff = 15 / nyquist
    coeff = signal.butter(2, [low_cutoff, high_cutoff], analog=False, btype='band', output='sos')
    filtered_signal = signal.sosfilt(coeff, unfiltered_ecg_signal) 
    return filtered_signal


#绘制寻找并R峰函数
def plot_R_peak(File_type, File_num, Channel):
    __file_name__, data = data_process(File_type, File_num)#获取文件名和文件12导联数据
    for i in range(0, Channel):
        mwin[i] = pt.solve(data[i])
        hr = pt.heart_rate(data[i], fs, mwin[i])
        result = hr.find_r_peaks()
        result = np.array(result)
        result = result[result > 0]
        plt.subplot(6,2,i+1)
        # Plotting the R peak locations in ECG signal
        plt.plot(data[i], linewidth = ld)        
        plt.scatter(result, data[i][result.astype('int64')], color = 'red', s = 50, marker= '*')
        plt.xlim(xfrom, xend)

def normalize(data):
   # data = data.astype('float')
    mx = np.max(data,axis=0).astype(np.float64)
    mn = np.min(data,axis=0).astype(np.float64)
    return np.true_divide(data-mn,mx-mn,out=np.zeros_like(data-mn),where=(mx-mn)!=0)

def deal_base_line(data_array):
    for i in range(0,12):
        ecg1[i] = data_array[i]
        ecg1[i] = normalize(ecg1[i])
        ecg2[i] = signal.medfilt(ecg1[i],t1+1)
        ecg3[i] = signal.medfilt(ecg2[i],t2+1)
        ecg4[i] = ecg1[i] - ecg3[i]

    return ecg4