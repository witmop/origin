from django.shortcuts import render
from django.http import HttpResponse
import requests as req
from random import randint
# Create your views here.

def random_character():
    result=[]
    temp = set()
    for i in range(12):
        rand_id=randint(1,83)
        if rand_id in temp or rand_id == 17:
            while rand_id in temp or rand_id==17:
                rand_id=randint(1,83)
        
        response = req.get(url = f"https://swapi.info/api/people/{rand_id}")
        data = response.json()
        data["id"] = rand_id
        result.append(data)
        temp.add(rand_id)
    return result

def main(request):
    result = random_character()
    context = {"characters":result}
    return render(request,"main_page.html",context)
