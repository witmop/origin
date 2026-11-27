import requests as req
for id in range(1,84):
    """Функция автоматически загужает фото персонаей с сайта akabab.github.io (делая запрос по API)"""
    
    if id!=17:  #На сайте нет персонажа с id == 17
        response = req.get(url = f"https://akabab.github.io/starwars-api/api/id/{id}.json")
        data = response.json()
        image_url = data["image"]
        image_data = req.get(image_url).content
        with open(f"{id}.jpg","wb+") as file:    #Сохраняем файл в формате {id персонажа}.jpg
            file.write(image_data)
