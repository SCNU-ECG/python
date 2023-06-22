import prcess_plot as pplt
import matplotlib.pyplot as plt
import Get_file_name as Get
pplt.xfrom = 10
pplt.xend = 1500

index = 106
a = 'STD'; b = 'STE'; c = 'Others'; d = 'DE'
# plt.figure(1)
# pplt.plot_DEO(d, index,12)
name = Get.Get_type_int(d, 14)
print(name)
plt.figure(2)
pplt.plot_DEO(d, 14, 12)
plt.show()
'''


pplt.plot_DEO(a, index+7, 12)
plt.figure(2)
pplt.plot_DEO(b,index+7, 12)
plt.show()
'''


