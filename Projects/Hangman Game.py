from random import choice
word_list=["виселица"]                  # откуда брать загаданные слова
def display_hangman(tries:int)->str:    #рисует виселицу
    stages = { # финальное состояние: голова, торс, обе руки, обе ноги
        0:
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                1:
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                2:
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                3:
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                4:
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                5:
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                6:
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    }
    print(stages[tries])

def show_word_func(show_word:list)->str:
    print("".join(el for el in show_word)) # вывод загаданого слова по мере его разгадки 

def hangman_game(hidden_word:str)->str:

    show_word=["_"]*len(hidden_word) # изначально слово отображается ____
    tries=6
    flag_letter_match=False 
            # проверка на наличие загаданных букв в вводимом слове
    print("Начнём игру!")
    display_hangman(tries)
    show_word_func(show_word)

    while True:
        enter_word=input("Введите слово: ")

        for el in enter_word:
            if el in hidden_word:
                flag_letter_match=True
                index=[ind for ind,letters in enumerate(hidden_word) if letters==el] # ищет индексы всех вхождений совпавшей буквы в загаданном слове
                for swap in index:
                    show_word[swap]=el

        if show_word.count("_")==0:             # проверка отгадано ли слово
            print("Вы выиграли!")
            break

        if flag_letter_match:               # если буквы совпали в загаданном слове, то ничего, иначе попытки -1
            flag_letter_match=False
        else:
            tries-=1
            print("Совпадений нет ")

        if tries==0:                        #проверка есть ли ещё попытки
            display_hangman(tries)
            print("Вы проиграли")
            print(f"Загаданное слово: {hidden_word}")
            break
        display_hangman(tries)
        show_word_func(show_word)

hangman_game(choice(word_list))
        