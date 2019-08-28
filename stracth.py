import pandas as pd
import numpy as np

a = {'a':[1,2,3], 'b' : [18,2,121]}

df = pd.DataFrame(a)
print(df)

print()

a = df['b'].tolist()
a.sort()
df_a = pd.DataFrame(a,columns=['Diff'])
#a.sort_values(by=['b'])

print(a)
print(df_a)