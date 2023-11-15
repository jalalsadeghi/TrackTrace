# TrackTrace

## project setup

1- SetUp venv
```
python -m venv venv
source venv/bin/activate
```

2- install Dependencies
```
pip install -r requirements_dev.txt
```

3- create your env
```
cp .env.example .env
```

4- spin off docker compose
```
docker compose -f docker-compose.dev.yml up -d
```

5- Create tables
```
python manage.py migrate
```

6- run the project
```
python manage.py runserver
```

7- Celery and celery beat

```
  python manage.py setup_periodic_tasks
  celery -A tracktrace.tasks worker -l info --without-gossip --without-mingle --without-heartbeat
  celery -A tracktrace.tasks beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```
