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

df=pd.DataFrame({"col1":[5,6,3,np.nan,7],
                   "col2":[27,6,7,40,70],
                   "col3":[1,45,6,62,7]},
                   index=["row1","row2","row3","row4","row5"])

print(df.drop("row2"))
print(df.drop(["col1","col2"],axis=1))
print(df.drop(index="row1",columns="col2"))
print(df.memory_usage())
new_df=df.astype({"col2":np.int8})
print(new_df.memory_usage())        #кол-во байтов на col2 уменьшилось
print(new_df.info())
print(df.info())