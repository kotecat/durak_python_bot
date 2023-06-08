# Игра "Дурак"  ♦ ♥ ♣ ♠
_______

## Подготовка
> 1. переименуйте файл **.env.example** в **.env**
> 2. заполните его (*укажите токен бота и список админов*)
## Запуск


> #### Первый способ (автоматический)
```
> start.bat
```
Данный файл при первом запуске, сам создаёт окружение и устанавливает необходимые библиотеки

> #### Второй способ
При первом запуске:
```
> python -m pip install virtualenv
> python -m venv venv
> venv\Scripts\activate
> python -m pip install -r requirements.txt
> python durak\bot.py
```

При последующих запусках:
```
> python durak\bot.py
```
