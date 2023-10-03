# YL_hackathon_backend
Backend для проекта хакатона "Яндекс.Практикум" и "Лента"

## Запуск

### Переход в папку с docker-compose
```
cd infra/
```

### Запуск контейнеров
```
docker-compose up -d
```

### Миграции
```
docker-compose exec backend python manage.py makemigrations
```
```
docker-compose exec backend python manage.py migrate
```

### Создание суперпользователя
```
docker-compose exec backend python manage.py createsuperuser
```

### Сбор статики
```
docker-compose exec backend python manage.py collectstatic
```


