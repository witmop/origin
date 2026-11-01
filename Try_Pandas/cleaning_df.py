import pandas as pd
import numpy as np

main_df=pd.read_csv("cars.csv")
work_df=main_df.drop_duplicates()           #удаляем дубликаты
work_df=work_df.dropna(ignore_index=True)            #может удалить строки с na (потеря 815)
len_before=len(work_df)
work_df=work_df[(work_df["Year"].between(1951,2021))&
                (work_df["Distance"].between(0,1_000_000))&
                (work_df["Engine_capacity(cm3)"].between(200,5000))&
                (work_df["Price(euro)"].between(101,500_000))&
                ~((work_df["Year"]<2021)&(work_df["Distance"]<1100))]
    # Год с 1951 до 2021, пробег до 1_000_000, объём двигателя от 200 до 5000, цена от 101 до 500_000, также если авто моложе 2021 и пробег меньше 1100 тоже убрали

print(f"Сколько убрали аномальных строк: {len_before-len(work_df)}")
work_df=work_df.reset_index()

work_df=work_df.rename(columns={"Engine_capacity(cm3)":"Engine","Price(euro)":"Price"})     #Переименовали колонки для удобства
print(work_df.columns.to_list())

    #Добавим возраст авто и среднегодовой пробег
work_df["Age"]=2022-work_df["Year"]         
work_df["km_year"]=work_df["Distance"]/work_df["Age"]

    #Добавич колонку с понятным значением трансмиссии
work_df["Transmission"]=work_df["AutoTransmission"].map({True:"Automatic",False:"Manual"})

    #Разобьём значени пробега на условныые категории
def km_year_category(value):
    if value<=10_000:
        return "Small"
    elif value<=30_000:
        return "Medium"
    else:
        return "Large"
work_df["km_year_cat"]=work_df["km_year"].apply(km_year_category)

    #Создадим новый столбец, где марки, которые редко встречаются превратим в Rare
work_df["New_make"]=work_df["Make"].copy()
make_count=work_df["Make"].value_counts()
make_share=make_count/len(work_df)

rare_make=make_share.loc[make_share<=0.01].index

work_df.loc[work_df["New_make"].isin(rare_make),"New_make"]="Rare"
del work_df["index"]

#   Сохраняем первично обработанный DF
work_df.to_csv("cars_process.csv",index=False)
