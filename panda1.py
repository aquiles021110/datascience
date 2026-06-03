import pandas as pd
data={'Name':['James','Andre'],'Age':[16,15]}
df=pd.DataFrame(data)
print(df)
print('###')
s=pd.Series([1,2,3])
print(s)
student_info={'Name':['Andre','Lucas','Sam','Enzo'],'Age':[14,15,17,16],'City':['Bristol','Sao Paulo','Jakarta','Seoul'],'Notes':[14,16,15,8]}
df2=pd.DataFrame(student_info)
print(df2.head())
print('###')
print(df2.tail())
