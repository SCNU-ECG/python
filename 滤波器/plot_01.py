import pywt
import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
from scipy.signal import medfilt
from scipy import signal
from Get_file_name import Get_name
from Get_file_name import Get_type

#去除基线漂移
#读取文件中的数据
sheet = Get_name('STD')
file ="..\\data_set\\" + sheet[0]
Inidata = sio.loadmat(file)
data_y_array = Inidata['ecg']
ST_type = Get_type(sheet[0])

ecg1=data_y_array[1]
def normalize(data):
    data = data.astype('float')
    mx = np.max(data,axis=0).astype(np.float64)
    mn = np.min(data,axis=0).astype(np.float64)
    
    return np.true_divide(data-mn,mx-mn,out=np.zeros_like(data-mn),where=(mx-mn)!=0)

t1 = int(0.2*500)
t2 = int(0.6*500)

for i in range(0,12):
    # ecg1=data_y_array[i]
    plt.subplot(3,4,i+1)
    # b = signal.firwin(51,0.1,fs=500)
    # ecg3 = signal.lfilter(b,1,ecg1)
    ecg1=data_y_array[i]
    ecg1 = normalize(ecg1)
    ecg2 = medfilt(ecg1,t1+1)
    ecg3 = medfilt(ecg2,t2+1)
    ecg4 = ecg1-ecg3
    plt.plot(ecg4)
    plt.xlim(0,2000)
    plt.xticks(range(0,2000,500))
    plt.title(sheet[0] + '  channel %d ' %i + ST_type)
    plt.subplots_adjust(hspace = 0.5)
    # y = data_y_array[i]
    # plt.subplot(3,4,i+1)
    # plt.plot(y, linewidth = 1)
    # plt.xlim(0,500)
    # plt.title(sheet[0] + '  channel %d ' %i + ST_type)
    # plt.subplots_adjust(hspace = 0.5)
plt.show()