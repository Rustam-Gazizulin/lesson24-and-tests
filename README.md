# Урок 24
Для начала работы скопируйте репозиторий на локальную машину:
c помощью команды в терминале

`https://github.com/skypro-008/lesson24-and-tests.git`

Откройте с клонированный репозиторий в PyCharm.

### Cоздайте виртуальное окружение:

#### Простой вариант:
Pycharm может предложить вам сделать это после того, как вы откроете папку с проектом.
В этом случае после открытия папки с проектом в PyCharm
Появляется всплывающее окно, Creating virtuan envrironment c тремя полями.
В первом поле выбираем размещение папки с вирутальным окружением, как правило это папка venv
в корне проекта
Во втором поле выбираем устанавливаемый интерпритатор по умолчанию (можно оставить без изменений)
В 3 поле выбираем список зависимостей (должен быть выбран фаил requirements.txt, находящийся в корне папки проекта)

#### Если этого не произошло, тогда следует выполнить следующие действия вручную:
#### Установка виртуального окружения:
1. Во вкладке File выберите пункт Settings
2. В открывшемся окне, с левой стороны найдите вкладку с именем
вашего репозитория (Project: lesson24-and-tests)
3. В выбранной вкладке откройте настройку Python Interpreter
4. В открывшейся настройке кликните на значек ⚙ (шестеренки) 
расположенный сверху справа и выберите опцию Add
5. В открывшемся окне слева выберите Virtualenv Environment, 
а справа выберите New Environment и нажмите ОК

#### Установка зависимостей:
Для этого можно воспользоваться графическим интерфейсом PyCharm,
который вам предложит сделать это как только вы откроете файл с заданием.

Или же вы можете сделать это вручную, выполнив следующую команду в терминале:
`pip install -r requirements.txt`

#### Настройка виртуального окружения завершена!

### Порядок выполнения заданий
#### Часть 1:

- part1/snake_task
- part1/clocks
- part1/clocks-2
- part1/letter_parse
- part1/create_decorator
- part1/param_decorator

#### Часть 2:

- part2/simple_types_str+
- part2/simple_types_int+
- part2/list_typing+
- part2/dict_typing
- part2/optional_typing
- part2/convert_to_dataclass
- part2/dataclass_rollback
- part2/point_factory
- part2/vk_user
- part2/dataclass_and_marshmallow
- part2/typing_introduction


Задачи описаны в комментариях в файле main.py
В текущих заданиях мы познакомимся с регулярными выражениями и датаклассами.
После того, как Вы выполнили задание, 
попробуйте запустить фаил main.py.
Вы можете это сделать, кликнув на него правой кнопкой мыши в окне проекта.

*Для каждого задания предусмотрены свои тесты
и запускать нужно именно те тесты, которые находятся в папке с заданием*

*Пожалуйста, запускайте тесты с помощью файла tests_runner.py*

