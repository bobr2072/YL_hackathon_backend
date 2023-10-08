# YL_hackathon_backend
Backend для проекта хакатона "Яндекс.Практикум" и "Лента"
Авторы:

- Борис Коренбляс(https://github.com/bobr2072)
- Анастасия Пушкарная(https://github.com/Anastasia7Si)

Технологии:
Python 3.11
Django 4.2
Django REST framework 3.14
Gunicorn 21.2
Celery[redis] 5.2


## Реализовано: 
<br>Выдача данных на frontend. По запросу от frontend идёт в БД, выбирает необходимые данные,
<br>подгототавливает (если требуется), отдаёт вответе на запрос.
## В работе: 
<br>Добавление фактических данных: принимает входящий запрос на добавление исторических данных по продажам, обрабатывает их и складывает в БД. 
<br>Запускает и управляет процессом инференса. По расписанию (раз в день) данных начинает процесс прогнозирования.

## Запуск
Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:bobr2072/YL_hackathon_backend.git
cd YL_hackathon_backend
```

### Переход в папку с docker-compose
```
cd infra/
```
Создать файл .env и прописать в него свои данные.
Пример:
```
DJANGO_SECRET_KEY= 'django-insecure-example-seckret-key'
```

### Запуск проекта
```
docker-compose up -d
```

### Создание суперпользователя
```
docker-compose exec backend python manage.py createsuperuser
```

### Сбор статики
```
docker-compose exec backend python manage.py collectstatic --no-input
docker compose -f docker-compose.yml exec backend cp -r /app/collected_static/. /backend_static/static/
```

### Загрузка данных
```
docker-compose exec backend python manage.py loaddata dump.json
```

### Загрузка данных в базу из csv-файла и из базы в csv-файл
```
docker-compose exec backend python manage.py uploading_to_db
docker-compose exec backend python manage.py loading_from_db
```
