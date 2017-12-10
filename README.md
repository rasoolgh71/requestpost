# Django Celery Example

## Running Locally

pip install -r requirements.txt
```

```bash
python manage.py migrate
```

```bash
python manage.py runserver
```

```bash
celery -A mysite worker -l info
```

Make sure you have RabbitMQ service running.

```bash
rabbitmq-server
```
