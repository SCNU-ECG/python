import pandas as pd

data = "..\Train.xlsx"
#STE = pd.DataFrame(pd.read_excel(data))
STE = pd.read_excel(data)
count = STE.loc[(STE['STE'] == 0) & (STE['STD'] == 0) & (STE['Others'] == 1)]
print(count['Others'].value_counts(),'\n')

count = STE.loc[(STE['STE'] == 1) & (STE['STD'] == 0)]
print(count['STE'].value_counts(),'\n')

count = STE.loc[(STE['STE'] == 0) & (STE['STD'] == 1)]
print(count['STD'].value_counts(),'\n')

count = STE.loc[(STE['STE'] == 1) & (STE['STD'] == 1)]
print("STE and STD: \n",count['STD'].value_counts(),'\n')

num = STE.loc[(STE['STE'] == 0) & (STE['STD'] == 1)]
list_STE = list(num['name'])
print(list_STE)