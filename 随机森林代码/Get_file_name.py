import pandas as pd
import scipy.io as sio
from warnings import simplefilter
data = "Train.xlsx"  # 定义文件名
xlsx = pd.read_excel(data)    # 读取文件内容并构建成表格型的数据结构
simplefilter(action="ignore", category=FutureWarning)
def Get_name(a):
    if a == 'STE':
        # 选出STE的文件名
        sheet = xlsx.loc[(xlsx['STE'] == 1) & (xlsx['STD'] == 0)] 
        sheet = list(sheet['name'])   # 将表格数据转化为list数据，方便取出
    elif a == 'STD':
        # 选出STD的文件名
        sheet = xlsx.loc[(xlsx['STE'] == 0) & (xlsx['STD'] == 1)]
        sheet = list(sheet['name'])
    elif a == 'Others':
        # 选出Others的文件名
        sheet = xlsx.loc[(xlsx['STE'] == 0) & (xlsx['STD'] == 0)]
        sheet = list(sheet['name'])
    elif a == 'DE':
        # 选出STE的文件名
        sheet = xlsx.loc[(xlsx['STE'] == 1) & (xlsx['STD'] == 1)]
        sheet = list(sheet['name'])
    else:
        print("There is no this type!\n")
    return sheet

# 获取文件file_name属于的ST类型
def Get_type(file_name):
    result = xlsx.loc[xlsx['name'] == file_name]  # 定位文件名为file_name的内容
    STE = 'STE' + ' = ' + str(int(result['STE']))   # 将内容转换为str并字符串拼接
    STD = 'STD' + ' = ' + str(int(result['STD']))
    Others = 'Others' + ' = ' + str(int(result['Others']))
    result = STE + '  ' + STD + '  ' + Others   # 返回类型
    return result

# 获取文件属于的ST类型，作为标签
def Get_type_int(File_type, File_num):
    # 读取文件名字
    sheet = Get_name(File_type)
    # 设置sheet中第i个mat文件作为读取文件
    file = sheet[File_num]
    # 定位文件名为file_name的内容
    result = xlsx.loc[xlsx['name'] == file]
    if (int(result['STE']) == 1) & (int(result['STD']) == 0):
        num = 1
    elif (int(result['STE']) == 0) & (int(result['STD']) == 1):
        num = 2
    elif (int(result['STE']) == 1) & (int(result['STD']) == 1):
        num = 3
    elif int(result['Others']) == 1:
        num = 0
    else:
        num = 0
    return num