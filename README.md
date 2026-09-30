<div align="center">

# 🧠 Учебный репозиторий

**Мой учебный репозиторий** — место, где я разбираю Python по частям:
задачи, ООП, работа с данными, алгоритмы и консольные проекты.

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![pandas](https://img.shields.io/badge/pandas-2.x-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Последний коммит](https://img.shields.io/github/last-commit/witmop/origin?style=for-the-badge&logo=github&logoColor=white)](https://github.com/witmop/origin/commits)
[![Контрибьюторы](https://img.shields.io/github/contributors/witmop/origin?style=for-the-badge&logo=github&logoColor=white)](https://github.com/witmop/origin/graphs/contributors)

</div>

---

## 📌 О проекте

Репозиторий создан, чтобы не терять всё написанное в стол, а вести учебный дневник в Git.
Здесь лежат конспекты, решённые задачи и небольшие консольные программы: часть кода
закомментирована и служит шпаргалкой, часть запускается как есть.

**Принцип:** сначала разобраться и заставить код работать, потом причесать.
Поэтому в файлах много комментариев с объяснением «почему так, а не иначе» — это заметки
для себя, а не готовый production-код.

## 📁 Структура

```
├── Numpy/                # задачи на NumPy
├── Projects/             # консольные программы
├── Python ООП/           # конспект по объектно-ориентированному Python
├── Try_Pandas/           # работа с табличными данными
├── leetcode/             # решённые задачи LeetCode
├── hello.html + style.css
└── .gitignore
```

## 🗂 Что внутри

### Консольные проекты — `Projects/`

| Файл | Что внутри |
|:--|:--|
| `tic-tac-toe.py` | Крестики-нолики в консоли: поле 3×3 на NumPy-массиве, ход игрока с валидацией ввода, ход «компьютера», проверка победы по строкам, столбцам и диагоналям. |
| `Hangman Game.py` | «Виселица»: случайное слово, поле из подчёркиваний, ASCII-визуализация виселицы из 7 стадий, счётчик ошибок, ввод сразу нескольких букв. |
| `Encryption Сaesar.py` | Шифр Цезаря: шифрование и расшифровка с сохранением регистра, работа с латиницей и кириллицей, приведение сдвига по модулю длины алфавита. |
| `Generate Passwords.py` | Генератор паролей: настройки собираются в словарь, пользователь выбирает наборы символов (строчные, заглавные, спецсимволы) и длину, пароль собирается случайным выбором. |

### Задачи и конспекты

| Файл | Что внутри |
|:--|:--|
| `Numpy/numpy-100.py` | Решения задач из набора [100 NumPy Exercises](https://github.com/rougier/numpy-100). Индексированные массивы, `reshape`, срезы, Broadcasting, `datetime64`, `random`, матричная арифметика, генераторы. |
| `Python ООП/Учу ооп.py` | Большой конспект: атрибуты класса и экземпляра, `__dict__`, `getattr` / `setattr` / `hasattr`, `__doc__`, методы и `self`, `__new__` / `__init__` / `__del__`, паттерн Singleton, `@classmethod` / `@staticmethod` / `@private`, инкапсуляция, «моносостояние» через общий `__shared_attrs`, перехват атрибутов через `__getattribute__` / `__setattr__` / `__getattr__` / `__delattr__`, дескрипторы `property` (getter / setter / deleter). |
| `Try_Pandas/Учу pandas.py` | Чтение CSV, деление колонок на числовые и категориальные, фильтрация и очистка выбросов, стандартизация и нормализация, `value_counts`, объединение редких категорий, кодирование через `.cat.codes` и `get_dummies`, новые признаки (`Age`, `km_year`). |
| `leetcode/20.ValidParentheses.py` | [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) — проверка корректности скобок с помощью стека. |
| `leetcode/28._Find_the_Index...py` | [28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) — поиск первого вхождения подстроки. |
| `hello.html` + `style.css` | Первая HTML-страница: минимум разметки, чтобы не забыть, как это выглядит. |
| `Try_Pandas/cars.csv`, `сars_no_dup.csv` | Датасет с характеристиками автомобилей и его версия без дубликатов. |

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
```

Запуск по желанию:

```bash
# консольные проекты (нужна только стандартная библиотека)
python Projects/tic-tac-toe.py
python Projects/Hangman\ Game.py
python Projects/Encryption\ Сaesar.py
python Projects/Generate\ Passwords.py

# задачи
python Numpy/numpy-100.py           # задачи 49–50
python leetcode/20.ValidParentheses.py

# работа с данными (нужны pandas и matplotlib)
python Try_Pandas/Учу\ pandas.py
```

> **Про кодировки имён.** В путях есть кириллица, а в двух именах файлов — невидимый
> подвох: в `сars_no_dup.csv` и `Encryption Сaesar.py` первая буква — кириллическая
> (`с` и `С`), хотя выглядит как латинская. Из-за этого `cd`, `git mv` и запуск
> из терминала иногда ведут себя непредсказуемо. Надёжнее запускать из VS Code
> или переименовать файлы в чисто латиницу.

## 🛠 Стек и инструменты

- **Python** — язык
- **NumPy** — массивы, векторные вычисления
- **pandas** — табличные данные
- **seaborn** / **matplotlib** — визуализация
- **stdlib** — `string`, `random`, `time` — для консольных проектов
- **accessify** — декораторы `@private` / `@protected` для ООП-конспекта
- **VS Code** + `venv` — рабочее окружение
- **Git / GitHub** — история обучения по коммитам

## 🎯 Планы

- [ ] Добить 100 задач по NumPy (сделано 50)
- [ ] Почистить датасет: до конца убрать выбросы, исправить `df.drop(...)` без присваивания
- [ ] Добавить ноутбук с визуализацией после очистки
- [ ] Расширить список слов в «Виселице» и сделать счёт очков
- [ ] Регулярно добавлять решённые задачи LeetCode
- [ ] Переписать ООП-конспект в тесты

## 📚 Источники

- [100 NumPy Exercises](https://github.com/rougier/numpy-100)
- [LeetCode](https://leetcode.com/)
- [Документация pandas](https://pandas.pydata.org/docs/)

## 👤 Контакты

Автор — [witmop](https://github.com/witmop).
Если нашли ошибку или хотите подсказать, как сделать код чище — открывайте issue 🐛.

---

<div align="center">
  <sub>Сделано с 🧠 и большим количеством комментариев · <a href="https://github.com/witmop/origin/commits">все коммиты</a></sub>
</div>
