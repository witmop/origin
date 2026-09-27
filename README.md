<div align="center">

# 🧠 Учебный репозиторий

**Мой учебный репозиторий** — место, где я разбираю Python по частям:
задачи, ООП, работа с данными и алгоритмы.

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![pandas](https://img.shields.io/badge/pandas-2.x-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Последний коммит](https://img.shields.io/github/last-commit/witmop/origin?style=for-the-badge&logo=github&logoColor=white)](https://github.com/witmop/origin/commits)
[![Контрибьюторы](https://img.shields.io/github/contributors/witmop/origin?style=for-the-badge&logo=github&logoColor=white)](https://github.com/witmop/origin/graphs/contributors)

</div>

---

## 📌 О проекте

Репозиторий создан, чтобы не терять всё написанное в стол, а вести учебный дневник в Git.
Здесь лежат конспекты и рабочие файлы: часть задач закомментирована и используется как
шпаргалка, часть — запускается как есть.

**Принцип:** сначала разобраться и заставить код работать, потом причесать.
Поэтому в файлах много комментариев с объяснением «почему так, а не иначе» — это заметки
для себя, а не готовый production-код.

## 🗂 Что внутри

| Файл | Что внутри |
|:--|:--|
| `Numpy/numpy-100.py` | Решения задач из набора [100 NumPy Exercises](https://github.com/rougier/numpy-100). Индексированные массивы, `reshape`, срезы, Broadcasting, `datetime64`, `random`, матричная арифметика, генераторы. |
| `Projects/tic-tac-toe.py` | Игра в консоли: поле 3×3 на NumPy-массиве, ход игрока с валидацией ввода, ход «компьютера», проверка победы по строкам, столбцам и диагоналям. |
| `Python ООП/Учу ооп.py` | Атрибуты класса и экземпляра, `__dict__`, `getattr` / `setattr` / `hasattr`, `__doc__`, методы и `self`, `__new__` / `__init__` / `__del__`, паттерн Singleton, `@classmethod` / `@staticmethod`, инкапсуляция, валидация значений. |
| `Try_Pandas/Учу pandas.py` | Чтение CSV, деление колонок на числовые и категориальные, фильтрация и очистка выбросов, стандартизация и нормализация, `value_counts`, объединение редких категорий, кодирование через `.cat.codes` и `get_dummies`, новые признаки (`Age`, `km_year`). |
| `leetcode/28. ...py` | Задача [28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) — поиск первого вхождения подстроки. |
| `hello.html` + `style.css` | Первая HTML-страница: минимум разметки, чтобы не забыть, как это выглядит. |

## 🚀 Как запустить

Нужен Python 3.10+.

```bash
# 1. Клонировать репозиторий
git clone https://github.com/witmop/origin.git
cd origin

# 2. Создать виртуальное окружение
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate

# 3. Установить зависимости
pip install numpy pandas seaborn matplotlib accessify
