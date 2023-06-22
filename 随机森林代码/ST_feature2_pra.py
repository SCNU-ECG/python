import ST_loca as ST
import time
import prcess_plot as pplt
from ST_feature2 import extract_ST_feature
a = 'STD'; b = 'STE'; c = 'Others'; d = 'DE'
start = time.time()
data_01, num = extract_ST_feature(b,10)
end = time.time()
elapsed_time = end - start
print("↓-------------this is shape-----------\n")
print(data_01)
print("--------------------------------------\n")
print(num)
print("程序执行时间为：", elapsed_time, "秒")