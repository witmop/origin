<div align="center">

# 🧠 Учебный репозиторий

**Мой учебный репозиторий** — место, где я разбираю Python по частям:
задачи, ООП, работа с данными, визуализация, запросы к API, алгоритмы
и консольные проекты. С 2026 года потихоньку добавляю C++ — пока это база.

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![pandas](https://img.shields.io/badge/pandas-2.x-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![matplotlib](https://img.shields.io/badge/matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white)](https://matplotlib.org/)
[![Requests](https://img.shields.io/badge/Requests-2.x-2B2D42?style=for-the-badge)](https://requests.readthedocs.io/)
[![C++](https://img.shields.io/badge/C%2B%2B-17-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)](https://isocpp.org/)
[![Последний коммит](https://img.shields.io/github/last-commit/witmop/origin?style=for-the-badge&logo=github&logoColor=white)](https://github.com/witmop/origin/commits)
[![Контрибьюторы](https://img.shields.io/github/contributors/witmop/origin?style=for-the-badge&logo=github&logoColor=white)](https://github.com/witmop/origin/graphs/contributors)

</div>

---

## 📌 О проекте

Репозиторий создан, чтобы не терять всё написанное в стол, а вести учебный дневник в Git.
Здесь лежат конспекты, решённые задачи и небольшие консольные программы:
часть кода закомментирована и служит шпаргалкой, часть запускается как есть.

**Принцип:** сначала разобраться и заставить код работать, потом причесать.
Поэтому в файлах много комментариев с объяснением «почему так, а не иначе» — это заметки
для себя, а не готовый production-код.

## 🆕 Что нового с прошлого обновления README

Обновление от 7 ноября 2026:

- **pandas: очистка DataFrame** (`Try_Pandas/cleaning_df.py`) — `drop_duplicates`, `dropna(ignore_index=True)`, фильтрация аномалий через `between` и булевы маски, `reset_index`, переименование столбцов, новые признаки `Age` / `km_year`, `map` для трансмиссии, категории пробега через `apply`, объединение редких марок в `Rare` (доля ≤ 1%) и сохранение результата в `cars_process.csv`.
- **matplotlib: первый конспект** (`Try_matplotlib/LearnMatplotlib.py`) — `plot` со стилями линий и маркеров, `fill_between`, несколько осей (`subplot`, `subplots`, `add_axes`, `GridSpec` с `width_ratios` / `height_ratios`), локаторы (`NullLocator`, `LinearLocator`, `MultipleLocator`, `IndexLocator`, `FixedLocator`, `LogLocator`, `MaxNLocator`), форматтеры (`NullFormatter`, `FormatStrFormatter`, `FuncFormatter`, `ScalarFormatter`, `FixedFormatter`), логарифмический масштаб (`semilogy`, `set_yscale`), оформление (`annotate`, `text`, `figtext`, фон и подписи), легенда и фигуры (`Line2D`, `Rectangle`, `add_line`, `add_patch`) и виды графиков (`step`, `stackplot`, `stem`, `scatter`).
- **requests: первые запросы к API** (`Requests/server_requests.py`) — POST / PUT / DELETE / GET через `requests`, JSON-payload и заголовки `Authorization: Bearer`, `Accept`, `Content-Type` на примере API Weeek.
- **C++: калькулятор на `if / else`** (`Try_C++/Calculator_v2.cpp`) — `float`, ввод двух чисел и знака операции, цепочка `if / else if`, отдельная проверка деления на ноль.
- **C++: случайные числа** (`Try_C++/Learn_C++.cpp`) — `srand(time(NULL))`, `rand() % 20` и диапазон `1..20`.
- **LeetCode: 2558 и 1385** — `pickGifts` (жадно берём подарки из самой большой кучи, `int(sqrt(max))`) и `findTheDistanceValue` (проверка расстояния между элементами двух массивов с запоминанием уже проверенных значений).

## 📁 Структура

```
├── Numpy/                # задачи на NumPy и конспект LearnNumpy.py
├── Projects/             # консольные программы: игры, генератор паролей, шифр Цезаря
├── Python ООП/           # конспект по объектно-ориентированному Python (LearnOOP.py)
├── Requests/             # первые запросы к API через библиотеку requests
├── Try_C++/              # первые программы на C++ и калькуляторы
├── Try_matplotlib/       # конспект по matplotlib: графики и оформление
├── Try_Pandas/           # работа с табличными данными: скрипты и CSV
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
| `Knight_and_Dragon.py` | «Рыцарь и дракон»: текстовый квест с классами `Knight`, `Sword`, `Dragon`. Три дороги на выбор, прочность меча (`check_durability` — сломанный бьёт слабее), броня поглощает 90% урона, пошаговый бой со случайным разбросом (`random.randint`), задержки `sleep`, победа/поражение по здоровью. |

### Конспект по ООП — `Python ООП/LearnOOP.py`

Самый крупный файл репозитория — больше 1000 строк, где каждая тема раскрыта рабочим
примером, а ранние примеры остаются закомментированными как шпаргалка. По порядку:

- **Основы классов** — атрибуты класса и экземпляра, `__dict__`, `getattr` / `setattr` / `hasattr` / `delattr`, `__doc__`.
- **Методы** — `self`, `@classmethod`, `@staticmethod`, `@private` из `accessify`.
- **Жизненный цикл объекта** — `__new__` / `__init__` / `__del__`, паттерн Singleton.
- **Инкапсуляция** — `_protected` и `__private`, name mangling, «моносостояние» через общий `__shared_attrs`.
- **Перехват атрибутов** — `__getattribute__` / `__setattr__` / `__getattr__` / `__delattr__`.
- **Дескрипторы** — `property` (getter / setter / deleter) и собственный дескриптор данных `Integer` с `__set_name__` / `__get__` / `__set__`.
- **Dunder-методы** — `__repr__` / `__str__`, `__len__` / `__abs__` / `__bool__`, арифметика `__add__` / `__radd__` / `__iadd__` на примере класса `Clock`, сравнения `__eq__` / `__lt__` / `__le__` и `__hash__`.
- **Протоколы коллекций** — `__getitem__` / `__setitem__` / `__delitem__` и итераторы `__iter__` / `__next__` с `StopIteration` (классы `Frange`, `Frange2D`).
- **Наследование** — базовый и дочерний класс, переопределение и расширение, делегирование через `super()`, `issubclass` / `isinstance`, наследование от встроенного `list`.
- **Наследование и инкапсуляция** — `_x1` и `__verify_coord`: почему `__`-метод родителя не виден в дочернем классе.
- **Полиморфизм** — абстрактный метод с `raise NotImplementedError` и общий цикл по списку фигур.
- **Множественное наследование** — примеси (Mixin), порядок `Notebook.__mro__`, явный вызов метода конкретного родителя.
- **`__slots__`** — экономия памяти, запрет новых атрибутов, наследование слотов.
- **Исключения** — `try` / `except` / `else` / `finally`, вложенные `try`, порядок выполнения относительно `return`, проброс исключения, `raise` и свои классы исключений с `__str__`.
- **Менеджеры контекста** — `with`, `__enter__` / `__exit__` на примере `DefenderVector` с откатом изменений при ошибке.
- **Вложенные классы** — `Women.Meta` и доступ к атрибутам внешнего и вложенного класса.
- **Метаклассы** — динамическое создание класса через `type()`, метакласс-функция `create_class_point`, метакласс-класс `Meta` от `type` с переопределённым `__init__`, подмена `__init__` класса через метакласс.
- **Data Classes** — `@dataclass` и автогенерация `__init__` / `__repr__`, `field(default_factory=list)`, свой `__eq__`, а также `field(init=False)` + `InitVar` и `__post_init__` на примере `V3D` с вычисляемой длиной.
- **Наследование Data Classes** — `@dataclass` в родителе и потомке (`Goods` → `Book`), вызов `super().__post_init__()`, авто-`uid` через атрибут класса `current_uid`, `field(default_factory=...)` с фабрикой из `staticmethod` (`GoodsMethodFactory.get_init_measure`).
- **`make_dataclass`** — генерация датакласса на лету: список полей `(имя, тип)` с `field(default=...)` и готовый метод, переданный через `namespace` (`lambda self: self.max_speed`).

### Задачи и конспекты

| Файл | Что внутри |
|:--|:--|
| `Numpy/LearnNumpy.py` | Конспект по NumPy (начат 16.10.2026), почти всё закомментировано как шпаргалка: типы данных и `dtype` / `sctypeDict`, создание массивов (`empty`, `eye`, `identity`, `zeros`, `ones`, `full`, `asmatrix`, `diag`, `diagflat`, `tri` / `tril` / `triu`, `arange`, `linspace`, `fromstring`, `fromfunction`), изменение формы (`reshape`, `view`, `ravel`, `resize`, `T`, `expand_dims`, `squeeze`, `np.newaxis`), объединение и разъединение (`hstack`, `vstack`, `column_stack`, `hsplit`, `vsplit`, `array_split`), доступ к элементам и булева индексация (`a[a>5]`, `flat`, выборка по списку индексов), операции со множествами (`any`, `isfinite`, `logical_and` / `or` / `not` / `xor`), математические функции (`sum` / `mean` с `axis`, `argmax` / `argmin`, `median`, `var`, `std`, `random` с `seed`), элементы линейной алгебры (`matmul`, `inner`, `outer`, `dot`, `matrix_rank`) и транслирование (`a1*b1+c1` без циклов и через `np.ix_`). |
| `Numpy/numpy-100.py` | Решения задач из набора [100 NumPy Exercises](https://github.com/rougier/numpy-100). Индексированные массивы, `reshape`, срезы, Broadcasting, `datetime64`, `random`, матричная арифметика, генераторы. |
| `Try_Pandas/LearnPandas.py` | Конспект по pandas (начат 20.10.2026), почти всё закомментировано как шпаргалка: `Series` и `DataFrame`, выравнивание индексов, чтение `read_csv` и запись `to_csv`, индексы и мультииндексы, работа со столбцами, арифметика, сравнение, фильтрация (`isin`, `query`), пропуски (`dropna` / `fillna`), `drop` и `astype`, доступ `iat` / `at` / `iloc` / `loc`, `unique` / `nunique` / `value_counts` / `sort_values`, `apply`, агрегация `agg`, `groupby`, объединение `concat` / `merge`, скользящие окна `rolling` и даты (`to_datetime`, `date_range`, `.dt`). |
| `Try_Pandas/Учу pandas.py` | Чтение CSV, деление колонок на числовые и категориальные, фильтрация и очистка выбросов, стандартизация и нормализация, `value_counts`, объединение редких категорий, кодирование через `.cat.codes` и `get_dummies`, новые признаки (`Age`, `km_year`). |
| `Try_Pandas/cleaning_df.py` | Пайплайн очистки датасета: удаление дубликатов и пропусков, фильтрация аномалий через `between` (год, пробег, объём двигателя, цена), `reset_index`, переименование столбцов, новые признаки `Age` / `km_year`, `map` для трансмиссии, категории пробега через `apply`, редкие марки → `Rare` и сохранение в `cars_process.csv`. |
| `Try_matplotlib/LearnMatplotlib.py` | Конспект по matplotlib (начат 04.11.2026), почти всё закомментировано как шпаргалка: `plot` и стили линий / маркеров, `fill_between`, несколько осей (`subplot`, `subplots`, `add_axes`, `GridSpec`), пределы и локаторы (`NullLocator`, `LinearLocator`, `MultipleLocator`, `IndexLocator`, `FixedLocator`, `LogLocator`, `MaxNLocator`, minor ticks), форматтеры (`NullFormatter`, `FormatStrFormatter`, `FuncFormatter`, `ScalarFormatter`, `FixedFormatter`), логарифмический масштаб (`semilogy`, `set_yscale`), оформление (`figtext`, `annotate`, `text`, фон и подписи), легенда и фигуры (`Line2D`, `Rectangle`, `add_line`, `add_patch`) и виды графиков (`step`, `stackplot`, `stem`, `scatter`). |
| `Requests/server_requests.py` | Первые запросы к API Weeek через `requests`: POST / PUT / DELETE / GET, JSON-payload, заголовки `Authorization: Bearer`, `Accept` и `Content-Type`. Все запросы закомментированы — включайте нужный блок. |
| `leetcode/13. Roman to Integer.py` | [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/) — перевод римского числа в арабское: сравнение соседних символов через стек, вычитание меньшего из большего. |
| `leetcode/20.ValidParentheses.py` | [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) — проверка корректности скобок с помощью стека. |
| `leetcode/28._Find_the_Index...py` | [28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) — поиск первого вхождения подстроки. |
| `leetcode/636. Exclusive Time of Functions.py` | [636. Exclusive Time of Functions](https://leetcode.com/problems/exclusive-time-of-functions/) — учёт «эксклюзивного» времени вызова функций: стек вложенных вызовов и пересчёт времени старта родителя при `start` / `end`. |
| `leetcode/150. Evaluate Reverse Polish Notation.py` | [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) — вычисление выражения в обратной польской записи: стек операндов, усечение результата деления в сторону нуля через `int(temp1/temp2)`. |
| `leetcode/804. Unique Morse Code Words.py` | [804. Unique Morse Code Words](https://leetcode.com/problems/unique-morse-code-words/) — перевод слов в код Морзе (индекс буквы через `ascii_lowercase.find`) и подсчёт уникальных строк через `set`. |
| `leetcode/1385. Find the Distance Value Between Two Arrays.py` | [1385. Find the Distance Value Between Two Arrays](https://leetcode.com/problems/find-the-distance-value-between-two-arrays/) — подсчёт элементов `arr1`, для которых нет элемента в `arr2` ближе чем на `d`: вложенные циклы, `abs(el1 - el2) <= d` и запоминание уже проверенных значений в `set`. |
| `leetcode/2558. Take Gifts From the Richest Pile.py` | [2558. Take Gifts From the Richest Pile](https://leetcode.com/problems/take-gifts-from-the-richest-pile/) — `k` раз берём самую большую кучу и заменяем её на `int(sqrt(...))`, результат — сумма всех куч. |
| `leetcode/3727. Maximum Alternating Sum of Squares.py` | Максимизация знакопеременной суммы квадратов: модули чисел сортируются, бо́льшая половина идёт со знаком «+», меньшая — со знаком «−». |
| `Try_C++/FirstProgramm.cpp` | Первая программа на C++: `#include` / `using namespace std`, `int main(int argc, const char *argv[])`, вывод через `cout`, пауза через `cin.get()`, код возврата `return 0`. |
| `Try_C++/Calculator.cpp` | Первый «полезный» калькулятор на C++: `cin` для двух чисел и знака операции, `switch` по операциям, отдельная проверка деления на ноль, вывод через `cout`. |
| `Try_C++/Calculator_v2.cpp` | Тот же калькулятор, но через `if / else if`: `float` для чисел, проверка деления на ноль и обработка некорректного знака операции. |
| `Try_C++/Learn_C++.cpp` | Случайные числа: `srand(time(NULL))` для новой последовательности при каждом запуске, `rand() % 20` и число от 1 до 20. |
| `hello.html` + `style.css` | Первая HTML-страница: минимум разметки, чтобы не забыть, как это выглядит. |
| `Try_Pandas/cars.csv`, `сars_no_dup.csv` | Датасет с характеристиками автомобилей и его версия без дубликатов; `cleaning_df.py` сохраняет очищенную версию в `cars_process.csv`. |

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
pip install numpy pandas seaborn matplotlib requests accessify
```

Запуск по желанию:

```bash
# консольные проекты (нужна только стандартная библиотека)
python "Projects/tic-tac-toe.py"
python "Projects/Hangman Game.py"
python "Projects/Encryption Сaesar.py"
python "Projects/Generate Passwords.py"
python "Projects/Knight_and_Dragon.py"     # бой идёт в реальном времени (time.sleep)

# конспекты (в основном закомментированы — раскомментируйте нужный блок)
python "Python ООП/LearnOOP.py"
python Numpy/LearnNumpy.py

# задачи
python Numpy/numpy-100.py                              # задачи 49–50
python "leetcode/13. Roman to Integer.py"
python "leetcode/20.ValidParentheses.py"
python "leetcode/150. Evaluate Reverse Polish Notation.py"
python "leetcode/636. Exclusive Time of Functions.py"
python "leetcode/804. Unique Morse Code Words.py"
python "leetcode/1385. Find the Distance Value Between Two Arrays.py"
python "leetcode/3727. Maximum Alternating Sum of Squares.py"

# работа с данными (нужны pandas и matplotlib)
python "Try_Pandas/Учу pandas.py"
python Try_Pandas/cleaning_df.py        # чистит cars.csv и пишет cars_process.csv
python Try_Pandas/LearnPandas.py        # конспект, почти всё закомментировано
python Try_matplotlib/LearnMatplotlib.py  # конспект, почти всё закомментировано

# запросы к API (нужен requests)
python Requests/server_requests.py      # все запросы закомментированы — включите нужный блок
```

Для `Try_C++/` нужен компилятор, а не Python:

```bash
# первая программа
g++ -std=c++17 Try_C++/FirstProgramm.cpp -o first_programm
./first_programm          # Linux/macOS
.\first_programm.exe      # Windows (PowerShell / cmd)

# калькулятор (switch)
g++ -std=c++17 Try_C++/Calculator.cpp -o calculator
./calculator

# калькулятор на if / else
g++ -std=c++17 Try_C++/Calculator_v2.cpp -o calculator_v2
./calculator_v2

# случайные числа
g++ -std=c++17 Try_C++/Learn_C++.cpp -o random_numbers
./random_numbers
```

> **Про русский текст в консоли C++.** Подсказки в `Calculator.cpp` и `Calculator_v2.cpp` написаны по-русски,
> а исходник сохранён в UTF-8. В старой Windows-консоли вместо текста может появиться
> мусор — помогает `chcp 65001` перед запуском или терминал из VS Code.

> **Про `Learn_C++.cpp`.** Если компилятор не видит `srand` / `time`, добавьте `#include <ctime>` —
> в комментарии к файлу это тоже отмечено.

> **Про токен в `Requests/server_requests.py`.** Токен вписан прямо в код и закомментирован
> вместе с запросами. Для реальных проектов его стоит хранить в переменной окружения или
> `.env`, а не в репозитории.

> **Про кодировки имён.** В путях есть кириллица, а в двух именах файлов — невидимый
> подвох: в `сars_no_dup.csv` и `Encryption Сaesar.py` первая буква — кириллическая
> (`с` и `С`), хотя выглядит как латинская. Из-за этого `cd`, `git mv` и запуск
> из терминала иногда ведут себя непредсказуемо. Поэтому в командах выше имена
> файлов взяты в кавычки. Надёжнее запускать из VS Code или переименовать файлы
> в чисто латиницу.

> **Про `Knight_and_Dragon.py`.** В коде есть `time.sleep` по 3–7 секунд, поэтому бой
> занимает реальное время. Русский текст в `input()` и `print()` требует UTF-8 терминала.

## 🛠 Стек и инструменты

- **Python** — основной язык
- **C++** — база: `#include`, `main`, потоки `cin` / `cout`, ветвление `switch` / `if-else`, `srand` / `rand` (`Try_C++/`)
- **NumPy** — массивы, векторные вычисления, `dtype` / `reshape` / broadcasting, `linalg` (`Numpy/`)
- **pandas** — табличные данные: `Series` / `DataFrame`, индексация, фильтрация и пропуски, `groupby`, `merge` / `concat`, `rolling`, работа с датами, очистка датасета (`Try_Pandas/`)
- **matplotlib** — графики: `plot`, `subplot` / `GridSpec`, локаторы и форматтеры, логарифмический масштаб, легенды, `step` / `stackplot` / `stem` / `scatter` (`Try_matplotlib/`)
- **seaborn** — визуализация поверх matplotlib
- **requests** — HTTP-запросы `GET` / `POST` / `PUT` / `DELETE`, JSON и заголовки авторизации (`Requests/`)
- **stdlib** — `string`, `random`, `time`, `dataclasses.make_dataclass` — для консольных проектов и конспектов
- **accessify** — декораторы `@private` / `@protected` для ООП-конспекта
- **VS Code** + `venv` — рабочее окружение
- **Git / GitHub** — история обучения по коммитам

## 🎯 Планы

- [ ] Дополнять конспект по NumPy новыми темами (основы, математика, `linalg` и broadcasting уже разобраны)
- [ ] Добить 100 задач по NumPy (сделано 50)
- [x] Почистить датасет: дубликаты, пропуски и выбросы в `Try_Pandas/cleaning_df.py`, новые признаки и `cars_process.csv`
- [ ] Расширить список слов в «Виселице» и сделать счёт очков
- [ ] Добавить в «Рыцаря и дракона» второй исход для 2-й дороги (сейчас там только история без боя) и баланс урона
- [ ] Регулярно добавлять решённые задачи LeetCode (сделано 9)
- [ ] Переписать ООП-конспект в тесты
- [ ] Продолжить `Try_C++/`: от компиляции через терминал к своим задачам
- [x] Настроить сборку C++ в VS Code (`g++` через `tasks.json`, сам `.vscode/` в `.gitignore`)
- [ ] Разобраться с отладкой C++ в VS Code
- [ ] Продолжить matplotlib: 3D-графики, сохранение в файлы, свои стили
- [ ] Доделать `Requests/`: вынести токен в переменные окружения и обработать коды ответов

## 📚 Источники

- [100 NumPy Exercises](https://github.com/rougier/numpy-100)
- [LeetCode](https://leetcode.com/)
- [Документация NumPy](https://numpy.org/doc/stable/) — создание массивов, `linalg`, broadcasting
- [Документация pandas](https://pandas.pydata.org/docs/)
- [Документация matplotlib](https://matplotlib.org/stable/) — графики, локаторы, форматтеры, логарифмический масштаб
- [Документация requests](https://requests.readthedocs.io/) — HTTP-запросы, JSON и заголовки
- [cppreference.com](https://en.cppreference.com/) — справка по C++
- [Группировка и агрегация Pandas](https://pandas.pydata.org/docs/user_guide/groupby.html)

## 👤 Контакты

Автор — [witmop](https://github.com/witmop).
Если нашли ошибку или хотите подсказать, как сделать код чище — открывайте issue 🐛.

---

<div align="center">
  <sub>Сделано с 🧠 и большим количеством комментариев · <a href="https://github.com/witmop/origin/commits">все коммиты</a></sub>
</div>
