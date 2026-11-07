import os

import requests as req

# Токен храним в переменной окружения, а не в коде:
# Linux/macOS: export WEEEK_TOKEN="ваш_токен"
# Windows (PowerShell): $env:WEEEK_TOKEN="ваш_токен"
TOKEN = os.environ.get("WEEEK_TOKEN", "")
if not TOKEN:
    print("WEEEK_TOKEN не задан: экспортируйте токен перед запуском запросов.")

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/json",
    "Content-Type": "application/json",
}

# POST запрос
# name_card = input("Введите название карточки: ")
# text = input("Введите текст карточки: ")
#
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
# response = req.post(url="https://api.weeek.net/public/v1/tm/tasks", headers=headers, json=payload)
# print(response.json())

# PUT запрос
#
# payload = {
#     "title": "Понедельник",
#     "priority": 2,
# }
#
# url = "https://api.weeek.net/public/v1/tm/tasks/11"
#
# response = req.put(url=url, headers=headers, json=payload)
# print(response.json())

# DELETE запрос
#
# response = req.delete(url="https://api.weeek.net/public/v1/tm/tasks/13", headers=headers)
# print(response.text)

# GET запрос
#
# payload = {
#     "day": "02.11.2026",
#     "projectId": 1,
#     "priority": 2,
#     "title": "Понедельник"
# }
# response = req.get(url="https://api.weeek.net/public/v1/tm/tasks", headers=headers, json=payload)
# print(response.json())
