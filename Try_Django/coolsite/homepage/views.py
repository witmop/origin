from django.shortcuts import render
from django.http import HttpResponse
import requests as req
from random import randint
# Create your views here.


def random_character():
    rand_id=randint(1,83)
    response = req.get(url = f"https://swapi.info/api/people/{rand_id}")
    data = response.json()
    return {"id":rand_id,"character_info":data}    


def main(request):
    result = random_character()
    context = {"id":result["id"],"character":result["character_info"] }
    return render(request,"main_page.html",context)
