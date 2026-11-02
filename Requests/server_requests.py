import requests as req

#POST запрос
# name_card=input("Введите название карточки: ")
# text=input("Введите текст карточки: ")

# payload = {
#     "title": name_card,
#     "description": text,
#     "day": "04.11.2026",
#     "locations": [
#         {
#             "projectId": 1,
#             "boardColumnId": 3
#         }
#     ],
# }
# response=req.post(url = "https://api.weeek.net/public/v1/tm/tasks",headers={"Authorization": "Bearer dece718c-62c6-4402-b0aa-46ab96b48515","Accept":"application/json","Content-Type":"application/json"},json=payload)
# print(response.json())

#PUT запрос

# payload = {
#     "title": "Понедельник",
#     "priority": 2,
# }

# url="https://api.weeek.net/public/v1/tm/tasks/11"

# response=req.put(url=url,headers={"Authorization": "Bearer dece718c-62c6-4402-b0aa-46ab96b48515","Accept":"application/json","Content-Type":"application/json"},json=payload)
# print(response.json())

#DELETE запрос

# response=req.delete(url="https://api.weeek.net/public/v1/tm/tasks/13",headers={"Authorization": "Bearer dece718c-62c6-4402-b0aa-46ab96b48515","Accept":"application/json"})
# print(response.text)

#GET запрос
# payload={
#     "day":"02.11.2026",
#     "projectId":1,
#     "priority":2,
#     "title":"Понедельник"
# }
# response=req.get(url="https://api.weeek.net/public/v1/tm/tasks",headers={"Authorization": "Bearer dece718c-62c6-4402-b0aa-46ab96b48515","Accept":"application/json"},json=payload)
# print(response.json())