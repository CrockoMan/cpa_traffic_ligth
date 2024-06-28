Тестовое задание
![image](https://github.com/CrockoMan/cpa_traffic_ligth/assets/125302139/5aaee115-521a-4eda-9cab-2cc7493f77e7)
#### Результат:
![image](https://github.com/CrockoMan/cpa_traffic_ligth/assets/125302139/07697874-8cf1-4e7c-94ce-4b7ea96fdc1d)
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:CrockoMan/cpa_traffic_ligth.git
cd cpa_traffic_ligth
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
source env/bin/activate
```

Установить зависимости из requirements.txt:

```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

Заполнение тестовыми данными:

```
python manage.py fill_bd
```
