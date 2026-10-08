from string import ascii_letters
from accessify import private,protected
# class Point:
#     color="red" #атрибуты или св-ва класса
#     circle=2
# Point.color="black"
# print(Point.color)
# print(Point.__dict__) #вывод все атрибуты класса

# a=Point()#объект сам по себе сейчас не содержит никаких атрибутов, только общие атрибуты класса Point 
# print(type(a)) # type(a)==Point вывод True, isinstance(a,Point) вывод True

# Point.circle=1 # данный меняются везде в каждом объекте, то есть в а теперь circle тоже равен 1

# a.color="green"# теперь у а есть свой атрибут color==green

# Point.type_pt="disc" #св-во появится у всех
# setattr(Point,"prop",1)# то же самое что и Point.prop=1

# res=Point.prop# присвоить значение атрибута переменной
# print(getattr(Point,"a",False))# если атрибута нет, то будет возвращаться False

# del Point.type_pt
# hasattr(Point,"type_pt")# проверяет существует ли объект в классе
# hasattr(a,"circle") #выводит True хотя сам атрибут circle не лежит в a, он есть в Point
# # del a.circle ошибка так как атрибут circle лежит не в a,а в Point в а лежит только color=green (строка 13)
# del a.color # теперь в а удаляется собсвенный атрибут color=green и color=black(строка 4) как в Point



# class Point:
#     "Класс для представления координат точек на плоскости"#Point.__doc__ описание класса
#     circle=2
#     color="red"
# a=Point()
# b=Point()
# a.x=1
# a.y=2
# b.x=10
# b.y=20
# print(Point.__dict__)


# class Point:
#     circle=2
#     color="red"
#     def set_coords():
#         print("вызов метода set_coords")
# Point.set_coords()
# pt=Point()
# pt.set_coords() #возникает ошибка так как питон автоматически посылает в функцию set_coords() 1 аргумент self-которая является ссылкой на объект pt это происходит всегда


# class Point:
#     circle=2
#     color="red"
#     def set_coords(self,x,y):#в экземляре класса, то есть pt создаём 2 локальных св-ва x и y (self - ссылка на экземпляр )
#         self.x=x
#         self.y=y
#     def get_coords(self):
#         return (self.x,self.y)
# #self нужен чтобы работать с локальными атрибутами экземлпяров класса
# pt=Point()
# pt2=Point()
# # Point.set_coords() #возникает ошибка так как ссылки на объект нет и в self ничего автоматическ не подставляется 
# pt.set_coords(1,2) # указывать значение self не нужно или Point.set_coords(pt,1,2) 
# print(pt.get_coords())#возвращает значение координат если x,y нет, то ошибка
# # print(hasattr(pt,"x")) что-бы не было ошибки монжо выполнить проверку на наличие атрибутов 
# # print(hasattr(pt,"y"))


# class Point:
#     circle=2
#     color="red"
#     def __init__(self,a=0,b=0):
#         print("вызов __init__")
#         self.x=a
#         self.y=b
#     def __del__(self):#например если pt=Point(), а потом pt=0 то в момент pt=0 будет выполнена функция __del__ финализатор и объект будет удалён(экземпляр класса)
#         print("Удаление экземпляра" +str(self))
#     def set_coords(self,x,y):
#         self.x=x
#         self.y=y
#     def get_coords(self):
#         return (self.x,self.y)
# pt=Point(1) #что происходит в этот момент
# #1 шаг создание объекта метод __new__
# #2 шаг инициализация объекта метод __init__ то есть функция __init__ выполняется сразу после созднания экземпляра класса и в нашем случае она задаёт значения x и y экземпляру
# print(pt.__dict__)


# class Point:
#     def __new__(cls,*args,**kwargs):# cls ссылается на класс Point значения args и kwargs передаём чтобы не было ошибка при создании экземпляра __new__(cls,*args,**kwargs) общий синтаксис
#         print("вызов __new__ для "+str(cls))
#         return super().__new__(cls)# все классы в питон начиная с 3 наследуются от базового класса object когда вызываем super() получаем ссылку на этот базовый класс и уже в нём вызываем наш Point
#     def __init__(self,x=0,y=0):# self ссылается на создаваемый экземпляр класса
#         print("вызов __init__ для "+str(self))
#         self.x=x
#         self.y=y
# pt=Point(1,2)
# print(pt.__dict__)

