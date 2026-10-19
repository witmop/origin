# Игра рыцарь и дракон
import random as rand
from time import sleep
class Knight:
    def __init__(self,health:int=200,armor:int=100,name:str="Рыцарь"):
        self._health=health
        self._armor=armor
        self.name=name

    def get_health(self):
        print(f"Ваше здоровье: {self._health}")

    def get_armor(self):
        print(f"Ваша броня: {self._armor}")

    def _deal_damage(self,sword,dragon):
        sword.check_durability()
        damage=rand.randint(sword.damage-10,sword.damage+10)
        dragon._health-=damage
        print(f"Вы нанесли дракону {damage} урона.")

class Dragon:
    def __init__(self,damage:int=25):
        self._health=rand.randint(275,325)
        self._damage=damage

    def _deal_damage(self,player):
        damage=rand.randint(self._damage-10,self._damage+10)
        if player._armor>0:
            if (player._armor-damage*0.9)<0:
                player._armor=0
                print("Дракон сломал вашу броню")

            else:
                player._armor-=int(damage*0.9)
                print(f"Дракон наносит {int(damage*0.9)} урона")

        else:
            player._health-=damage
            print(f"Дракон наносит {damage} урона")

    def get_health(self):
        print(f"Здоровье дракона {self._health}")

class Sword:
    def __init__(self):
        self.damage=25
        self.durability=8

    def check_durability(self):
        if self.durability<=0:
            self.damage=15
            print("Меч сломан, урон ниже обычного")
        else:
            self.durability-=1
            print(f"У вашего меча осталось {self.durability} прочности")

    def info_sword(self):
        print(f"У вашего меча {self.damage} урона и {self.durability} прочности")


def fight(player,sword,dragon):
    print("У тебя начинается бой с драконом.\
          Дракон нападает первым, но ты успеваешь уклониться и нанести первый удар")
    sleep(3)
    player._deal_damage(sword,dragon)
    sleep(3)
    print("Дракон разворачивается и у вас начинается бой.")

    while True:
        print("Удар дракона")
        dragon._deal_damage(player)
        sleep(3)

        if player._health<=0:
            print("Дракон победил тебя")
            break
        player.get_armor()
        player.get_health()
        print("Ваш удар")
        sleep(5)
        player._deal_damage(sword,dragon)

        if dragon._health<=0:
            print(f"{player.name} победил дракона!")
            break
        dragon.get_health()
        sleep(5)

player1=Knight()
sword1=Sword()
dragon1=Dragon()

print("Добро пожаловать рыцарь как тебя зовут?")
player1.name=input()

print("Перед тобой 3 дороги, реши куда ты пойдёшь?(Введите 1, 2 или 3) ")
road=int(input())

if road==1:
    print("Дорога кажется запутанной, на пути ты видишь камень, а рядом с камнем роскошный меч.\
          Возможно его кто-то оставил здесь специально для тебя. Или это ловушка!")
    choise=input("Подобрать меч? (да/нет) ").lower()

    if choise=="да":
        print("Ты подобрал новый меч, ничего страшного не случилось.\
                Старый меч тебе больше не нужен и ты его выбрасываешь.")
        sword1.damage+=20
        sword1.info_sword()
        sleep(5)
        print("Ты идёшь дальше и вдруг на горе видишь золотого дракона, он заметил тебя и уже летит в твою сторону")
        
    else:
        print("Ты пропускаешь меч и идёшь дальше.\
              Вдруг на горе ты видишь золотого дракона, кажется он тоже замети тебя и уже летит в твою сторону")
    fight(player1,sword1,dragon1)

elif road==2:
    print("Вы идёте через тёмный-тёмный лес.\
          Вдруг слышите чей-то плачь")
    sleep(5)
    print("Вы продвигаетесь по нарпалвнию к плачу, вдруг лес заканчивается и перед вами поляна сирени.\
          На поляне вы видите девушка. Она тоже вас заметила...")
    sleep(7)
    print("Девушка с заплаканными глазами подходит к вам. Она берёт вас за руку и ведёт в даль...")

else:
    print("Вы идёте по тропинке. Видно что по этой дорога протоптана до вас\
          Вдруг вы видете чей-то скелет...")
    sleep(2)
    print("Поднимаете голову и видете золотого дракона...")
    sleep(2)
    fight(player1,sword1,dragon1)