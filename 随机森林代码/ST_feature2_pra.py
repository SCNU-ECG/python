import ST_loca as ST
import prcess_plot as pplt
from ST_feature2 import extract_ST_feature_02
a = 'STD'; b = 'STE'; c = 'Others'; d = 'DE'

data_01,num = extract_ST_feature_02(b,12)
print("↓-------------this is shape-----------\n")
print(data_01)
print("--------------------------------------\n")
print(num)