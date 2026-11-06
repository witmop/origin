import matplotlib
import matplotlib.pyplot as plt 
import numpy as np
from matplotlib.gridspec import GridSpec
from matplotlib.ticker import NullLocator,LinearLocator,MultipleLocator,IndexLocator,FixedLocator,LogLocator
import matplotlib.ticker as mtc
from matplotlib.lines import Line2D
import matplotlib.patches as ptc 

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

# x=np.arange(-2*np.pi,2*np.pi,0.1)
# y=np.cos(x)
# plt.plot(x,y)
# plt.fill_between(x,y,where=(y<0),color="r",alpha=0.5)
# plt.fill_between(x,y,where=(y>0),color="b",alpha=0.5)

# plt.grid()
# plt.show()


#Отображение нескольких координатных осей

# plt.subplot(2,3,1)      #1 строка 3 столбца индекс графика 1
# plt.plot(np.random.random(10))
# plt.subplot(2,3,2) #==232
# plt.plot(np.random.random(10))
# plt.subplot(2,3,3)
# plt.plot(np.random.random(10))
# # plt.grid()          #применится только к последнему графику
# plt.subplot(2,1,2)
# plt.plot(np.random.random(10))

# plt.show()
# fig=plt.figure(figsize=(7,4))
# ax1=fig.add_axes([0.0,0,1.0,1.0])       #ось в разммер окна
# ax1.plot(np.arange(0,5,0.5))


# f,ax=plt.subplots(2,2)      #разбивка 2 строки и 2 столбца
# f.set_size_inches(7,4)
# f.set_facecolor("darkred")

# ax[0,0].plot(np.arange(0,5,0.2))
# ax[0,0].grid()

# ax[0,1].plot(np.arange(5,0,-0.2))
# ax[0,1].grid()
# plt.show()

# ws=[1,2,5]
# hs=[2,0.5]      #компановка осей, какую часть относительно других клеток занимает клетка
# fig=plt.figure(figsize=(7,4))

# gs=GridSpec(ncols=3,nrows=2,figure=fig,width_ratios=ws,height_ratios=hs)
# ax1=plt.subplot(gs[0,0])
# ax1.plot(np.arange(0,5,0.2))
# ax2=fig.add_subplot(gs[1,0:2])
# ax2.plot(np.random.random(10))
# ax3=fig.add_subplot(gs[:,2])
# ax3.plot(np.random.random(10))

# plt.show()


#Граничные значения, метки осей

# fig=plt.figure(figsize=(7,4))
# ax=fig.add_subplot()
# ax.plot(np.arange(1,5,0.25))
# ax.set(xlim=(-5,30),ylim=(-1,6))    #или ax.set_xlim(xmin=,xmax=)
# ax.grid()
# ax.yaxis.set_major_locator(NullLocator())      #ушли горизонтальные линии
# ax.yaxis.set_major_locator(LinearLocator(10))     #ось y разбилась на 10 равных частей
# ax.xaxis.set_major_locator(MultipleLocator(2.5))  #через какое знач будет стоять метка

# x=np.arange(-np.pi/2,np.pi,0.1)
# ax.plot(x,np.sin(x))
# ax.grid()
# ax.xaxis.set_major_locator(IndexLocator(base=0.5,offset=0.57))      #как Multiple, но можно задать начальное значение
#FixedLocator([1,3,5,-2])   конкретные точки
# ax.xaxis.set_major_locator(LogLocator(base=2))      #логарифмический масштаб
#MaxNLocator(5)  максимальное кол-во рисок (необязательно будет 5), он будет будет подбирать удобное кол-во, чтобы были ровные числа
# ax.minorticks_on()  #включение доп сетки
# ax.grid(which="major",lw=2)
# ax.grid(which="minor")  #ax.xaxis.set_minor_locator(...)

# plt.show()


#Формат отображения

# def format_func(x,pos):
#     return f"[{x}]" if x<0 else f"({x})"

