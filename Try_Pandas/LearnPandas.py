import numpy as np
import pandas as pd


#Series
# some_series=pd.Series([1,2,3,4.2,5],
#                     index=["row1","row2","row3","row4","row5"],     #если передаём список, то кол-во индекса = кол-во элементов
#                     dtype="string",
#                     name="SomeSer"
#                        )
# print(some_series)

# dict_array={"row1":2,"row2":3,"row3":4,"row4":5,"row5":6}
# dict_series=pd.Series(dict_array,
#                       index=["row3","row4","row100"],        #если передаём словарь, то происходит поиск значений по индексам
#                       dtype=int,
#                       name="DictSer"
#                       )
# print(dict_series)

# np_array=np.array(range(5,10))
# series_from_array=pd.Series(np_array,
#                             copy=False          #данные также изменится в самом массиве если стоит False
#                             )
# print(series_from_array)
# series_from_array.iloc[2]=101
# print(series_from_array)
#передача series=dict


#DataFrame
# some_dict={"col1":[5,6,7,23,3],
#            "col2":[5,13,2,11,3],
#            "col3":[65,1,21,54,3],
#            "col4":[11,15,98,14,3]
#            }
# df=pd.DataFrame(some_dict,
#                 index=["row1","row2","row3","row4","row5"],
#                 columns=["col4","col1","5"],        #выборка
#                 dtype=float
#                 )
# print(df)

# some_array=np.random.randint(1,27,size=(5,5))
# df_1=pd.DataFrame(some_array,copy=True)
# print(df_1)
# df_1.iloc[:,3:5]=111
# print(df_1)

#Выравнивание индексов

# dict_array={"row1":2,"row2":3,"row3":4,"row4":5,"row5":6}
# df=pd.DataFrame({"col1":pd.Series(dict_array),
#                 "col2":pd.Series([5,6,6,np.nan,7],index=["row3","row4","row5","row6","row9"])},
#                 index=["row1","row2"]
#                 )
# print(df)

#Чтение и запись данных

# df=pd.read_csv("cars.csv",
#                index_col="Make",
#                usecols=["Style","Year","Fuel_type","Make"],
#                dtype={"Year":"category"},            #смена типа данных
#                nrows=5
#                #parse_dates=[["year","month","day"],"activation_date"(название столбца),"category_name"(название столбца)]  если есть возможно, то из исходного столбца получается year_month_day столбец с типом datetime
#                #keep_date_col=True       сохраняет изначальные столбцы после парсинга в дату
#                #encoding="utf-8"        кодировка файла
#                )
# print(df)
# print(df.info())

# df=pd.read_csv("cars.csv")

#df.to_csv("cars_copy.csv,
#           sep=";"
#           columns=["city","price"]  какие столбцы будут сохранены
#           header=True     сохранение названий стобцов
#           headers=["city_copy"]   другие названия столбцов
#           index=False     записывать индексы или нет
#           index_label="Название столбца с индексами"
#           ")


#Индексы

# list_index=list("qfmoq")

# index_data=pd.Index(list_index,
#                     name="rows",
#                     dtype="str"
#                     )
# columns_data=pd.Index(["col1","col2","col3"],
#                       name="cols"
#                       )

# df_data=pd.DataFrame({"col1":np.random.randint(1,30,size=5),
#                       "col2":np.random.randint(1,30,size=5),
#                       "col3":np.random.randint(1,30,size=5)},
#                       index=index_data,
#                       columns=columns_data
#                       )
# print(df_data)

# df=pd.DataFrame({f"c_{i}":np.arange(1000)*i for i in range(100)})
# index=df.index
# columns=df.columns
# columns.to_numpy()      #необязательно, просто пример

# print(index_data.unique())
# print(index_data.nunique())     #кол-во уникальных значений
# print(index_data.is_unique)    #все ли значения уникальные
# print(index_data.duplicated())

# index_data.name="rows_new"

# new_df=df_data.rename(columns={"col1":"col_1",
#                         "col2":"col_2",
#                         "col3":"col_3",
#                         "col4":"col_4"})        #можно писать лишние, ошибки не будет

# row_rename=new_df.rename(str.upper,axis=0)
# print(new_df)
# print(row_rename)

# index=pd.Index([1,np.nan,3,np.nan,5])

# df_nan=pd.DataFrame(np.arange(5),index=index)
# print(df_nan)
# print(df_nan.index.hasnans)     #проверка на наличие nan
# print(df_nan.index.isna())
# print(df_nan.index.dropna())


#Столбцы

# df=pd.DataFrame({"col1":np.random.randint(1,30,size=6),
#                  "col2":np.random.randint(1,30,size=6),
#                  "col3":np.random.randint(1,30,size=6),
#                  "col4":np.random.randint(1,30,size=6)})
# df.set_index(["col1","col4"],append=True,inplace=True)      #мультииндекс append осталяет изначальные индекса DF

