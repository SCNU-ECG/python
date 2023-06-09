import prcess_plot as pplt
import matplotlib.pyplot as plt
import Get_file_name as Get
pplt.xfrom = 100
pplt.xend = 6000

index = 106
a = 'STD'; b = 'STE'; c = 'Others'; d = 'DE'
# plt.figure(1)
# pplt.plot_DEO(d, index,12)
name = Get.Get_type_int(a, 12)
print(name)
plt.figure(2)
pplt.plot_DEO(d, 106, 12)
plt.show()
'''


pplt.plot_DEO(a, index+7, 12)
plt.figure(2)
pplt.plot_DEO(b,index+7, 12)
plt.show()
'''


