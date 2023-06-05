import prcess_plot as pplt
import matplotlib.pyplot as plt

pplt.xfrom = 3500
pplt.xend = 6000

index = 25
a = 'STD'; b = 'STE'; c = 'Others'; d = 'DE'
# plt.figure(1)
# pplt.plot_DEO(d, index,12)

plt.figure(2)
pplt.plot_DEO(c, 0, 12)
plt.show()
'''


pplt.plot_DEO(a, index+7, 12)
plt.figure(2)
pplt.plot_DEO(b,index+7, 12)
plt.show()
'''


