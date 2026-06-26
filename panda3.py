#loc and iloc in pandas
#loc is label based
#iloc is index based
############
import pandas as pd
temp={'Name':['James Courbet','Emile Marechal','Enzo Descourts','Emile Faivre'],'Age':[15,16,14,15]}
df=pd.DataFrame(temp,index=['a','b','c','d'])
tt=pd.read_csv('titanic.csv')
print(df)
print(df.loc['a'])
print(df.iloc[1,1])
###########
#get the count of rows
print(df['Name'].value_counts())
#
print(df.groupby('Name')['Name'].count())
#sorting
tt.sort_values(by='Age',ascending=True,inplace=True)
print(tt[['Name','Age']].head())
tt.sort_values(by=['Pclass','Age'],ascending=True,inplace=True)
print(tt[['Name','Pclass','Age']].head())
#text data
tt['Surname']=tt['Name'].str.lower()
print(tt['Surname'])
df[['Surname','Last Name']]=df['Name'].str.split(' ',expand=True)
print(df)
df['First Name']=df['Name'].str.split(' ').str.get(0)
print(df)
###
tt['M/F']=tt['Sex'].replace({'male':'M','female':'F'})
print(tt.head())
