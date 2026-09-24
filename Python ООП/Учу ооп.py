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



class Point:
    def __init__(self,x=0,y=0):
        self.__x=self.__y=0
        if self.check_value(x) and self.check_value(y):
            self.__x=x
            self.__y=y
    # @private #чтобы сделать метод приватным(более защищённым) для дурачков,кто вызывает pt._Point__x
    @classmethod
    def check_value(cls,x):
        return type(x) in (int,float)
    def set_coord(self,x,y):
        if self.check_value(x) and self.check_value(y):
            self.__x=x
            self.__y=y
        else:
            raise ValueError ("Координаты должны быть числами")
    def get_coord(self):
        return self.__x,self.__y
pt=Point(1,2)
pt.set_coord(10,20)
print(pt.check_value(5))
#_ одно нижнее подчёркивание лишь предостерегает, не запрещает (внутрення служебная переменная)
#__ можно обращаться только внутри класса print(pt.__y,py.__x) не будет работать
