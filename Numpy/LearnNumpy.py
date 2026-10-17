import numpy as np

# a=np.array([1,2,3,4])
# print(a)
# b = np.array([1,2,3,False,"124"])
# print(b[ [1,1,1,1,1,1] ]) #заменил единицу на 1 элемент
# print(b[[True,False,True,False,True]])


# print(np.sctypeDict)
a=np.array([1,2,500,3000],dtype="int16")
print(a.dtype)
b=np.complex64(a)
print(b)
word_arr=np.array("Hello")
print(word_arr)