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


matr=np.asmatrix("1 2; 3 4")     #матрица 2x2
print(matr)
d=np.diag([1,2,4,5])
print(d)
df=np.diagflat([(1,2,3), (4,5,6), (7,8,9)])
print(df)
tr=np.tri(3)
print(tr)
some_arr=np.array([(1,2,3),(4,5,6),(7,8,9)])
print(np.tril(some_arr))