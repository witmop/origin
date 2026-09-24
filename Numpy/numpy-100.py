#https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises.ipynb
import numpy as np #1

# print(np.version) 
# print(np.show_config()) 2

# zero=np.zeros(10).astype(int) # 3 

# print(np.size(zero)) # 4

# print(np.info('add'))# 5

# zero[4]=1 # 6

# vector=np.arange(10,50)#7

# vector=vector[::-1]#8

# matrix=np.arange(1,10).reshape(3,3)#9

# vvod=np.array([1,2,0,0,4,0])
# nt_zeros=np.nonzero(vvod) #10

# iden_matrix=np.full(9,fill_value=1).reshape(3,3)#11

# rand_matrix=np.random.randint(0,100,size=(3,3,3))#12

# new_rand_matrix=np.random.randint(0,30,size=(10,10))
# print(new_rand_matrix)
# print(np.max(new_rand_matrix),np.min(new_rand_matrix))#13

# rand_vector=np.random.randint(0,100,size=(30))
# print(rand_vector.mean())#14

# array_2d=np.array([1,0]).reshape(2,1)
# print(array_2d)#15

# some_array=np.full(9,fill_value=1).reshape(3,3)
# some_array=np.pad(some_array,pad_width=1,mode="constant",constant_values=0)
# print(some_array)#16

# matrix_5=np.full(25,fill_value=10).reshape(5,5)
# np.fill_diagonal(matrix_5,[1,2,3,4,5])
# print(matrix_5)#18

# check_array=np.indices((8,8)).sum(axis=0)%2
# print(check_array)#19

# print(np.unravel_index(100,(6,7,8)))#20

# matrix=np.array([[1,2,3,4],[4,3,2,1]])
# checkboard=np.tile(matrix,(4,2))
# print(checkboard)#21

# random_matrix=np.random.randint(0,100,size=(5,5))
# M=random_matrix.mean()
# STD=random_matrix.std()
# normalize_matrix=np.zeros(25).reshape(5,5)
# for (i,j),x in np.ndenumerate(random_matrix):
#     normalize_matrix[i,j]=(x-M)/STD
# print(random_matrix)
# print(normalize_matrix)#22

# rgba_dtype=np.dtype([("R","u1"),("G","u1"),("B","u1"),("A","u1")])
# #u1 = 0-255
# colors=np.array([(255,0,120,0),(255,255,255,255)],dtype=rgba_dtype)#23

# matrix_1=np.random.randint(1,10,size=(5,3))
# matrix_2=np.random.randint(1,10,size=(3,2))
# print(np.matmul(matrix_1,matrix_2))# 24 умножение матриц matmul матричное умножение

some_array=np.random.randint(1,10,size=(8))
mask=(some_array>=3) & (some_array<=8)
some_array[mask]=-some_array[mask]
print(some_array)# 25 in-place замена чисела на отрицательные