import requests as req
import json
TOKEN="set your token"
class Student:
    def __init__(self, first_name:str, second_name:str, password:int) -> None:
        self.first_name = first_name
        self.second_name = second_name
        self.__pass= password
        self._headers = {
            "Authorization": f"Bearer ",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    def __check_pass(self,password:int) -> bool:
        return self.__pass == password

    def set_token(self, token:str, password:int) -> None:
        if self.__check_pass(password):
                self._headers = {"Authorization": f"Bearer {token}",
                                 "Accept": "application/json",
                                 "Content-Type": "application/json",}
                print("Токен установлен")
        else:
            print("Пароль неверный")

    def change_name(self, name:str, password:int) -> None:
        if self.__check_pass(password):
            self.first_name=name
            print("Ваше имя было изменено")
        else:
            print("Неверный пароль")

    def check_schedule(self, date:str, lesson_name:str) -> None:
        payload = {"day": date,"projectId": 1,"priority": 2,"title": lesson_name}
        response = req.get(url = "https://api.weeek.net/public/v1/tm/tasks",headers =self._headers,json = payload)
        data=response.json()
        print(f"Название урока: {data["tasks"][0]["title"]}")  
        print(f"Комментарий к уроку: {data["tasks"][0]["description"]}") 
        # print(data)

    def info(self, password:int) -> None:
        if self.__check_pass(password):
            print(f"Ваше имя: {self.first_name}, фамилия: {self.second_name}.")
        else:
            print("Неверный пароль")

class Teacher(Student):
    def create_lesson(self,date:str, lesson_name:str, lesson_description:str) -> None:
        payload = {
        "title": lesson_name,
        "description": lesson_description,
        "day": date,
        "locations": [
            {
                "projectId": 1,
                "boardColumnId": 3
            }
        ],
        }
        response = req.post(url = "https://api.weeek.net/public/v1/tm/tasks", headers = self._headers,json = payload)
        # print(response.text)
        print("Урок успешно создан")

    def update_lesson(self, lesson_id:int, new_lesson_name:str, new_lesson_description:str) -> None:
        payload = {
        "title": new_lesson_name,
        "priority": 2,
        "description": new_lesson_description
        }
        url = f"https://api.weeek.net/public/v1/tm/tasks/{lesson_id}"
        response = req.put(url = url,headers = self._headers,json = payload)
        print("Данные об уроке были изменены")

    def delete_lesson(self, lesson_id:int) -> None: 
        url = f"https://api.weeek.net/public/v1/tm/tasks/{lesson_id}"
        response=req.delete(url = url, headers=self._headers)
stud = Student("Иван", "Иванов", 1234)
tech = Teacher("Василий", "Победоносный", 1000)
stud.set_token(TOKEN, 9999)
stud.set_token(TOKEN, 1234)
stud.change_name("Виталий", 1234)
stud.info(1234)

stud.check_schedule("16.11.2026", "Программирование")
tech.set_token(TOKEN, 1000)
tech.create_lesson("18.11.2026","Programming", "to come at one’s own discretion")
tech.update_lesson(10, "Math", "Test")

