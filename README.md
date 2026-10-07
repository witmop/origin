<div align="center">

# 🧠 Учебный репозиторий

**Мой учебный репозиторий** — место, где я разбираю Python по частям:
задачи, ООП, работа с данными, алгоритмы и консольные проекты.
С 2026 года потихоньку добавляю C++ — пока это база.

Отдельно лежит **лабораторная работа по Pandas** в виде Jupyter-ноутбука —
это отработанный разбор данных, который можно открыть и прокликать по шагам.

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![pandas](https://img.shields.io/badge/pandas-2.x-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![C++](https://img.shields.io/badge/C%2B%2B-17-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)](https://isocpp.org/)
[![Последний коммит](https://img.shields.io/github/last-commit/witmop/origin?style=for-the-badge&logo=github&logoColor=white)](https://github.com/witmop/origin/commits)
[![Контрибьюторы](https://img.shields.io/github/contributors/witmop/origin?style=for-the-badge&logo=github&logoColor=white)](https://github.com/witmop/origin/graphs/contributors)

</div>

---

## 📌 О проекте

Репозиторий создан, чтобы не терять всё написанное в стол, а вести учебный дневник в Git.
Здесь лежат конспекты, решённые задачи, небольшие консольные программы и Jupyter-ноутбук:
часть кода закомментирована и служит шпаргалкой, часть запускается как есть.

**Принцип:** сначала разобраться и заставить код работать, потом причесать.
Поэтому в файлах много комментариев с объяснением «почему так, а не иначе» — это заметки
для себя, а не готовый production-код.

## 📁 Структура

```
├── Numpy/                # задачи на NumPy
├── Projects/             # консольные программы
├── Python ООП/           # конспект по объектно-ориентированному Python
├── Try_C++/              # первые программы на C++
├── Try_Pandas/           # работа с табличными данными: скрипты, CSV, ноутбук
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

### Лабораторная по Pandas — `Try_Pandas/03_Pandas_сводный_анализ.ipynb`

Ноутбук «Сводный анализ данных» (95 ячеек, 51 markdown + 44 кода) по вторичному
рынку автомобилей. Раскрыто по порядку:

| Раздел | Что внутри |
|:--|:--|
| 1–2. Загрузка и первичная проверка | `read_csv`, `info` / `shape`, `isna().sum().sum()`, `duplicated().sum()`, `drop_duplicates().copy()` |
| 3. Сводный анализ признаков | разделение колонок на численные и категориальные, `describe(percentiles=[...])`, `groupby(['Make','Year'])` + `agg(['mean','count'])`, именованная агрегация (`n=`, `median_price=`), `quantile` |
| 4. Сводные таблицы | `pivot_table` с `aggfunc='size'` и `'mean'`, `loc` / `iloc` по срезу, `crosstab` + `normalize='index'`, приведение редких кузовов к группе `Rare` |
| 5. Простая оценка цены | MAE = среднее \|y − ŷ\| по группе, оценка через `pivot_table.loc[make, year]`, `map` по группе, `groupby(...).transform('mean')` |
| 6. Графики Pandas | `Series.plot` → `marker='o'` + подписи осей + `grid`, столбчатая диаграмма, `logy=True` |
| 7–8. Отчёт и проверка | выгрузка `cars_summary_input.csv` / `cars_make_summary.csv`, сплит 80/20 с `random_state=42`, сравнение MAE общей средней и групповой оценки |

> **Про входной файл.** Ноутбук ищет `cars_processed.csv` рядом с собой, а если
> его нет — подгружает его по ссылке на внешний репозиторий курса
> (`MVRonkin/BasicDataAnalysisCourse`). В этом репозитории лежат `cars.csv`
> и `сars_no_dup.csv`, поэтому без интернета понадобится положить свой
> `cars_processed.csv` рядом с `.ipynb`.

### Задачи и конспекты

| Файл | Что внутри |
|:--|:--|
| `Numpy/numpy-100.py` | Решения задач из набора [100 NumPy Exercises](https://github.com/rougier/numpy-100). Индексированные массивы, `reshape`, срезы, Broadcasting, `datetime64`, `random`, матричная арифметика, генераторы. |
| `Python ООП/Учу ооп.py` | Большой конспект: атрибуты класса и экземпляра, `__dict__`, `getattr` / `setattr` / `hasattr`, `__doc__`, методы и `self`, `__new__` / `__init__` / `__del__`, паттерн Singleton, `@classmethod` / `@staticmethod` / `@private`, инкапсуляция, «моносостояние» через общий `__shared_attrs`, перехват атрибутов через `__getattribute__` / `__setattr__` / `__getattr__` / `__delattr__`, дескрипторы `property` (getter / setter / deleter) и собственный дескриптор данных `Integer` с магическими `__set_name__` / `__get__` / `__set__`, класс `Point3D`, Dunder-методы (`__repr__` / `__str__`, `__len__` / `__abs__`), арифметика `__add__` / `__radd__` / `__iadd__` на примере класса `Clock`, магические методы сравнения `__eq__` / `__lt__` / `__le__` и `__hash__`. |
| `Try_Pandas/Учу pandas.py` | Чтение CSV, деление колонок на числовые и категориальные, фильтрация и очистка выбросов, стандартизация и нормализация, `value_counts`, объединение редких категорий, кодирование через `.cat.codes` и `get_dummies`, новые признаки (`Age`, `km_year`). |
| `leetcode/13. Roman to Integer.py` | [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/) — перевод римского числа в арабское: сравнение соседних символов через стек, вычитание меньшего из большего. |
| `leetcode/20.ValidParentheses.py` | [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) — проверка корректности скобок с помощью стека. |
| `leetcode/28._Find_the_Index...py` | [28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) — поиск первого вхождения подстроки. |
| `leetcode/636. Exclusive Time of Functions.py` | [636. Exclusive Time of Functions](https://leetcode.com/problems/exclusive-time-of-functions/) — учёт «эксклюзивного» времени вызова функций: стек вложенных вызовов и пересчёт времени старта родителя при `start` / `end`. |
| `Try_C++/FirstProgramm.cpp` | Первая программа на C++: `#include` / `using namespace std`, `int main(int argc, const char *argv[])`, вывод через `cout`, пауза через `cin.get()`, код возврата `return 0`. |
| `hello.html` + `style.css` | Первая HTML-страница: минимум разметки, чтобы не забыть, как это выглядит. |
| `Try_Pandas/cars.csv`, `сars_no_dup.csv` | Датасет с характеристиками автомобилей и его версия без дубликатов. |

## 🚀 Как запустить

Для всего, кроме `Try_C++/`, нужен Python 3.10+.

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

# 4. Для ноутбука — ещё и Jupyter
pip install jupyter
```

Запуск по желанию:

```bash
# консольные проекты (нужна только стандартная библиотека)
python "Projects/tic-tac-toe.py"
python "Projects/Hangman Game.py"
python "Projects/Encryption Сaesar.py"
python "Projects/Generate Passwords.py"

# задачи
python Numpy/numpy-100.py                              # задачи 49–50
python "leetcode/13. Roman to Integer.py"
python "leetcode/20.ValidParentheses.py"
python "leetcode/636. Exclusive Time of Functions.py"

# работа с данными (нужны pandas и matplotlib)
python "Try_Pandas/Учу pandas.py"
```

Ноутбук запускается не скриптом, а через Jupyter — он откроется в браузере:

```bash
jupyter notebook "Try_Pandas/03_Pandas_сводный_анализ.ipynb"
# или прямо из VS Code — кнопка Run All над первым разделом
```

Ячейки уже выполнялись: `kernel: venv (3.14.4)`, результаты сохранены в `.ipynb`,
поэтому содержимое читается и без запуска.

Для `Try_C++/` нужен компилятор, а не Python:

```bash
g++ -std=c++17 Try_C++/FirstProgramm.cpp -o first_programm
./first_programm          # Linux/macOS
.\first_programm.exe      # Windows (PowerShell / cmd)
```

> **Про кодировки имён.** В путях есть кириллица, а в двух именах файлов — невидимый
> подвох: в `сars_no_dup.csv` и `Encryption Сaesar.py` первая буква — кириллическая
> (`с` и `С`), хотя выглядит как латинская. Из-за этого `cd`, `git mv` и запуск
> из терминала иногда ведут себя непредсказуемо. Поэтому в командах выше имена
> файлов взяты в кавычки. Надёжнее запускать из VS Code или переименовать файлы
> в чисто латиницу.

## 🛠 Стек и инструменты

- **Python** — основной язык
- **C++** — база: `#include`, `main`, ввод-вывод из потока (`Try_C++/`)
- **NumPy** — массивы, векторные вычисления
- **pandas** — табличные данные: `groupby`, `pivot_table`, `crosstab`, `transform`
- **Jupyter** — ноутбуки с разбором данных
- **seaborn** / **matplotlib** — визуализация
- **stdlib** — `string`, `random`, `time` — для консольных проектов
- **accessify** — декораторы `@private` / `@protected` для ООП-конспекта
- **VS Code** + `venv` — рабочее окружение
- **Git / GitHub** — история обучения по коммитам

## 🎯 Планы

- [ ] Добить 100 задач по NumPy (сделано 50)
- [ ] Почистить датасет: до конца убрать выбросы, исправить `df.drop(...)` без присваивания
- [x] Добавить ноутбук с визуализацией после очистки — сделано в `03_Pandas_сводный_анализ.ipynb`
- [ ] Передать ноутбук в лабораторную 04 и продолжить серию
- [ ] Расширить список слов в «Виселице» и сделать счёт очков
- [ ] Регулярно добавлять решённые задачи LeetCode (сделано 4)
- [ ] Переписать ООП-конспект в тесты
- [ ] Продолжить `Try_C++/`: от компиляции через терминал к своим задачам
- [ ] Разобраться со сборкой C++ в VS Code и отладкой

## 📚 Источники

- [100 NumPy Exercises](https://github.com/rougier/numpy-100)
- [LeetCode](https://leetcode.com/)
- [Документация pandas](https://pandas.pydata.org/docs/)
- [cppreference.com](https://en.cppreference.com/) — справка по C++
- [BasicDataAnalysisCourse](https://github.com/MVRonkin/BasicDataAnalysisCourse) — курс, к которому относится ноутбук 03
- [Группировка и агрегация Pandas](https://pandas.pydata.org/docs/user_guide/groupby.html)

## 👤 Контакты

Автор — [witmop](https://github.com/witmop).
Если нашли ошибку или хотите подсказать, как сделать код чище — открывайте issue 🐛.

---

<div align="center">
  <sub>Сделано с 🧠 и большим количеством комментариев · <a href="https://github.com/witmop/origin/commits">все коммиты</a></sub>
</div>
