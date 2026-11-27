import requests as req
from random import randint
for id in range(18,84):
    response = req.get(url = f"https://akabab.github.io/starwars-api/api/id/{id}.json")
    data = response.json()
    image_url = data["image"]
    image_data = req.get(image_url).content
    with open(f"{id}.jpg","wb+") as file:
        file.write(image_data)
