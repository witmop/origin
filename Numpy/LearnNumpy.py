import numpy as np

# a=np.array([1,2,3,4])
# print(a)
# b = np.array([1,2,3,False,"124"])
# print(b[ [1,1,1,1,1,1] ]) #заменил единицу на 1 элемент
# print(b[[True,False,True,False,True]])


# print(np.sctypeDict)
# a=np.array([1,2,500,3000],dtype="int16")
# print(a.dtype)
# b=np.complex64(a)
# print(b)
# word_arr=np.array("Hello")      #будет создан массив состоящий из одного слова
# print(word_arr)


# a=np.array([0]*10)

# empty_arr=np.empty((3,2),dtype="int32")     #работают быстрее чем range
# print(empty_arr)
# b=np.eye(4,2)
# print(b)
# c=np.identity(5)
# print(c)
# t=np.zeros((2,3,4))
# print(t)
# k=np.ones([4,5],dtype="int32")
# print(k)
# f=np.full((3,2),-1)
# print(f)


# matr=np.asmatrix("1 2; 3 4")     #матрица 2x2
# print(matr)
# d=np.diag([1,2,4,5])
# print(d)
# df=np.diagflat([(1,2,3), (4,5,6), (7,8,9)])
# print(df)
# tr=np.tri(3)                #треугольная матрица
# print(tr)
# some_arr=np.array([(1,2,3),(4,5,6),(7,8,9)])
# print(np.tril(some_arr))            #triu противоположная функция


# a=np.arange(1,6,0.5)
# print(a)
# cos_a=np.cos(np.arange(0,np.pi,0.1))
# print(cos_a)

# b=np.linspace(0,np.pi,3)        #делит диапазон  от 0 до pi на 3 части и берёт по одному число из каждой
# print(b)

# a=np.fromstring("1, 2, 3",dtype="int16",sep=", ")
# print(a)
# def getRange(x,y):
#     return 100*x +y
# b=np.fromfunction(getRange,(4,5))
# print(b)



# a=np.array([0.1,0.2,0.3,0.4,0.5])
# print(a.dtype)
# a.dtype=np.int8()
# print(a)        #данных в 8 раз больше было float64 стало int8

# b=np.ones( (3,4,5) )
# print(b.ndim)
# print(b.shape)
# c=b.reshape(12,5)           #выглядят по-разному, но данные одни, если меняем что-то в b, то меняется и в c
# print(c)

a=np.array([1,2,3,4,5,6,7,8,9])
b=a.view().reshape(3,3)          #создаём копию массива а
print(b)
print(a)