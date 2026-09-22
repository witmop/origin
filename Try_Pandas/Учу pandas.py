import pandas as pd
df=pd.read_csv("cars.csv")
print(df.duplicated().sum())
DF=df.drop_duplicates().reset_index(drop=True)
DF.to_csv("сars_no_dup.csv",index=False)