#Паттерн проектирования Singleton (когда у класса может быть только 1 экземлпяр)
# class Database:
#     __instance=None
#     def __new__(cls,*args,**kwargs):#cls здесь это как ссылка на класс Database
#         if cls.__instance is None:# проверка есть ли экземпляры
#             cls.__instance=super().__new__(cls)# если нет, то создаём новый
#         return cls.__instance#иначе ссылаемся на существующий
#     def __del__(self):
#         Database.__instance=None
#     def __init__(self,user,psw,port):
#         self.user=user
#         self.psw=psw
#         self.port=port
#     def connect(self):
#         print(f"Db connect: {self.user},{self.psw}.{self.port}")
#     def close(self):
#         print("Close Db")
#     def read(self):
#         return "Db data"
#     def write(self,data):
#         print(f"Write Db {data}")
# db=Database("root","1234",80)
# db2=Database("root2","5678",40)# на самом деле объект не был создан, ссылается на db но данные берутся из db2 root2 5678 40
# print(id(db),id(db2))


# class Vector:
#     min_coord=0
#     max_coord=100
#     @classmethod
#     def validate(cls,arg):# метод класса работает только с атрибумати самого класса, не может обращаться к атрибутам экземпляров
#         return cls.min_coord<=arg<=cls.max_coord
#     def __init__(self,x,y):
#         self.x=self.y=0
#         if self.validate(x) and self.validate(y):#проверка значений x и y
#             self.y=y
#             self.x=x
#         print(Vector.norm2(self.x,self.y))
#     def get_coord(self):
#         return self.x,self.y
#     @staticmethod #функция не обращается не к самому классу не к его экземлярам
#     def norm2(x,y):# нет скрытых параметров
#         return x*x +y*y
# v=Vector(10,2)
# print(Vector.norm2(5,3))
#  __init__ и get_coord() имеют доступ к атрибутам внутри класса, и к переменнам самих экземпляров
# @classmethod работает только с атрибутами класса(в функция вместо self, cls)
# @staticmethod не обращается ни к каким атрибутам



# class Point:
#     def __init__(self,x=0,y=0):
#         self.__x=self.__y=0
#         if self.__check_value(x) and self.__check_value(y):
#             self.__x=x
#             self.__y=y
#     @private #чтобы сделать метод приватным(более защищённым по сравнению с __) для дурачков,кто вызывает pt._Point__check_value()
#     @classmethod
#     def __check_value(cls,x):
#         return type(x) in (int,float)
#     def set_coord(self,x,y):
#         if self.__check_value(x) and self.__check_value(y):
#             self.__x=x
#             self.__y=y
#         else:
#             raise ValueError ("Координаты должны быть числами")
#     def get_coord(self):
#         return self.__x,self.__y
# pt=Point(1,2)
# pt.set_coord(10,20)
# print(pt.check_value(5))
# #_ одно нижнее подчёркивание лишь предостерегает, не запрещает (внутрення служебная переменная)
# #__ можно обращаться только внутри класса print(pt.__y,py.__x) не будет работать


# class Point:
#     max_coord=100
#     min_coord=0

#     def __init__(self,x,y):
#         self.x=x
#         self.y=y

#     def set_coord(self,x,y):
#         self.x=x
#         self.y=y

#     def __getattribute__(self, item): #вызывается при обращении к атрибутам через экземпляры классов
#         if item == "x":
#             raise ValueError("доступ запрещён")
#         else:
#             return object.__getattribute__(self,item)

#     def __setattr__(self, name, value):#вызывает при присваивании атрибутов экземпляру класса
#         if name=="z":
#             raise AttributeError("Недопустимое имя атрибута")
#         else:
#             print("__setattr__")
#             object.__setattr__(self,name,value)
#             # self.x=value функция зациклиться
#             # self.__dict__[name]=value можно и так, но object лучше
    
#     def __getattr__(self, name): # при обращении к несуществуещему атрибуту будет вызываться (чтобы не было ошибки)
#         return False

#     def __delattr__(self, name):#вызывается при удалении атрибута
#         print("dellattr")
#         object.__delattr__(self,name)
    
# pt1=Point(1,2)
# pt1.y=5
# del pt1.x
# print(pt1.__dict__)
# # print(pt1.z)


# Моносотояние

# class ThreadData:
#     __shared_attrs={"name":"thread_1","data":{},"id":1}

#     def __init__(self):
#         self.__dict__ = self.__shared_attrs #при создании нового объекта класса его коллекция дикт будет ссылаться на __shared_attrs

