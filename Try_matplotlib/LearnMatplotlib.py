import matplotlib
import matplotlib.pyplot as plt 
import numpy as np

# print(matplotlib.get_backend())


#Функция plot
# x=np.array([1,3,6,9,10])
# plt.plot(x,[1,2,-6,0,4])      #лучше использовать np.array()
# plt.show()

# x=np.array([1,1,5,5,1])
# y=np.array([1,5,5,1,1])
# plt.plot(x,y)       #квадрат
# plt.show()

# y=np.arange(1,10,1)
# x=np.array([num**2 for num in y])

# x1=[0,1,2,3]
# y1=[i*2 for i in x1]
# plt.plot(x,y,x1,y1)     #также можно дописать снизу plt.plot(x1,y1) будет то же самое
# plt.grid()      #включает сетку
# plt.show()

# y=np.arange(1,10,1)
# x=np.array([num**2 for num in y])

# lines=plt.plot(x,y,"--r",marker="s",markerfacecolor="w",linewidth=4)  #"-"-просто линия "-."-штрих пунктир ":"-пунктир None или " "-без линии
# # plt.setp(lines,linestyle=":")
# plt.grid()      
# plt.show()

x=np.arange(-2*np.pi,2*np.pi,0.1)
y=np.cos(x)
plt.plot(x,y)
plt.fill_between(x,y,where=(y<0),color="r",alpha=0.5)
plt.fill_between(x,y,where=(y>0),color="b",alpha=0.5)

plt.grid()
plt.show()