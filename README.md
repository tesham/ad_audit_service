## Django REST API for Audit service with PostgreSQL
This project implements a RESTful API using Django and Django REST Framework (DRF) for audit related task. It has a RabbitMQ consumer that receive audit data from
ip and auth service and store it to database. It also has an API to fetch audit data.

## Features

- Consume RabbitMQ audit message and store
- Fetch audit data
- PostgreSQL as the database backend

### Prerequisites

- Python 3.9
- PostgreSQL
- Django 4.1.0
- Django REST Framework 3.14

### Installation

1. clone the repository

2. Create and activate a virtual environment if it doesn't exist in the project folder:
```
    python -m venv venv
    source venv/bin/activate
```

3. Install all the requirements using `pip`:
```
    pip install -r requirements.txt
```

4. Add database connection information in main `settings.py` 
```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
```

5. Apply migrations from terminal
```
    python manage.py makemigrations audit
    python manage.py migrate audit
    
    model structure:
    class Audit(models.Model):
        user = models.CharField(max_length=100) # user who perform operation
        session_id = models.IntegerField(null=True) # user session id
        module = models.CharField(max_length=100) # audit module AUTH/IP
        label = models.CharField(max_length=100) # if AUTH label can be : Login/logout
        ip = models.CharField(max_length=100, null=True, blank=True) # ip address
        action = models.TextField(null=True, blank=True) # action taken
        created_at = models.DateTimeField(auto_now_add=True) # action perform date
```

6. Put RabbitMQ config in setting.py

```
    RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'rabbitmq')
    RABBITMQ_PORT = 5672
    RABBITMQ_USER = 'guest'
    RABBITMQ_PASSWORD = 'guest'
```
    
7. Start the server:
```
    python manage.py runserver
```


### Configuration

Update the `settings.py` file with your configurations. Ensure you have the `SECRET_KEY`, `JWT_SECRET_KEY` and other necessary configurations set.

### Entry point

audit_service/urls