# th1=ThreadData()
# th2=ThreadData()
# th2.id=3 #меняется у всех экземпляров класса
# th1.atter_new="new_attr"#добавляется всем экземплярам класса


#Атрибут свойства property
# class Person:
#     def __init__(self,name,old):
#         self.__name=name
#         self.__old=old
#     @property #обязательно сначала getter
#     def old(self): #раньше была get_old
#         return self.__old
#     @old.setter #из название верхней фукнции
#     def old(self,old):#раньше была set_old
#         self.__old=old
#                             # теперь можно убрать old=property() и также обращаться p.old=35

#     @old.deleter
#     def old(self):      #так как property можно просто писать del p.old
#         del self.__old      
#     # old=property()# порядок обязателен
#     # old=old.setter(set_old)
#     # old=old.getter(get_old)
#     #a=p.old будет автоматически вызываться get_old
#     #print(a)

#     #p.old=35 будет автоматически вызываться set_old


# p=Person("Сергей",20)
# # p.set_old(35)
# p.__dict__["old"]="old in object p"
# a=p.old
# p.old=35 #приоритет выше чем у приватного old
# a=p.old
# print(a)
# print(p.__dict__)


# class Person:
#     S_RUS="абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
#     S_RUS_UPPER="абвгдеёжзийклмнопрстуфхцчшщъыьэюя".upper()
#     def __init__(self,fio,old,ps,weight):
#         self.verify_fio(fio)
#         # self.verify_old(old)      можно убрать так как мы прописали через property
#         # self.verify_ps(ps)
#         # self.verify_weight(weight)

#         self.__fio=fio.split()
#         self.old=old            #было self.__old=old , изменили так как сделали привязку через property
#         self.passport=ps
#         self.weight=weight

#     @classmethod
#     def verify_fio(cls,fio):
#         if type(fio)!=str:
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()
#         if len(f)!=3:
#             raise TypeError("Неверный формат записи")

#         letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
#         for s in f:
#             if len(s)<1:
#                 raise TypeError("В ФИО хотя бы 1 символ")
#             if len(s.strip(letters))!=0:
#                 raise TypeError("В ФИО должны быть только буквенные символы и дефис")
#     @classmethod
#     def verify_old(cls,old):
#         if type(old)!= int or old <14 or old>120:
#             raise TypeError("Возраст должен быть целым числом в диапазоне [14;120]")
        
#     @classmethod
#     def verify_weight(cls,w):
#         if type(w)!=float or w<20:
#             raise TypeError("Вес должен быть вещественным числом от 20 и выше") 

#     @classmethod
#     def verify_ps(cls,ps):
#         if type(ps)!=str:
#             raise TypeError("Паспорт должен быть строкой")
        
#         s=ps.split()
#         if len(s)!=2 or len(s[0])!=4 or len(s[1])!=6:
#             raise TypeError("Неверный формат паспорта")

#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Сериян и номер паспорта должны быть числами")

#     @property
#     def fio(self):
#         return self.__fio

#     @property
#     def old(self):
#         return self.__old

#     @old.setter
#     def old(self,old):
#         self.verify_old(old)
#         self.__old=old

#     @property
#     def weight(self):
#         return self.__weight

#     @weight.setter
#     def weight(self,weight):
#         self.verify_weight(weight)
#         self.__weight=weight
    
#     @property
#     def passport(self):
#         return self.__passport

#     @passport.setter
#     def passport(self,ps):
#         self.verify_ps(ps)
#         self.__passport=ps
# p=Person("Иван Иванович Иванов",30,"1234 567890",80.0)
# p.old=100
# p.passport="4567 123456"
# p.weight= 70.3
# print(p.__dict__)


#Дескриптор данных
# class Integer:
#     @classmethod
#     def verify_coord(cls,coord):
#         if type(coord)!=int:
#             raise TypeError("Координата должна быть целым числом")

#     def __set_name__(self,owner,name):
#         self.name="_"+name

#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]#или getattr(instance,self.name)

#     def __set__(self, instance, value):
#         self.verify_coord(value)
#         print(f"__set__: {self.name} = {value}")
#         instance.__dict__[self.name] = value#или setattr(instance,self.name)
        
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()

#     def __init__(self,x,y,z):
#         self.x = x
#         self.y = y
#         self.z = z
    
# p=Point3D(1,2,3)
# print(p.__dict__)


# Dunder-методы (double underscope)

# class Cat:
#     def __init__(self,name):
#         self.name=name

