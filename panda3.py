#loc and iloc in pandas
#loc is label based
#iloc is index based
############
import pandas as pd
temp={'Name':['James','Emile','Enzo'],'Age':[15,16,14]}
df=pd.DataFrame(temp,index=['a','b','c'])
print(df)
print(df.loc['a'])
print(df.iloc[1,1])