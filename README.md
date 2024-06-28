## Тестовое задание python-разработчик CPA Traffic Light
![image](https://github.com/CrockoMan/cpa_traffic_ligth/assets/125302139/5aaee115-521a-4eda-9cab-2cc7493f77e7)
#### Результат:
![image](https://github.com/CrockoMan/cpa_traffic_ligth/assets/125302139/11d0593a-b484-410c-91ec-7f85d9927036)
### Как запустить проект:

Клонировать репозиторий и перейти в него:

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

При необходимости, заполнить .env:

```
SECRET_KEY=your_absolutely_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

Для доступа к админке создать супервользователя:

```
python3 manage.py createsuperuser
```

Запустить проект:

```
python3 manage.py runserver
```

Заполнение тестовыми данными:

```
python manage.py fill_bd
```
Автор: К.Гурашкин
