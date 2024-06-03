# places-remember

## Setup Google credentials
```
pip install -r requirements.txt
python setup.py

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata initial_data.json
python manage.py set_google_credentials
```

## Run Django server
- It may take a while for the Google Cloud to load the credentials. Restart the server in case cannot access the credentials.
```
python manage.py runserver
```

## Use Django admin page
- Create a superuser with
```
python manage.py createsuperuser
```
- Go to **[Admin page](http://127.0.0.1:8000/admin)**
- User the superuser to login into admin page
