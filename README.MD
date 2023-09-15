# Игра "Дурак" ( OPEN-BETA ) ♦ ♣ ♥ ♠
_______

## *Рекомендуемая версия python - 3.11.0*
## Подготовка
> 1. переименуйте файл **.env.example** в **.env**
> 2. заполните его (*укажите токен бота и список админов*)
## Запуск


> #### Первый способ (автоматический)
###### Windows:
```
> start.bat
```
###### Linux:
```
$ sh start.sh
```
Данный файл при первом запуске, сам создаёт окружение и устанавливает необходимые библиотеки

> #### Второй способ (Ручной)
#### При первом запуске:
###### Windows:
```
> python -m pip install virtualenv
> python -m venv venv
> venv\Scripts\activate
> python -m pip install -r requirements.txt
> python durak\bot.py
```
###### Linux:
```
$ python3 -m pip install virtualenv
$ python3 -m venv venv
$ . venv/bin/activate
$ python3 -m pip install -r requirements.txt
$ python3 durak/bot.py
```

#### При последующих запусках:
###### Windows:
```
> venv\Scripts\activate
> python durak\bot.py
```
###### Linux:
```
$ . venv/bin/activate
$ python3 durak/bot.py
```