import ST_loca as ST
import prcess_plot as pplt
a = 'STD'; b = 'STE'; c = 'Others'; d = 'DE'
for i in range(12):
    for a in range(11,13):
        Q_line, ST_line = ST.basic_line_st(b, a, i)


# shape, clopes = ST.extract_ST_feature(a, 0, 1)
# print("--------------this is shape-------------")
# print(shape)
# print("-----------this is clopes----------\n",clopes)