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

df=pd.read_csv("cars.csv",
               index_col="Make",
               usecols=["Style","Year","Fuel_type","Make"],
               dtype={"Year":"category"},            #смена типа данных
               nrows=5
               )
print(df)
print(df.info())