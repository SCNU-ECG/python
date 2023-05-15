import prcess_plot as pplt
import matplotlib.pyplot as plt

pplt.xfrom = 3500
pplt.xend = 6000

index = 13
a = 'STD'; b = 'STE'; c = 'Others'; d = 'DE'

pplt.plot_DEO(b, index+15,12)
plt.show()
'''


pplt.plot_DEO(a, index+7, 12)
plt.figure(2)
pplt.plot_DEO(b,index+7, 12)
plt.show()
'''


