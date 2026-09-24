import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("сars_no_dup.csv")
# sns.pairplot(data=df,hue="Transmission")
# plt.show()
num_columns=[]
cat_columns=[]
for column_name in df.columns:
    if (df[column_name].dtypes==int) or (df[column_name].dtypes==float):
        num_columns+=[column_name]
    else:
        cat_columns+=[column_name]
# Старый авто с низким пробегом
dist_year=df[(df.Year<2021)&(df.Distance<1100)]
df=df.drop(dist_year.index)
# Слишком большой пробег
dist=df[(df.Distance > 0.5e6)]
df=df.drop(dist.index)
# Слишком малый объём двигателя
engine=df[df["Engine_capacity(cm3)"]<200]
df.drop(engine.index)
# Слишком большой обём двигателя
engine=df[df["Engine_capacity(cm3)"]>5000]
df.drop(engine.index)
# Слишком низкие цены
price=df[df["Price(euro)"]<101]
df.drop(price.index)
# Слишком большие цены
price=df[df["Price(euro)"]>1e5]
df.drop(price.index)
# Слишком старые авто
year=df[df.Year<1971]
df.drop(year.index)
M=df[num_columns].mean()
STD=df[num_columns].std()
df_scaled=(df[num_columns]-M)/STD #Стандартизация
Xmin=df[num_columns].min()
Xmax=df[num_columns].max()
df_norm=(df[num_columns]-Xmin)/(Xmax-Xmin)#Нормализация
counts=df.Make.value_counts()# Кол-во авто по маркам
rare=counts[(counts.values<25)]
df["Make"]=df["Make"].replace(rare.index.values,"Rare")# Объединяеми редки марки авто
df["Transmission"]=df["Transmission"].map({"Automatic":1,"Manual":0})
df_ce=df.copy()
df_ce[cat_columns]=df_ce[cat_columns].astype("category")
for _, column_name in enumerate(cat_columns):
    df_ce[column_name]=df_ce[column_name].cat.codes
df_ohe=pd.get_dummies(df.copy())
df["Age"]=2026-df.Year
df["km_year"]=df.Distance/df.Age