#     def __repr__(self):
#         return f"{self.__class__}: {self.name}" #менят вывод при написании print(cat1) или str(cat1) если нет метода __str__()

#     def __str__(self):
#         return f"{self.name}"       # менят вывод при написании print(cat1) или str(cat1)

# # cat1=Cat("Васька")
# # print(cat1)

# class Point:
#     def __init__(self,*args):
#         self.__cords=args

#     def __len__(self):          # позволяет применять к объектам класса метод len
#         return len(self.__cords)

#     def __abs__(self):
#         return list(map(abs,self.__cords))          # позволяет применять к объектам класса метод abs

# p1=Point(1,-2)
# print(len(p1))
# print(abs(p1))


# class Clock:
#     __DAY=86400         #Число секунд в одном дне

#     def __init__(self,seconds:int):
#         if not isinstance(seconds,int):
#             raise TypeError("Секунды должны быть целым числом")

#         self.seconds=seconds%self.__DAY

#     def get_time(self):
#         s = self.seconds %60
#         m = (self.seconds //60)%60
#         h = (self.seconds//3600)% 24

#         return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

#     @classmethod
#     def __get_formatted(cls,x):
#         return str(x).rjust(2,"0")

#     def __add__(self, other):               #теперь можно писать с1=с1+100, а не c1=c1.seconds + 100
#         if not(isinstance(other,(int,Clock))):
#             raise ArithmeticError("Правый операнд должен быть int или Clock")

#         sc=other                      
#         if isinstance(other,Clock):     # теперь можно писать с1+с2
#             sc=other.seconds

#         return Clock(self.seconds+sc)

#     def __radd__(self, other):          #теперь можно писать с1=100+с1
#         return self+other       # поменяли местами, будет вызывать __add__

#     def __iadd__(self, other):          #теперь с+=100 не создаёт новый экземпляр класса, без этого создавался именно новый экземпляр
#         print("__iadd___")
#         if not isinstance(other,(int,Clock)):
#             raise ArithmeticError("Правый операнд должен быть int или Clock")

#         sc=other                      
#         if isinstance(other,Clock): 
#             sc=other.seconds

#         self.seconds+=sc
#         return self

#     @classmethod
#     def __verify_data(cls,value):
#         if not(isinstance(value,(int,Clock))):
#             raise TypeError("Операнд справа должен быть int или Clock")

#         return value if isinstance(value,int) else value.seconds

#     def __eq__(self, value):    
#         sc=self.__verify_data(value)              # теперь можно сравнивать с1==с2 или с1==1000       с1!=с2, с1!=1200 также можно (python делает not(c1==c2))
#         return self.seconds == sc

#     def __lt__(self, value):
#         sc=self.__verify_data(value)              # теперь можно c1<c2          можно и с1>c2 (python делает c2<c1) или сделать самому __gt__ (>)
#         return self.seconds < sc

#     def __le__(self, value):                    # аналогично с __lt__ или же можно сделать отдельный метод __ge__ (>=)
#         sc=self.__verify_data(value)
#         return self.seconds <= sc

     
# c1=Clock(1000)
# c1+=100
# print(c1.get_time())



# ХЭШ

# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y

#     def __eq__(self, value):
#         return self.x==value.x and self.y ==value.y

#     def __hash__(self):
#         return hash((self.x,self.y))
# p1=Point(1,2)
# p2=Point(1,2)
# print(hash(p1),hash(p2),sep="\n")
# print(p1==p2)


# Метод __bool__

# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y

#     def __len__(self):          #если нет метода __bool__ то вызывается __len__
#         print("__len__")
#         return self.x * self.x + self.y* self.y

#     def __bool__(self):
#         print("__bool__")
#         return self.x==self.y
# p=Point(3,4)
# if p:           # применяется __bool__
#     print("True")
# else:
#     print("False")


# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=list(marks)

#     def __getitem__(self, key):     # теперь можно просто писать s1[2]
#         if 0<= key <=len(self.marks):
#             return self.marks[key]  
#         else:
#             raise IndexError("Неверный индекс")

#     def __setitem__(self, key, value):      #теперь можно s[1]=5
#         if not isinstance(key,int) or key<0:
#             raise TypeError("Индекс должнен быть целым неотрицательным числом")
        
#         if key>=len(self.marks):
#             off = key+1-len(self.marks)
#             self.marks.extend([None]*off)
#         self.marks[key]=value