# df.reset_index(["col4"],inplace=True)
# print(df)

# df=pd.DataFrame({"col1":np.random.randint(1,30,size=6),
#                  "столбец_2":np.random.randint(1,30,size=6),
#                  "col 3":np.random.randint(1,30,size=6),
#                  "col4":np.random.randint(1,30,size=6)})
# print(df["col 3"])#Series
# print(df[["col 3"]])#DataFrame
# df["new col"]=5         #новый столбец
# df["copy_col"]=df["col 3"]
# print(df)
# del df["copy_col"]

# #print(df[[False,True,False,True,True,False]])       #маска какие строки вывести

# df[[False,True,False,True,True,False]]=100
# print(df[[False,True,False,True,True,False]][["col 3"]])

# print(df.col1)


#Мультииндекса

# array=[[1,1,2,2],["row1","row2","row3","row4"]]
# multi_array=pd.MultiIndex.from_arrays(array,names=["level0","level1"])
# print(multi_array)

# df_index=pd.DataFrame([[4,3,2,1],[4,3,2,1],[4,3,2,1],[4,3,2,1]],index=multi_array)
# print(df_index)
# df_columns=pd.DataFrame([[4,3,2,1],[4,3,2,1],[4,3,2,1],[4,3,2,1]],columns=multi_array)
# print(df_columns)

# level_0=["row1","row2"]
# level_1=[1,2,3]

# multi_product=pd.MultiIndex.from_product([level_0,level_1],names=["level_0","level_1"])

# df_multi=pd.DataFrame([[4,3,2,1],[4,3,2,1],[4,3,2,1],[4,3,2,1],[4,3,2,1],[4,3,2,1]],index=multi_product)
# print(df_multi)
# print(df_multi.index.nlevels)           #уровни мультииндекса
# print(df_multi.index.levels)
# df_multi.index.droplevel()             #по умолчанию убирает 0 индекс


#Арифметически операции

# df_1=pd.DataFrame({"col1":[5,6,np.nan,3,7],
#                    "col2":[27,6,7,40,70],
#                    "col3":[1,45,6,62,7]},
#                    index=["row1","row2","row3","row4","row5"])


# df_2=pd.DataFrame({"col1":[5,6,3,np.nan,7],
#                    "col2":[27,6,7,40,70],
#                    "col3":[1,45,6,62,7]},
#                    index=["row1","row2","row3","row4","row5"])

# some_series=pd.Series([5,6,np.nan,1,7],
#                       index=["row_10","col2","row3","row4","row5"])


# print(some_series+5)
# print(some_series+[1,2,3,4,5])
# print(some_series+df_1["col1"])         #сложение происходит по названием индекса

# print(df_1+10)

# df_3=df_1.head(2)
# # print(df_3)
# df_4=df_1[["col1","col2"]]
# # print(df_4)
# # print(df_3+df_4)            #выравнивание индекса, там где ничего нет встаёт nan

# print(df_1.add([10,20,30],axis=1))         #выполнятеся вдоль строки, длина должна быть 3, если axis=0, то плюс идёт по столбцу

# print(df_3.add(df_4,fill_value=10))      #пропуски заполняются ун


#Операции сравнения

# df_1=pd.DataFrame({"col1":[5,6,np.nan,3,7],
#                    "col2":[27,6,7,40,70],
#                    "col3":[1,45,6,62,7]},
#                    index=["row1","row2","row3","row4","row5"])


# df_2=pd.DataFrame({"col1":[5,6,3,np.nan,7],
#                    "col2":[27,6,7,40,70],
#                    "col3":[1,45,6,62,7]},
#                    index=["row1","row2","row3","row4","row5"])

# some_ser=pd.Series([5,6,np.nan,1,7],index=["row1","row2","row3","row4","row5"])
# print(df_1["col1"]>=df_2["col1"])
# print(df_1==6)
# # print(df_1==df_2["col2","col1","col3"])  порядок индексов важен
# print(some_ser.le(df_1["col3"]))        #le даёт возможность сравнивать по разным индексам не по порядку
# print(df_1.le([10,20,30,7,8],axis=0))
# print(df_1.equals(df_1))


#Фильтрация данных

# dict_array={"age":np.random.randint(18,50,size=5), 
#             "name":["Саша","Женя","Маша","Юля","Люля"],
#             "наличие авто":[True,False,True,True,False]} 

# df=pd.DataFrame(dict_array)
# print(df)

# print(df[[True,False,True,True,False]])        #какие строки выводить, какие нет
# print(df[(df["age"]<25)&(df["наличие авто"])])
# print(df[(df["age"]<25)|~(df["наличие авто"])])     # ~==not 
# print(df[df["age"].isin([k for k in range(18,30)])])
# print(df.query("not `наличие авто` and age <28"))           #название столбцов должны быть в обратных кавычках если кирилица 


