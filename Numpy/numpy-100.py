#https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises.ipynb
import numpy as np#1

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

# some_array=np.random.randint(1,10,size=(8))
# mask=(some_array>=3) & (some_array<=8)
# some_array[mask]=-some_array[mask]
# print(some_array)# 25 in-place замена чисела на отрицательные

# print(sum(range(5),-1))# 0+1+2+3+4-1
# print(np.sum(range(5),-1))# 26 в numpy на месте -1 -это по какой оси суммировать 

# Z=np.random.randint(0,10,size=(5))
# print(Z)
# print(Z**Z)
# print(2 << Z >> 2)#быстрая операция её суть 2**(z-1) <<-побитовый сдвиг влево 3=0011, после =1100=12 (2 << Z) тоже самое как и **2
# print(Z <- Z)
# print(1j*Z)
# print(Z/1/1)
# print(Z<Z>Z) 27

# print(np.array(0) / np.array(0))
# print(np.array(0) // np.array(0))
# print(np.array([np.nan]).astype(int).astype(float)) #28

# some_array=np.array([3.2,1.8,3.5,65.13,11.0])
# print(np.ceil(some_array).astype(int))#29 

# first_array=np.array([3,56,22,13,11])
# second_array=np.array([53,3,28,90,76,11])
# result=np.intersect1d(first_array,second_array)# как найти схожие значения
# print(result)#30

# np.seterr(all="ignore") # глобально отключает проверку арифмитических выражний( например деление на 0)
# with np.errstate(all="ignore"):# в определённом месте
#     x=np.array([0.0])
#     y=x/x #31

# print(np.sqrt(-1) == np.emath.sqrt(-1)) # 32 False так-как первое это nan(то есть не такого числа, а во втором случае система автоматически перешла в комплексные числа и выдала 0+1i)

# today=np.datetime64("today","D")
# yesterday=today-np.timedelta64(1,"D")
# tomorrow=today+np.timedelta64(1,"D")
# print(today,yesterday,tomorrow) #33

# year,month=2016,7
# start=f"{year:04d}-{month:02d}"
# end=f"{year:04d}-{(month%12)+1:02d}" if month!=12 else f"{year+1:04d}-01"#04d и 02d нужно чтобы если число например 2016-9(datetime не поддерживает) писало 2016-09 
# dates=np.arange(start,end,dtype="datetime64[D]")
# print(dates)#34

# a=np.random.randint(0,10,size=(5)).astype(float)
# b=np.random.randint(5,20,size=(5)).astype(float)
# temp=np.empty_like(a)
# np.negative(a,out=temp)
# np.divide(temp,2,out=temp)
# np.add(a,b,out=a)
# np.multiply(a,b, out=a)
# np.multiply(a,temp,out=a)# не совсем понял как сделать in place temp-единсветнный временный массив
# print(a)#35

# arr=np.random.randint(0,10,size=10)
# print(arr)
# print(np.floor(arr).astype(int))#округление вниз
# print(np.trunc(arr).astype(int))#отбрасывания дробной части
# print(arr.astype(int))# отбрасывания дробной части(жёсткое усечение) прямое приведение
# quot,remainder =np.divmod(arr,1) # целая часть и остаток от деления на 1
# print(quot.astype(int)) #36

# row=np.arange(5)
# matrix=np.tile(row,(5,1))#берёт массив row и повторяет его 5 раз по строкам и 1 раз по столбцам
# print(matrix) #37

# def gen_10_inits():
#     for i in range(10):
#         yield i*2# генератор отдаёт значение, пауза, продолжает с места где остановился, return вовзращает только 1 раз, а yield хоть сколько
# new_arr=np.fromiter(gen_10_inits(),dtype=int,count=10)# как сделать из генератора массив
# print(new_arr) #38

# vector=np.random.random(size=(10))
# print(vector)#39

# some_array=np.random.randint(0,30,size=(10))
# print(some_array)
# some_array=np.sort(some_array)
# print(some_array) #40

# ar=np.arange(10)
# print(sum(ar))#41 для маленьких массивов примерно до 64 np.sum() проигрывает из-за проверки типов, создания объектов, диспетчеризации

# A=np.array([0,3,5])
# B=np.array([0,14,2])
# print(np.array_equal(A,B)) # 42 проверка на схожесть или np.equal(A,B) проверка по каждому элементу


# arr=np.arange(10)
# arr.flags.writeable=False #43 read-only вектор

# coords_xy=np.random.uniform(-10,10,size=(10,2))
# x=coords_xy[:,0]
# y=coords_xy[:,1]
# r=np.sqrt(x**2+y**2) # радиус
# theta=np.arctan2(y,x)# угод в радианах
# coords_polar_rad=np.column_stack((r,theta))
# print(coords_xy)
# print(coords_polar_rad) #44

# some_vector=np.random.randint(0,30,size=(10))
# print(some_vector)
# some_vector[some_vector==some_vector.max()]=0
# print(some_vector)#45

# coords=np.random.uniform(-0.1,0.1,size=(5,2))
# print(coords) #46

# x=np.array([1,2,7,9])
# y=np.array([13,5,17])
# D=np.subtract.outer(x,y)#матрица разностей
# C=1.0/D# матрица Коши
# print(D)
# print(C) #47

# types={}#48 пропуск

array=np.random.randint(-20,20,size=(4,4))
for x in array.flat:#flat даёт возможность выводить не только 1D массивы
    print(x)#49

vec=np.array([3,7,13,19,2])
target=15
diffs=np.abs(vec-target)
idx=np.argmin(diffs)
closest=vec[idx]
print(closest) #50