#     def __delitem__(self, key):         #del s1[2]
#         if not isinstance(key,int) or key<0:
#             raise TypeError("Индекс должнен быть целым неотрицательным числом")

#         del self.marks[key]

# s1=Student("Сергей",[4,1,3,2])
# s1[10]=10
# del s1[2]
# print(s1.marks)


# class Frange:
#     def __init__(self,start=0.0,stop=0.0,step=1.0):
#         self.start=start
#         self.stop=stop
#         self.step=step

#     def __iter__(self):     # теперь можно for x in fr: (сначала получает итератор, потом через next перебирает значения)
#         self.value=self.start-self.step
#         return self
    
#     def __next__(self):
#         if self.value + self.step <self.stop:
#             self.value+=self.step
#             return self.value
#         else:
#             raise StopIteration

# class Frange2D:
#     def __init__(self,start=0.0,stop=0.0,step=1.0,rows=5):
#         self.rows=rows
#         self.fr= Frange(start,stop,step)
#         self.value=0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.value<self.rows:
#             self.value+=1
#             return iter(self.fr)
#         else:
#             raise StopIteration

# fr=Frange2D(0,2,0.5,4)
# # print(fr.__next__())
# # print(fr.__next__())
# # print(fr.__next__())
# for row in fr:
#     for x in row:
#         print(x,end=" ")
#     print()

# Наследование

# class Geom:         #Базовый класс
#     name="Geom"
#     def set_coords(self,x1,y1,x2,y2):       #Параметр self может ссылаться на объекты дочерних классов
#         self.x1=x1
#         self.x2=x2
#         self.y1=y1
#         self.y2=y2

#     def draw():
#         print("Рисование примитива")

# class Line(Geom):           #Дочерний класс
#     name = "Line"           #Переопределение атрибута
#     def draw(self):
#         print("Рисование линии")

# class Rect(Geom):           #Дочерний класс
#     pass

# g=Geom()
# l=Line()
# r=Rect()
# l.set_coords(1,1,2,2)
# print(l)



# class Geom:
#     pass

# class Line(Geom):
#     pass

# g=Geom()
# l=Line()
# print(l)
# print(issubclass(Line,Geom))        #сначала дочерний, потом родительский
# print(isinstance(l,Geom))


# class Vector(list):
#     def __str__(self):
#         return " ".join(map(str,self))



# class Geom:
#     name="Geom"
#     def __init__(self,x1,y1,x2,y2):
#         self.x1=x1
#         self.x2=x2
#         self.y1=y1
#         self.y2=y2

# class Line(Geom):
#     name="Line"             #переопределение overriding
    
#     def draw(self):         #расширение extended
#         print("Рисование линии")

# class Rect(Geom):
#     def __init__(self,x1,y1,x2,y2,fill=None):       #делегирование
#         super().__init__(x1,y1,x2,y2)           #супер вовращает ссылку на родительский класс в такому случае self писаь не нужно и 
#         self.fill=fill
#     name="Rect"            
    
#     def draw(self):         
#         print("Рисование прямоугольника")


# class Geom:
#     __name="Geom"
#     def __init__(self,x1,y1,x2,y2):
#         self._x1=x1
#         self._x2=x2
#         self._y1=y1
#         self._y2=y2

#     def __verify_coord(self,coord):     #можно вызывать только в Geom
#         return 0<= coord< 100

# class Rect(Geom):
#     def __init__(self, x1, y1, x2, y2,fill="red"):
#         super().__init__(x1, y1, x2, y2)
#         self._fill=fill
#     def get_coords(self):
#         return (self._x1,self._y1)

# r=Rect(0,0,10,20)
# print(r.__dict__)


# Полиморфизм
class Geom:
    def get_pr(self):
        raise NotImplementedError("В дочернем классе должен быть переопределён метод get_pr() ")
    
class Rectangle(Geom):
    def __init__(self,w,h):
        self.w=w
        self.h=h

    def get_pr(self):
        return 2*(self.w*self.h)

class Square(Geom):
    def __init__(self,a):
        self.a=a

    def get_pr(self):
        return 4*self.a

class Triangle(Geom):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    # def get_pr(self):
    #     return self.a+self.b+self.c

r1=Rectangle(1,2)
r2=Rectangle(3,4)
s1=Square(10)
s2=Square(20)
t1=Triangle(1,2,3)
t2=Triangle(4,5,6)
geom=[r1,r2,s1,s2,t1,t2]
for el in geom:
    print(el.get_pr())