# fig=plt.figure(figsize=(7,4))
# ax=fig.add_subplot()
# x=np.arange(-np.pi/2,np.pi,0.1)
# ax.plot(x,np.sin(x))
# ax.xaxis.set_major_formatter(mtc.NullFormatter())     пропадут значения по Ox
# ax.yaxis.set_major_formatter(mtc.FormatStrFormatter("%d"))      #округление чисел
# ax.yaxis.set_major_formatter(mtc.FuncFormatter(format_func))        #можно вставить свою функцию
# ax.yaxis.set_major_formatter(mtc.ScalarFormatter())     #выносит большную степень например 10**10(по умолчанию) можно сделать .set_power_limits()
# ax.yaxis.set_major_formatter(mtc.FixedFormatter(["a","b","c","d","g"]))    #как назвать отображаемые значения


# plt.grid()
# plt.show() 


#Логарифмический масштаб

# fig=plt.figure(figsize=(7,4))
# ax=fig.add_subplot()
# x=np.arange(-10*np.pi,10*np.pi,0.5)
# y=np.sinc(x)*np.exp(-abs(x/10))
# # ax.semilogy(x,y)        #логарифмический мастштаб по оси y 
# ax.plot(x,y)
# ax.set_yscale("log",base=10,subs=[2,9])        #логарифмический масштаб с основанием 10

# plt.grid()
# plt.show()


#Оформление графиков
# fig=plt.figure(figsize=(7,4),facecolor="#eee")      #или fig.set(facecolor="...")
# ax=fig.add_subplot()
# plt.figtext(0.5,0.5,"Текст в середине окна",fontsize=13,color="darkred")

# x=np.arange(-5,5,0.1)
# y1=x**2+1
# y2=(x*10)**0.5
# ax.plot(x,y1,x,y2)
# ax.annotate("Аннотация",xy=(-2,2),xytext=(-3,10),
#             arrowprops={"facecolor":"grey","shrink":0.1})
# ax.text(-4,25,"Текст в коорд. осях",bbox={"boxstyle":"darrow","facecolor":"blue"})
# ax.set(facecolor="darkgreen")

# plt.xlabel("Ox")
# plt.title("Заголовк")
# plt.grid()
# plt.show()


#Легенда и фигуры на графиках

# fig=plt.figure(figsize=(7,4))
# ax=fig.add_subplot()

# l1=Line2D([1,2,5],[2,5,8])
# rect=ptc.Rectangle((0,0),10,5,facecolor="darkgreen")

# ax.plot(np.arange(0,5,0.25),"--o",label="line 1")
# ax.plot(np.arange(0,10,0.5),":s",label = "line 2")
# ax.add_line(l1)
# #если add_line - единственный график, то нужно указать ax.set(xlim=(...),ylim=(...)) иначе на графике будут значение по умолчанию от 0 до 1
# ax.add_patch(rect)

# plt.legend(["1","2"],bbox_to_anchor=(0.2,0.7),framealpha=0.5)       #label игнорируется
# plt.show()  


#Виды графиков

fig=plt.figure(figsize=(10,5))
ax=fig.add_subplot()

#Ступенчатый график
# x=np.arange(0,10)
# ax.step(x,x)    #where=(...)

#Стековый график
x=np.arange(-2,2,0.1)
# y1=np.array([-y**2 for y in x]) + 8
# y2=np.array([-y**2 for y in x]) + 8
# y3=np.array([-y**2 for y in x]) + 8
# ax.stackplot(x,y1,y2,y3)

#Stem график
# x=np.arange(-np.pi,np.pi,0.2)
# y=np.cos(x)
# ax.stem(x,y,"--r",bottom=0.3)

#Scatter график
x=np.random.normal(0,2,100)
y=np.random.normal(0,2,100)
ax.scatter(x,y,s=50,c="g",linewidth=1,marker="s",edgecolors="r")

plt.grid()
plt.show()