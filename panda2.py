import pandas as pd
df=pd.read_csv('titanic.csv')
print(df)
print(df.info())
print('###')
print(df.describe())
print(df.dtypes)
name_age=df[['Name','Age']]
print('###')
print(name_age)
print('###')
print(name_age.head())
print('###')
abv_35=df[df['Age']>35]
print(abv_35)
print('###')
#we want to combine different conditions together
passenger_class2_3=df[df['Pclass'].isin([2,3])]
print(passenger_class2_3[['Name','Pclass']])
###
#pratice .loc
print('###')
print(df.iloc[9:25,2:5])
print('###')
print(df.loc[df['Age']>18,'Name'])
#change value
df.iloc[0:3,2]='Samuel'
print(df['Name'])
#make csv file
print('###')
df.to_csv('fake_titantic.csv')
###
df['Swimmer']=df['Fare']+2
print(df['Swimmer'])
df['New Fare']=df['Fare']*df['Pclass']
print(df['New Fare'])
#rename column
df_renamed=df.rename(columns={'Pclass':'Passenger Class','Fare':'Fares'})
print(df_renamed.info())
#mean value of 2 columns
print('###')
print(df[['Age','Fare']].mean())
print('###')
#affect the same operation on multiple columns
print(df.groupby('Age')['Fare'].mean())
#aggregation
print('###')
print(df.groupby('Age')['Fare'].agg(['sum','mean','max']))