#Пропуски в данных

# dict_array={"age":[np.nan,24,35,18,61], 
#             "name":["Саша","Женя",np.nan,"Юля","Люля"],
#             "наличие авто":[np.nan,np.nan,np.nan,np.nan,np.nan]} 

# df=pd.DataFrame(dict_array)
# print(df.dropna())      #axis=0 (по умолчанию)-удаление строк
# # print(df.dropna(how='all',axis=1))
# print(df.dropna(subset=[1],axis=1))     
# print(df.fillna(value={"age":100,
#                        "name":"string",
#                        "наличие авто":False}))
# print(df.isna())
# print(df["age"].isna())
# print(df[~df["age"].isna()])            #только те строки, где в age нет пропуска
# print(df[df["name"].notna()])


#Удаление строк и столбцов

# df=pd.DataFrame({"col1":[5,6,3,np.nan,7],
#                    "col2":[27,6,7,40,70],
#                    "col3":[1,45,6,62,7]},
#                    index=["row1","row2","row3","row4","row5"])

# print(df.drop("row2"))
# print(df.drop(["col1","col2"],axis=1))
# print(df.drop(index="row1",columns="col2"))
# print(df.memory_usage())
# new_df=df.astype({"col2":np.int8})
# print(new_df.memory_usage())        #кол-во байтов на col2 уменьшилось
# print(new_df.info())                #стал занимать 297 байтов вместо 332   
# print(df.info())    


#Методы iat, at, iloc, loc

# dict_array={"age":np.random.randint(18,50,size=5), 
#             "name":["Саша","Женя","Маша","Юля","Люля"],
#             "наличие авто":[True,False,True,True,False]} 

# df=pd.DataFrame(dict_array,index=["row1","row2","row3","row4","row5"])

# print(df.iat[1,1])
# print(df["age"].iat[3])
# df.iat[4,1]="Кто-то"
# print(df)
# #df.at[] то же самое , но не по индексам, а по названияем

# print(df.iloc[1,1])
# print(df.iloc[df["наличие авто"].to_list(),[True,False,True]])
# df.iloc[1:3,[0]]=60
# print(df)
# #df.loc то же самое, но по названиеям

# print(df.loc[df["age"]==60])

# df.loc["row1":"row3",["age","name"]]=pd.DataFrame({"name":["Андрей","Вася","Буся"],
#                                                    "age":[22,34,35]},index=["row1","row2","row3"])
# print(df)


#Полезные методы

# dict_array={"age":np.random.randint(18,50,size=7), 
#             "name":["Саша","Женя","Маша","Юля","Люля","Буся","Андрей"],
#             "наличие авто":[True,False,True,True,False,True,False]}

# df=pd.DataFrame(dict_array,index=["row1","row2","row3","row4","row5","row6","row7"])
# print(df["age"].unique())
# print(df.nunique())
# print(df.value_counts())        #по умолчанию строки с nan не считаются чтобы считалось нужно сделать dropna=False 
# print(df["наличие авто"].value_counts())
# print(df.value_counts(["name","наличие авто"],normalize=True))
# print(df.sort_values("name"))       #na_position="first" пропуски будут вначале


#Метод apply()

# dct={f"col_{i}":[i*1,i*2,i*3,i*4,i*5] if i!=3 else [i,i,i,i,i] for i in range(5)}
# df=pd.DataFrame(dct)
# print(df.apply(np.min))
# def my_func(series):
#     return (series*100) if series.name!="col_2" else series * 0
# print(df.apply(my_func))
# print(df.apply(np.mean,axis=1))

# dict_array={"age":[53,27,92,18,15],
#             "name":["Фамилия_1 Имя_1",'Фамилия_2 Имя_2',"Фамилия_3 Имя_3 Отчество_3","Фамилия_4 Имя_4 Отчество_4","Фамилия_5 Имя_5"],
#             "наличие авто":[True,False,False,True,False]}

# df=pd.DataFrame(dict_array)

# def get_patronymic(name):
#     name_split=name.split(" ")
#     return name_split[-1] if len(name_split)!=2 else np.nan

# df["patronymic"]=df["name"].apply(get_patronymic)
# print(df)


#Агрегация данных   (превращение набора в одно значение)

# df=pd.DataFrame([[1,2,3],
#                  [4,5,6],
#                  [7,8,9],
#                  [np.nan,np.nan,np.nan]],columns=["col1","col2","col3"])

# print(df.min())
# print(df.mean())
# print(df.count())       #не учитывает nan
# print(df["col3"].sum())
# print(df.agg('mean'))
# def my_func(series):
#     return series.min()+100
# print(df.agg(my_func))
# print(df.agg([np.max,np.sum,np.mean]))
# print(df.agg(np.max,axis=1))        #по строкам
# print(df.agg({"col1":[np.min,np.max],
#               "col3":["mean"]}))
# print(df.agg(min_col1=("col1","min"),max_col2=("col2","max")))#именная агрегация


