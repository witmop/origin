from django.shortcuts import render
from django.http import HttpResponse
import requests as req
from random import randint
# Create your views here.

def random_character():
    """Функция выбирает случайных персонажей и делай запрос по API для получения информации о героя"""
    
    result=[]
    temp = set()    #Нужно чтобы карточки персонажей не повторялись на странице
    for i in range(12):
        rand_id=randint(1,83)   #Всего 83 персонажей есть на swapi.info
        if rand_id in temp or rand_id == 17:    #На swapi.info нет карточки 17 персонажа
            while rand_id in temp or rand_id==17:
                rand_id=randint(1,83)
        
        response = req.get(url = f"https://swapi.info/api/people/{rand_id}")
        data = response.json()
        data["id"] = rand_id    #При получении json файла с данными о персонаже там нет его id , добавляем его сами
        result.append(data)
        temp.add(rand_id)
    return result

def main(request):
    result = random_character()
    context = {"characters":result}
    return render(request,"main_page.html",context)
