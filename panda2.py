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