#Группировка данных

# df=pd.DataFrame({"имя":["name1","name2","name3","name3","name3","name2","name4"],
#                  "город_работы":["city1","city2","city3","city3","city4","city1",np.nan],
#                  "как_долго_работал":[12,24,36,12,48,5,np.nan]})

# print(df)
# groups=df.groupby("имя")
# for name,group in groups:
#     print(name)
#     print(group,end="\n\n")

# print(df.groupby("город_работы").sum())         #можно передать dropna=False
# print(df.groupby("имя",as_index=False).sum())       #столбец name не стал индексом
# print(df.groupby("имя")["как_долго_работал"].sum())
# print(df.groupby(["имя","город_работы"],dropna=False).count().rename(columns={"как_долго_работал":"count"}))
# print(df.groupby("имя")["город_работы"].nunique())

# print(df.groupby("имя").agg({'как_долго_работал':[np.sum,np.max],
#                              "город_работы":"count"}))


#Объединение данных

# df1 = pd.DataFrame({"A": ["A0", "A1", "A2", "A3"],
#                     "B": ["B0", "B1", "B2", "B3"],
#                     "C": ["C0", "C1", "C2", "C3"],
#                     "D": ["D0", "D1", "D2", "D3"]},
#                    index=[0, 1, 2, 3])

# df2 = pd.DataFrame({"A": ["A4", "A5", "A6", "A7"],
#                     "B": ["B4", "B5", "B6", "B7"],
#                     "C": ["C4", "C5", "C6", "C7"],
#                     "D": ["D4", "D5", "D6", "D7"]},
#                    index=[1, 2, 3, 4])

# df3 = pd.DataFrame({"A": ["A8", "A9", "A10", "A11"],
#                     "B": ["B8", "B9", "B10", "B11"],
#                     "C": ["C8", "C9", "C10", "C11"],
#                     "D": ["D8", "D9", "D10", "D11"]},
#                    index=[2, 3, 4, 5])

# print(pd.concat([df1,df2,df3],ignore_index=True))

# df_1 = pd.DataFrame({'client_id': [100103, 21990, 455323, 100103, 21990, 455323, 455323, 21990, 455323],
#                      'product': ['product_2', 'product_2', 'product_1', 'product_1', 'product_1', 'product_3',"product_3","product_3","product_3"]})

# df_2 = pd.DataFrame({'product': ['product_1', 'product_2', 'product_3', 'product_4', 'product_5'],
#                      'price': [1000, 2000, 3000, 4000, 5000]})

# print(df_1.merge(df_2,how="left"))
# print(df_1.merge(df_2,how="right"))
# print(df_1.merge(df_2,how="inner"))     #объединится только то, что есть в обоих DF (общие ищутся в общем столбце product)
# print(df_1.merge(df_2,how="outer"))     #объединяется всё
# #df_1.merge(df_2,how="inner",on="product") если несколько одинаковых столбцов, то можно указать по какому будет объединение

# df_1.rename(columns={"product":"prod"},inplace=True)
# print(df_1.merge(df_2,how="left",left_on=["prod"],right_on=["product"]))

# df_1 = pd.DataFrame({'product': ['product_1', 'product_2', 'product_3', 'product_4', 'product_5'],
#                      'count': [10, 20, 30, 40, 50]})

# df_2 = pd.DataFrame({'product': ['product_3', 'product_4', 'product_5', 'product_6', 'product_7'],
#                      'count': [100, 200, 300, 400, 500]})

# print(df_1.merge(df_2,how="outer",on="product",suffixes=["_shop_left","_shop_right"]))      #так как название count одинаковое то по умолчанию в итоговом df будет count_x и count_y их также можно переименовать


#Скользящие окна

df_date=pd.DataFrame({"col1":[0,1,2,3,4],
                      "col2":[90,91,92,93,94]})
print(df_date)
for window in df_date.rolling(3):
    print(window,end="\n\n")

print(df_date.rolling(3).sum())
print(df_date.rolling(3,min_periods=1).mean())      #min_periods минимальное кол-во наблюдение в окне при котором будет вовзращаться nan(то есть если ширина <1, то будет возращаться nan)
print(df_date.rolling(2).agg({"col1":"sum",
                              "col2":'mean'}))

df=pd.DataFrame({"sales":np.random.randint(0,50,100)},index=pd.date_range("2023",periods=100))
df_roll=df.rolling(7,min_periods=1).agg({"sales":["mean","max","sum","min"]})
df_roll.reset_index(inplace=True)
df_roll["weekday"]=df_roll["index"].dt.dayofweek    
print(df_roll[df_roll["weekday"]==6])