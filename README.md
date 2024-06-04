# Places Remember

## Set up Google credentials
- Make sure to activate the virtual environment.
```
pip install -r requirements.txt
python setup.py  # Please input your Google credentials (client_id and client_secret)
```

## Run the app with Docker
### Build and start the container
```
docker-compose up --build
```
- Go to **[Place Remeber app page](http://127.0.0.1:8000)**

### Testing
- Run tests for the 'places' and 'users' apps. These should all pass.
```
docker-compose run web python manage.py test places.tests
docker-compose run web python manage.py test users.tests
```

## Run the app manually
### Set up
```
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata initial_data.json
python manage.py set_google_credentials
```

### Testing
- Run tests for the 'places' and 'users' apps. These should all pass.
```
python3 manage.py test places.tests
python3 manage.py test users.tests
```

### Run Django server
- It may take a while for the Google Cloud to load the credentials. Restart the server in case cannot access the credentials.
```
python manage.py runserver
```
- Go to **[Place Remeber app page](http://127.0.0.1:8000)**

### Use Django admin page
- Create a superuser with
```
python manage.py createsuperuser
```
- Go to **[Admin page](http://127.0.0.1:8000/admin)**
- User the superuser to login into admin page
