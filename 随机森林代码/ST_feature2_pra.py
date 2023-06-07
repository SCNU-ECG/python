import ST_loca as ST
import prcess_plot as pplt
from ST_feature2 import extract_ST_feature_02
a = 'STD'; b = 'STE'; c = 'Others'; d = 'DE'
for i in range(12):
#    for index in range(11,13):
        Q_line, ST_line = ST.basic_line_st(b, 12, i)
        data_01,num = extract_ST_feature_02(b,12,ST_line,i)
        print("↓-------------this is shape-----------\n")
        print(data_01)
        print("--------------------------------------\n")
        print(num)