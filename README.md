# Places Remember

**Places Remember** is an intuitive application designed to capture and preserve your cherished memories associated with the various places you've visited. Whether it's a breathtaking view from a mountain peak, the bustling streets of a city you love, or the quiet corner of a local café, **Places Remember** allows you to store not just the location but the emotions and experiences that make each place unique.

With **Places Remember**, you can:

-   **Record** your personal reflections and narratives tied to each location.
-   **Attach** notes to create a vivid memory capsule.
-   **Revisit** your favorite spots through the stories you've saved, reliving those moments anytime, anywhere.

This application is more than just a travel log; it's a companion for those who want to hold onto the essence of the places that have touched their hearts. Start creating your memory map with **Places Remember** today!

# Table of contents

<!--ts-->

-   [Set up Google credentials](#set-up-google-credentials)
-   [Run the app with Docker](#run-the-app-with-docker)
    -   [Build and start the container](#build-and-start-the-container)
    -   [Testing](#testing)
-   [Run the app manually](#run-the-app-manually)
    -   [Set up](#set-up)
    -   [Testing](#testing)
    -   [Run Django server](#run-django-server)
    -   [Use Django admin page](#use-django-admin-page)

## Set up Google credentials

-   Make sure to activate the virtual environment.

```
pip install -r requirements.txt
python setup.py  # Please input your Google credentials (client_id and client_secret)
```

## Run the app with Docker

### Build and start the container

```
docker-compose up --build
```

-   Go to **[Place Remeber app page](http://127.0.0.1:8000)**

### Testing

-   Run tests for the 'places' and 'users' apps. These should all pass.

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

-   Run tests for the 'places' and 'users' apps. These should all pass.

```
python3 manage.py test places.tests
python3 manage.py test users.tests
```

### Run Django server

-   It may take a while for the Google Cloud to load the credentials. Restart the server in case cannot access the credentials.

```
python manage.py runserver
```

-   Go to **[Place Remeber app page](http://127.0.0.1:8000)**

### Use Django admin page

-   Create a superuser with

```
python manage.py createsuperuser
```

-   Go to **[Admin page](http://127.0.0.1:8000/admin)**
-   User the superuser to login into admin page
