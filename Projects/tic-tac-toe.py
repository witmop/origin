from numpy import full,diag,fliplr,array
from random import choice
from random import randint
from time import sleep
# ❌⭕⬜
game_field=full((3,3),"⬜",dtype=str)
def show_field(game_field=game_field):
    for row in game_field:
        print(*row)
def ask_for_game(replay=False):
    welcome_list=["Здравствуйте! Не желаете ли сыграть?","Доброго времени суток! Хотите поиграть?","Привет! Как насчет игры?"]
    replay_list=["Сыграем еще разок?","Хотите еще сыграть?","Желаете еще раз?"]
    if not(replay):
        print(choice(welcome_list))
        answer=input("Введите Да/Нет ").lower()
        return answer
    else:
        print(choice(replay_list))
        answer=input("Введите Да/Нет ").lower()
        return answer
def who_goes_first():
    #0-человек
    #1-робот
    return randint(0,1)

def get_user_input(game_field=game_field):
    print("Введите номер столбца и ряда через пробел.")
    vvod=list(map(str,input().split()))
    suitable=False
    temp=[]
    while not(suitable):
        try:
            int(vvod[0])
            int(vvod[1])
            suitable=True
        except:
            ValueError
            print("Неккоректный ввод, повторите попытку.")
            suitable=False
            vvod=list(map(str,input().split()))
        if suitable==True:
            if not(1<=int(vvod[0])<=3) or not(1<=int(vvod[1])<=3):
                suitable=False
                print("Введите числа от 1 до 3")
                vvod=list(map(str,input().split()))
        if game_field[int(vvod[1])-1,int(vvod[0])-1]!="⬜":
            print("Эта клетка уже занята ")
            suitable=False
            vvod=list(map(str,input().split()))        
    temp.append(int(vvod[1])-1)
    temp.append(int(vvod[0])-1)
    result=tuple(map(int,temp))
    return result

def get_computer_move(game_field=game_field):
    a,b=randint(0,2),randint(0,2)
    sleep(2)
    while game_field[a,b]!="⬜":
        a,b=randint(0,2),randint(0,2)
    result=(a,b)
    return result

def check_result(game_field=game_field):
    diagonal=diag(game_field)
    antidiag=diag(fliplr(game_field))
    if (diagonal=="⭕").sum()==3:
        print("Победили нолики")
        return True
    elif (diagonal=="❌").sum()==3:
        print("Победили крестики")
        return True
    if (antidiag=="⭕").sum()==3:
        print("Победили нолики")
        return True
    elif (antidiag=="❌").sum()==3:
        print("Победили крестики")
        return True
    for row in game_field:
        if (row=="❌").sum()==3:
            print("Победили крестики")
            return True
        elif (row=="⭕").sum()==3:
            print("Победили нолики")
            return True
    for col in range(game_field.shape[1]):
        column=game_field[:,col]
        if (column=="⭕").sum()==3:
            print("Победили нолики")
            return True
        elif (column=="❌").sum()==3:
            print("Победили крестики")
            return True
    return False
def two_player():
    vvod=input("Вы будете играть с роботом? Введите Да/Нет ").lower()
    if vvod=="да":return False
    elif vvod=="нет":return True
    else:return None


def main_game(replay=False):
    if ask_for_game(replay)=="да":
        answer=two_player()
        if answer==False:
            if who_goes_first()==0:
                print("Вы ходите первым")
                show_field()
                game_field[get_user_input()]="❌"
                show_field()
                count=1
                while check_result()==False or count<9:
                    print("Ход компьютера...")
                    sleep(2)
                    game_field[get_computer_move()]="⭕"
                    count+=1
                    show_field()
                    if count==9:
                        print("Ничья")
                        break
                    if check_result():break
                    print("Ваш ход")
                    game_field[get_user_input()]="❌"
                    show_field()
                    if check_result():break
                    count+=1
                    if count==9:
                        print("Ничья")
                        break
            elif who_goes_first()==1:
                show_field()
                print('Первым ходит компьютер')
                sleep(2)
                game_field[get_computer_move()]="❌"
                show_field()
                count=1
                while check_result()==False or count<9:
                        game_field[get_user_input()]="⭕"
                        show_field()
                        if check_result():break
                        count+=1
                        if count==9:
                            print("Ничья")
                            break
                        print("Ход компьютера...")
                        sleep(2)
                        game_field[get_computer_move()]="❌"
                        count+=1
                        show_field()
                        if count==9:
                            print("Ничья")
                            break
                        if check_result():break
        elif answer==True:
            count=0
            while check_result==False or count <9:
                print("Ходит первый игрок ")
                show_field()
                game_field[get_user_input()]="❌"
                show_field()
                count+=1
                if count==9:
                    print("Ничья")
                    break
                if check_result():break
                print("Ходит второй игрок ")
                game_field[get_user_input()]="⭕"
                show_field()
                if check_result():break
                count+=1
                if count==9:
                    print("Ничья")
                    break
main_game()